DevConnect Backend

This is the backend for DevConnect, built using **FastAPI** and **PostgreSQL**.

## 🚀 Features
• Implement persistent user authentication (signup & login).

• Allow users to create a profile with basic information.

• Enable users to post projects with title, description, and relevant links.

• Other users should be able to view all projects and leave feedback (comment) on them.

• Add a feature to search for other users by name or project.

• The app should be visually clean, responsive, and functionally complete.

## 🚀 Getting Started (Locally)

### 1. Install Dependencies
cd backend
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt
▶️ Run Locally
uvicorn app.main:app --reload
Access: http://localhost:8000/docs

2. Environment Variables
Create a .env file in the root:
DATABASE_URL=postgresql://user:password@localhost:5432/devconnect
SECRET_KEY=your-secret-key

3. Database Setup
Ensure your PostgreSQL database is created and accessible. The database models will auto-create on server start via:
Base.metadata.create_all(bind=engine)

4. 🛠️ Tech Stack
FastAPI
SQLAlchemy
PostgreSQL
Pydantic
Uvicorn