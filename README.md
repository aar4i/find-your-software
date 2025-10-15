# Find Your Software

An AI-powered software recommendation system that uses semantic search to match user requirements with the most suitable software solutions.

## Overview

This application combines Flask, Haystack AI, and a MySQL database to provide intelligent software recommendations. Users describe what they need in natural language, and the system uses embeddings and semantic similarity to find the best match from a curated database of 15 popular software tools.

## Tech Stack:

### Backend
- **Flask** - Web framework and API  
- **Django** - Admin panel for managing software entries  
- **Haystack** - AI search framework  
- **Sentence Transformers** - Embedding model (all-MiniLM-L6-v2)  
- **MySQL** - Database  

### Frontend
- **HTML/JavaScript** - User interface  
- **Tailwind CSS** - Styling  

### Database
The application includes 15 pre-configured software entries:
- Notion, Jira, Figma, Salesforce, VS Code  
- QuickBooks, Moodle, Canva, Trello, SAP ERP  
- Asana, Adobe XD, GitHub, FreshBooks, Zoom  

## Features

- Semantic search using AI embeddings  
- Natural language query processing  
- Real-time software recommendations with similarity scores  
- RESTful API  
- Django admin panel for managing software database  
- Responsive web interface  

### Setup Steps
**Make sure Docker Desktop is running before starting!**    

1. **Clone the repository and navigate to the project directory:**
   ```bash
   git clone https://github.com/yourusername/find_your_software.git
    ```
    ```bash
   cd find_your_software
  
   docker-compose up -d
    ```
2. **Run migrations:**

```bash
   docker exec -it find_your_software_admin python manage.py migrate
   ```

3. **Add columns to the table:**

   ```bash
   docker exec -it find_your_software_db mysql -u root -pmysecretpassword
    ```

4. **In MySQL console:**

    ```bash
        USE find_your_software;

        ALTER TABLE software 
        ADD COLUMN created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
        ADD COLUMN updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP;

        EXIT;
    ```

5. **Create a superuser:**
    ```bash
    docker exec -it find_your_software_admin python manage.py createsuperuser
    ```

6. **Open in your browser:**

        Django Admin: http://127.0.0.1:8000/admin/
        Flask API: http://127.0.0.1:5050/


