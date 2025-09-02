# Incident Reporter

An incident reporting web app for aged care settings, developed with Django and HTMX. Focused on clean UX, semantic structure, and progressive enhancement. Currently refining template logic and exploring Tailwind CSS for responsive design, with plans to experiment with Alpine.js for lightweight interactivity.

## Features

-  Incident submission via dynamic Django form
-  Server-side pagination with HTMX interactions (in progress)
-  Modular template structure with conditional rendering
-  Semantic HTML and accessibility aligned with WCAG principles
-  Planned integration of Tailwind CSS for responsive design
-  Alpine.js planned for lightweight client-side interactivity

## Tech Stack

- **Backend**: Django (views, models, forms, template inheritance)
- **Frontend**: HTMX, semantic HTML, WCAG-aligned accessibility
- **Styling**: Tailwind CSS *(in progress)*
- **Interactivity**: Alpine.js *(in progress)*

## Getting Started

```bash
# Clone the repo
git clone https://github.com/your-username/incident-reporter.git
cd incident-reporter

# Set up virtual environment
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows

# Install dependencies
pip install -r requirements.txt

# Run migrations
python manage.py migrate

# Start development server
python manage.py runserver
