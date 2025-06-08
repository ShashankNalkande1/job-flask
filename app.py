from flask import Flask
from flask_login import LoginManager
from flask_wtf.csrf import CSRFProtect
from flask_bcrypt import Bcrypt
from models import db
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Initialize extensions
login_manager = LoginManager()
csrf = CSRFProtect()
bcrypt = Bcrypt()

def create_app():
    app = Flask(__name__)
    
    # Configuration
    app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'dev-secret-key-change-in-production')
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'sqlite:///app.db')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    # Initialize extensions with app
    db.init_app(app)
    login_manager.init_app(app)
    csrf.init_app(app)
    bcrypt.init_app(app)
    
    # Login manager configuration
    login_manager.login_view = 'auth.login'
    login_manager.login_message = 'Please log in to access this page.'
    login_manager.login_message_category = 'info'
    
    @login_manager.user_loader
    def load_user(user_id):
        from models.user import User
        return User.query.get(int(user_id))
    
    # Import and register blueprints
    from routes.auth import auth_bp
    from routes.onboarding import onboarding_bp
    from routes.dashboard import dashboard_bp
    from routes.api import api_bp
    
    app.register_blueprint(auth_bp, url_prefix='/auth')
    app.register_blueprint(onboarding_bp, url_prefix='/onboarding')
    app.register_blueprint(dashboard_bp)
    app.register_blueprint(api_bp, url_prefix='/api')
    
    # Create database tables
    with app.app_context():
        # Import models to ensure they are registered
        from models.user import User
        from models.business import BusinessInfo
        from models.preferences import Preferences
        from models.dashboard import DashboardSummary
        
        db.create_all()
        
        # Create dummy dashboard data if it doesn't exist
        if not DashboardSummary.query.first():
            dummy_data = DashboardSummary(
                team_count=12,
                active_projects=8,
                notifications=5
            )
            db.session.add(dummy_data)
            db.session.commit()
    
    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True, host='0.0.0.0')
