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

- Python 3.8+
- MySQL 8.0+
- Node.js 16+ (for Tailwind CSS)

### Setup Steps

1. Clone the repository and navigate to the project directory

2. Create and activate a virtual environment:
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

3. Install Python dependencies:
```bash
pip install -r requirements.txt
```

4. Set up MySQL database:
```bash
mysql -u root -p
CREATE DATABASE find_your_software;
USE find_your_software;
SOURCE flaskr/schema.sql;
```

5. Configure database connection:

Create `instance/config.py`:
```python
MYSQL_DATABASE_PASSWORD = 'your_mysql_password'
```

6. Install Node.js dependencies and build Tailwind CSS:
```bash
npm install
npx tailwindcss -i ./flaskr/static/input.css -o ./flaskr/static/style.css
```

## Running the Application

### Flask Application (Port 5000)

```bash
flask --app flaskr run --debug
```

Visit: http://127.0.0.1:5000

### Django Admin Panel (Port 8000)

```bash
cd admin_panel
python manage.py runserver 8000
```

Visit: http://127.0.0.1:8000/admin

Login with the superuser credentials you created during setup.
login: admin
password: admin123

## API Usage

### POST /recommend

Search for software based on user requirements.

**Request:**
```bash
curl -X POST http://127.0.0.1:5000/recommend \
  -H "Content-Type: application/json" \
  -d '{"query": "project management with kanban boards"}'
```

**Response:**
```json
{
  "success": true,
  "software": {
    "name": "Trello",
    "description": "Visual project management with kanban boards",
    "features": "kanban boards, checklists, due dates, labels...",
    "category": "project_management"
  },
  "score": 0.716,
  "explanation": "Best match (similarity: 0.716)"
}
```

## Development

### Tailwind CSS Development Mode

For automatic CSS rebuilding during development:
```bash
npx tailwindcss -i ./flaskr/static/input.css -o ./flaskr/static/style.css --watch
```

### Creating Django Superuser

```bash
cd admin_panel
python manage.py createsuperuser
```