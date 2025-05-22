# Django Portfolio Website

A modern, responsive portfolio website built with Django, featuring interactive elements and cloud-based storage. Designed to showcase projects, activities, and professional experiences in a clean, user-friendly format.

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![Python](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Django](https://img.shields.io/badge/django-4.0+-green.svg)](https://www.djangoproject.com/)

**Repository:** [github.com/your-username/django-portfolio](https://github.com/your-username/django-portfolio)

![Portfolio Website](https://matty-122726483175.europe-west1.run.app/)

## Features

- **Interactive Constellation Background**: Dynamic WebGL-powered background that responds to user interactions
- **Responsive Design**: Fully responsive layout that works across desktop, tablet, and mobile devices
- **Project Showcase**: Highlights personal and professional projects with details and links
- **Activities & Experience**: Displays educational and professional experience with visual timeline
- **Media Storage**: Google Cloud Storage integration for reliable media management
- **Database-Driven**: All content managed through a custom admin interface

## Tech Stack

- **Backend**: Django (Python)
- **Database**: PostgreSQL (Railway)
- **Storage**: Google Cloud Storage
- **Frontend**: HTML, CSS, JavaScript
- **Deployment**: Google Cloud Run
- **CI/CD**: Google Cloud Build
- **Version Control**: Git/GitHub

## Local Development Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/Matty27100/django-portfolio.git
   cd django-portfolio
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   source venv/Scripts/activate  # Windows
   # OR
   source venv/bin/activate      # macOS/Linux
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**
   - Create a .env file in the project root with:
   ```
   DATABASE_URL=your_database_url
   DEBUG=True
   SECRET_KEY=your_secret_key
   ALLOWED_HOSTS=localhost,127.0.0.1
   GS_BUCKET_NAME=your_gcs_bucket_name
   GOOGLE_APPLICATION_CREDENTIALS=path_to_credentials_file.json
   ```

5. **Run migrations**
   ```bash
   python manage.py migrate
   ```

6. **Create a superuser**
   ```bash
   python manage.py createsuperuser
   ```

7. **Run the development server**
   ```bash
   python manage.py runserver
   ```

8. **Access the site**
   - Frontend: http://127.0.0.1:8000/
   - Admin interface: http://127.0.0.1:8000/admin/

## Deployment

The site is deployed on Google Cloud Run using Docker:

1. **Build the Docker image**
   ```bash
   gcloud builds submit --tag gcr.io/YOUR_PROJECT_ID/portfolio
   ```

2. **Deploy to Cloud Run**
   ```bash
   gcloud run deploy portfolio --image gcr.io/YOUR_PROJECT_ID/portfolio --platform managed --region YOUR_REGION
   ```

## Backup and Restore

To backup your database content:

```bash
python manage.py dumpdata --exclude auth.permission --exclude contenttypes --exclude admin.logentry --exclude sessions.session --indent 2 > backups/portfolio_backup_$(date +%Y%m%d).json
```

To restore from a backup:

```bash
python manage.py loaddata backups/portfolio_backup_YYYYMMDD.json
```

## Project Structure

```
django-portfolio/
├── backups/                # Database backups
├── portfolio/              # Main Django project directory
│   ├── settings.py         # Project settings
│   ├── urls.py             # Main URL routing
│   └── wsgi.py             # WSGI configuration
├── project/                # Main Django app
│   ├── admin.py            # Admin interface configuration
│   ├── models.py           # Database models
│   ├── views.py            # View controllers
│   ├── urls.py             # App URL routing
│   ├── static/             # Static files (CSS, JS, images)
│   ├── templates/          # HTML templates
│   └── templatetags/       # Custom template tags
├── staticfiles/            # Collected static files
├── venv/                   # Virtual environment
├── .env                    # Environment variables
├── .gitignore              # Git ignore file
├── Dockerfile              # Docker configuration
├── manage.py               # Django management script
└── requirements.txt        # Python dependencies
```

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Contact

Matei Bejinaru - [bejinaru.matei7@gmail.com](mailto:bejinaru.matei7@gmail.com)

---

Replace placeholder values with your actual information before publishing.