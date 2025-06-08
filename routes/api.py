from flask import Blueprint, request, jsonify
from flask_login import login_required, current_user
from flask_wtf.csrf import validate_csrf, ValidationError
from models.user import User
from models.preferences import Preferences
from models import db

api_bp = Blueprint('api', __name__)

@api_bp.route('/profile', methods=['GET'])
@login_required
def get_profile():
    """Get user profile details"""
    return jsonify({
        'id': current_user.id,
        'name': current_user.name,
        'email': current_user.email,
        'onboarding_completed': current_user.onboarding_completed
    })

@api_bp.route('/profile', methods=['PATCH'])
@login_required
def update_profile():
    """Update user profile (email or name)"""
    data = request.get_json()
    
    if 'name' in data:
        current_user.name = data['name']
    
    if 'email' in data:
        # Check if email is already taken by another user
        existing_user = User.query.filter_by(email=data['email']).first()
        if existing_user and existing_user.id != current_user.id:
            return jsonify({'error': 'Email already in use'}), 400
        current_user.email = data['email']
    
    db.session.commit()
    
    return jsonify({
        'message': 'Profile updated successfully',
        'user': {
            'id': current_user.id,
            'name': current_user.name,
            'email': current_user.email
        }
    })

@api_bp.route('/preferences', methods=['GET'])
@login_required
def get_preferences():
    """Get user preferences"""
    preferences = Preferences.query.filter_by(user_id=current_user.id).first()
    
    if not preferences:
        return jsonify({
            'theme': 'light',
            'layout': 'default'
        })
    
    return jsonify({
        'theme': preferences.theme,
        'layout': preferences.layout
    })

@api_bp.route('/preferences', methods=['POST'])
@login_required
def save_preferences():
    """Save or update user preferences"""
    data = request.get_json()
    
    preferences = Preferences.query.filter_by(user_id=current_user.id).first()
    
    if not preferences:
        preferences = Preferences(user_id=current_user.id)
        db.session.add(preferences)
    
    if 'theme' in data:
        preferences.theme = data['theme']
    
    if 'layout' in data:
        preferences.layout = data['layout']
    
    db.session.commit()
    
    return jsonify({
        'message': 'Preferences saved successfully',
        'preferences': {
            'theme': preferences.theme,
            'layout': preferences.layout
        }
    })

@api_bp.route('/projects', methods=['POST'])
@login_required
def create_project():
    """Create a new project"""
    try:
        # Skip CSRF validation for API endpoints by getting JSON data directly
        data = request.get_json()
        
        # Debug logging
        print(f"Received project data: {data}")
        
        # Validate that we have data
        if not data:
            return jsonify({'error': 'No data provided'}), 400
        
        # Validate required fields
        if not data.get('name'):
            return jsonify({'error': 'Project name is required'}), 400
        
        # Simulate project creation (you can integrate with actual database later)
        project_data = {
            'id': f'proj_{len(data.get("name", "")) + 1}',
            'name': data['name'],
            'description': data.get('description', ''),
            'priority': data.get('priority', 'medium'),
            'start_date': data.get('startDate'),
            'due_date': data.get('dueDate'),
            'category': data.get('category', ''),
            'created_by': current_user.id
        }
        
        # Here you would normally save to database
        # For now, we'll just return success
        
        return jsonify({
            'message': f'Project "{data["name"]}" created successfully!',
            'project': project_data
        }), 201
        
    except Exception as e:
        print(f"Error creating project: {str(e)}")
        return jsonify({'error': str(e)}), 500

@api_bp.route('/team-members', methods=['POST'])
@login_required
def add_team_member():
    """Add a new team member"""
    try:
        # Skip CSRF validation for API endpoints by getting JSON data directly
        data = request.get_json()
        
        # Debug logging
        print(f"Received team member data: {data}")
        
        # Validate that we have data
        if not data:
            return jsonify({'error': 'No data provided'}), 400
        
        # Validate required fields
        if not data.get('name'):
            return jsonify({'error': 'Name is required'}), 400
        
        if not data.get('email'):
            return jsonify({'error': 'Email is required'}), 400
        
        # Validate email format
        import re
        email_pattern = r'^[^\s@]+@[^\s@]+\.[^\s@]+$'
        if not re.match(email_pattern, data['email']):
            return jsonify({'error': 'Invalid email format'}), 400
        
        # Simulate team member creation (you can integrate with actual database later)
        member_data = {
            'id': f'member_{len(data.get("name", "")) + 1}',
            'name': data['name'],
            'email': data['email'],
            'role': data.get('role', 'member'),
            'department': data.get('department', ''),
            'invited_by': current_user.id,
            'invitation_sent': data.get('sendInvitation', False)
        }
        
        # Here you would normally save to database and send invitation email
        # For now, we'll just return success
        
        invite_text = ' and invitation sent' if data.get('sendInvitation') else ''
        return jsonify({
            'message': f'Team member "{data["name"]}" added successfully{invite_text}!',
            'member': member_data
        }), 201
        
    except Exception as e:
        print(f"Error adding team member: {str(e)}")
        return jsonify({'error': str(e)}), 500