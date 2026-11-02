# St. Bottle Cathedral - Production Django Website

This is a complete, production-ready Django application for St. Bottle Cathedral. It features a modern Vanilla CSS frontend, member authentication, sermons, events, prayer requests, and donations.

## Features
- **Custom User Model:** Advanced member registration and profile management.
- **Modern Frontend:** Premium, responsive design with dynamic animations (Vanilla CSS).
- **Core App:** Home, About, Contact, and Livestream views.
- **Sermons:** Audio, video (iframe embed), and text descriptions.
- **Events:** Calendar events with start/end times and locations.
- **Prayers:** Public and private prayer requests for the congregation.
- **Donations:** Donation tracking model with a frontend form.
- **PostgreSQL Ready:** Configured via `dj-database-url` to use PostgreSQL seamlessly.

## Local Development Setup

1. **Clone the repository:**
   ```bash
   git clone <repo-url>
   cd church2
   ```

2. **Create and activate a virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Environment Variables:**
   Create a `.env` file in the project root:
   ```env
   SECRET_KEY=your-secret-key
   DEBUG=True
   ALLOWED_HOSTS=*
   # DATABASE_URL=postgres://user:password@localhost:5432/church_db (Optional for local)
   ```

5. **Run Migrations:**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

6. **Create Superuser:**
   ```bash
   python manage.py createsuperuser
   ```

7. **Run the server:**
   ```bash
   python manage.py runserver
   ```

## Production Deployment (Heroku / Render / VPS)

### 1. PostgreSQL Database
The app is configured to use `dj-database-url`. Simply set the `DATABASE_URL` environment variable in your production environment (e.g., Render Dashboard).

### 2. Static Files
`whitenoise` is configured to serve static files in production. Run `python manage.py collectstatic` during the build phase.

### 3. Docker (Optional)
A `Dockerfile` is provided for containerized deployment.
```bash
docker build -t stbottle .
docker run -p 8000:8000 --env-file .env stbottle
```
