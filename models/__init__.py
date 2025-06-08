# This file makes the models directory a Python package
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# Import all models so they are registered with SQLAlchemy
from .user import User
from .business import BusinessInfo
from .preferences import Preferences
from .dashboard import DashboardSummary
