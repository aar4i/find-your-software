from haystack import Document, Pipeline
from haystack.document_stores.in_memory import InMemoryDocumentStore
from haystack.components.retrievers.in_memory.embedding_retriever import InMemoryEmbeddingRetriever
from haystack.components.embedders.sentence_transformers_document_embedder import SentenceTransformersDocumentEmbedder
from haystack.components.embedders.sentence_transformers_text_embedder import SentenceTransformersTextEmbedder
import logging

logger = logging.getLogger(__name__)


class SoftwareRecommender:
    def __init__(self):
        """Initialize empty recommender"""
        self.document_store = None
        self.pipeline = None
    
    def load_from_mysql(self, mysql_connection):
        """
        Load all software from MySQL database.
        
        Args:
            mysql_connection: Flask-MySQL connection
            
        Returns:
            list of Haystack Documents
        """
        try:
            cursor = mysql_connection.get_db().cursor()
            cursor.execute('SELECT id, name, features, description, category FROM software')
            software_list = cursor.fetchall()
            cursor.close()
            
            logger.info(f"Loading {len(software_list)} software from MySQL...")
            
            documents = []
            for software in software_list:
                sw_id = software[0]
                name = software[1]
                features = software[2]
                description = software[3]
                category = software[4]
                
                content = f"{name}. {description}. Features: {features}"
                
                doc = Document(
                    content=content,
                    meta={
                        "id": sw_id,
                        "name": name,
                        "description": description,
                        "features": features,
                        "category": category
                    }
                )
                documents.append(doc)
            
            logger.info(f"✅ Loaded {len(documents)} documents from MySQL")
            return documents
            
        except Exception as e:
            logger.error(f"❌ Error loading from MySQL: {e}")
            raise
        
    def initialize(self, mysql_connection):
        """
        Initialize Haystack with real data from MySQL.
        This will be called by Flask app.
        
        Args:
            mysql_connection: Flask-MySQL connection
        """
        try:
            logger.info("Initializing Haystack with MySQL data...")
            
            # 1. Create DocumentStore
            self.document_store = InMemoryDocumentStore()
            
            # 2. Load documents from MySQL
            docs = self.load_from_mysql(mysql_connection)
            
            # 3. Create document embedder
            doc_embedder = SentenceTransformersDocumentEmbedder(
                model="sentence-transformers/all-MiniLM-L6-v2"
            )
            doc_embedder.warm_up()
            
            # 4. Generate embeddings
            docs_with_embeddings = doc_embedder.run(docs)
            self.document_store.write_documents(docs_with_embeddings["documents"])
            
            # 5. Create search pipeline
            self.create_search_pipeline()
            
            logger.info("✅ Haystack initialized with MySQL data!")
            return True
            
        except Exception as e:
            logger.error(f"❌ Error initializing Haystack: {e}")
            raise


    def create_search_pipeline(self):
        """
        Create search pipeline with text embedder and retriever.
        """
        try:
            logger.info("Creating search pipeline...")
            
            # Create pipeline
            self.pipeline = Pipeline()
            
            # Text embedder for user queries
            text_embedder = SentenceTransformersTextEmbedder(
                model="sentence-transformers/all-MiniLM-L6-v2"
            )
            
            # Retriever to find similar documents
            retriever = InMemoryEmbeddingRetriever(
                document_store=self.document_store,
                top_k=1
            )
            
            # Add components
            self.pipeline.add_component("text_embedder", text_embedder)
            self.pipeline.add_component("retriever", retriever)
            
            # Connect: query → embedder → retriever
            self.pipeline.connect("text_embedder.embedding", "retriever.query_embedding")
            
            logger.info("✅ Pipeline created!")
            return True
            
        except Exception as e:
            logger.error(f"❌ Error creating pipeline: {e}")
            return False
        
    def recommend(self, query: str):
        """
        Get software recommendation based on query.
        
        Args:
            query: User's description of needed functionality
            
        Returns:
            dict with recommendation
        """
        try:
            if not self.pipeline:
                return {
                    "success": False,
                    "message": "Pipeline not initialized"
                }
            
            # Run search
            result = self.pipeline.run({
                "text_embedder": {"text": query},
                "retriever": {"top_k": 1}
            })
            
            documents = result["retriever"]["documents"]
            
            if not documents:
                return {
                    "success": False,
                    "message": "No matching software found"
                }
            
            # Get best match
            best = documents[0]
            
            return {
                "success": True,
                "software": {
                    "name": best.meta["name"],
                    "description": best.meta["description"],
                    "features": best.meta["features"],
                    "category": best.meta["category"]
                },
                "score": round(best.score, 3),
                "explanation": f"Best match (similarity: {round(best.score, 3)})"
            }
            
        except Exception as e:
            logger.error(f"Error in recommend: {e}")
            return {
                "success": False,
                "message": str(e)
            }
        
# Global instance for Flask app
recommender = SoftwareRecommender() 
        