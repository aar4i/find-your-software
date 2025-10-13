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

## Installation

### Prerequisites

- Docker 20.10+  
- Docker Compose 2.0+  

### Setup Steps

1. **Clone the repository and navigate to the project directory:**
   ```bash
   git clone https://github.com/yourusername/find_your_software.git
   cd find_your_software

2. **Build and start all services with Docker Compose:**
    ```bash

    docker-compose up --build

    This will:

    Build and run the Flask API
    Launch the Django admin panel
    Initialize the MySQL database
    Connect all containers in a shared Docker network

3. **Access the services:**

    Flask app → http://localhost:5050

    Django admin → http://localhost:8000/admin

4. **Stop the containers:**

    docker-compose down

5. **(Optional) Rebuild everything from scratch:**

    docker-compose up --build --force-recreate



Login with the superuser credentials you created during setup.

### Creating Django Superuser

```bash
cd admin_panel
python manage.py createsuperuser
```

login: admin,
password: admin123