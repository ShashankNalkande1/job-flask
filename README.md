# Flask Dashboard Application

A comprehensive web application built with Flask, featuring user authentication, onboarding process, and an interactive dashboard with project and team management capabilities.




<img src="https://raw.githubusercontent.com/ShashankNalkande1/job-flask/main/Screenshot%202025-06-08%20092157.png" alt="Dashboard Screenshot">
<img src="https://raw.githubusercontent.com/ShashankNalkande1/job-flask/main/Screenshot%202025-06-08%20092211.png" alt="Screenshot" style="width:100%; max-width:800px; border:1px solid #ccc;
   border-radius:10px;">
   <img src="https://raw.githubusercontent.com/ShashankNalkande1/job-flask/main/Screenshot%202025-06-08%20092225.png" alt="Screenshot" style="width:100%; max-width:800px; border:1px solid #ccc; border-radius:10px;">



## Features

### Core Functionality
- **User Authentication**: Secure registration and login system
- **Multi-Step Onboarding**: 3-step guided setup process for new users
- **Interactive Dashboard**: Statistics, charts, and activity timeline
- **Project Management**: Create and manage projects with priorities and deadlines
- **Team Management**: Add team members with role-based access
- **Profile Management**: User profile and preferences customization
- **Responsive Design**: Mobile-friendly interface with dark/light theme support

### Technical Features
- **Flask Framework**: Modern Python web framework
- **SQLite Database**: Lightweight database with SQLAlchemy ORM
- **Form Validation**: Comprehensive client-side and server-side validation
- **CSRF Protection**: Security measures against cross-site request forgery
- **Bootstrap 5**: Modern UI components and responsive design
- **Chart.js Integration**: Interactive data visualization

## Installation & Setup

### Prerequisites
- Python 3.8+
- pip (Python package installer)

### Installation Steps

1. **Clone/Download the project**
   ```bash
   # Navigate to project directory
   cd "job flask"
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**
   ```bash
   python app.py
   ```

4. **Access the application**
   - Open your browser and navigate to: `http://127.0.0.1:5000`
   - For mobile access (same WiFi network): `http://[your-ip]:5000`

## Project Structure

```
job flask/
├── app.py                 # Main Flask application
├── requirements.txt       # Python dependencies
├── README.md             # Project documentation
├── .env                  # Environment variables (optional)
│
├── models/               # Database models
│   ├── __init__.py
│   ├── user.py          # User authentication model
│   ├── business.py      # Business information model
│   ├── preferences.py   # User preferences model
│   └── dashboard.py     # Dashboard statistics model
│
├── routes/              # Application routes/blueprints
│   ├── __init__.py
│   ├── auth.py         # Authentication routes
│   ├── onboarding.py   # Onboarding process routes
│   ├── dashboard.py    # Dashboard routes
│   └── api.py          # API endpoints
│
├── forms/              # WTForms form definitions
│   ├── __init__.py
│   ├── auth.py        # Authentication forms
│   └── onboarding.py  # Onboarding forms
│
├── templates/          # Jinja2 HTML templates
│   ├── base.html      # Base template
│   ├── auth/          # Authentication templates
│   ├── dashboard/     # Dashboard templates
│   └── onboarding/    # Onboarding templates
│
├── static/            # Static assets
│   ├── css/
│   │   └── custom.css # Custom styles
│   └── js/
│       └── dashboard.js # Dashboard JavaScript
│
└── instance/          # Instance-specific files
    └── app.db        # SQLite database
```

## Usage Guide

### Getting Started

1. **Registration**: Create a new account using the registration form
2. **Onboarding**: Complete the 3-step onboarding process:
   - Personal Information
   - Business Information  
   - Preferences Setup
3. **Dashboard**: Access the main dashboard with statistics and features
4. **Project Management**: Create and manage projects
5. **Team Management**: Add team members and manage roles

### API Endpoints

- `POST /api/projects` - Create new project
- `POST /api/team-members` - Add team member
- `GET/PATCH /api/profile` - User profile management
- `GET/POST /api/preferences` - User preferences

## Configuration

### Environment Variables (Optional)
Create a `.env` file in the root directory:

```env
SECRET_KEY=your-secret-key-here
DATABASE_URL=sqlite:///app.db
```

### Database
The application automatically creates the SQLite database and tables on first run.

## Security Features

- **Password Hashing**: Bcrypt encryption for user passwords
- **CSRF Protection**: Cross-site request forgery protection
- **Form Validation**: Comprehensive input validation
- **Session Management**: Secure user session handling

## Browser Compatibility

- Chrome 90+
- Firefox 88+
- Safari 14+
- Edge 90+
- Mobile browsers (iOS Safari, Chrome Mobile)

## Development

### Key Technologies
- **Backend**: Flask, SQLAlchemy, Flask-Login, Flask-WTF
- **Frontend**: Bootstrap 5, Chart.js, Vanilla JavaScript
- **Database**: SQLite (development), easily adaptable to PostgreSQL/MySQL
- **Security**: Flask-Bcrypt, CSRF protection

### Code Quality
- Modular architecture with blueprints
- Separation of concerns (models, views, forms)
- Comprehensive error handling
- Mobile-responsive design
- Cross-browser compatibility

## License

This project is developed for educational and professional demonstration purposes.

## Support

For technical support or questions about this application, please contact the development team.
