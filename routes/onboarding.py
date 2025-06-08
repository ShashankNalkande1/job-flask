from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from flask_login import login_required, current_user
from models.user import User
from models.business import BusinessInfo
from models.preferences import Preferences
from forms.onboarding import PersonalInfoForm, BusinessInfoForm, PreferencesForm
from models import db

onboarding_bp = Blueprint('onboarding', __name__)

@onboarding_bp.route('/start')
@login_required
def start():
    # If user already completed onboarding, redirect to dashboard
    if current_user.onboarding_completed:
        return redirect(url_for('dashboard.index'))
    
    # Initialize session data for onboarding
    session['onboarding_data'] = {}
    return redirect(url_for('onboarding.step1'))

@onboarding_bp.route('/step1', methods=['GET', 'POST'])
@login_required
def step1():
    if current_user.onboarding_completed:
        return redirect(url_for('dashboard.index'))
    
    form = PersonalInfoForm()
    
    # Pre-populate with existing user data
    if request.method == 'GET':
        form.name.data = current_user.name
        form.email.data = current_user.email
    
    if form.validate_on_submit():
        # Store data in session
        if 'onboarding_data' not in session:
            session['onboarding_data'] = {}
        
        session['onboarding_data']['name'] = form.name.data
        session['onboarding_data']['email'] = form.email.data
        session.modified = True
        
        return redirect(url_for('onboarding.step2'))
    
    return render_template('onboarding/step1.html', form=form, step=1)

@onboarding_bp.route('/step2', methods=['GET', 'POST'])
@login_required
def step2():
    if current_user.onboarding_completed:
        return redirect(url_for('dashboard.index'))
    
    # Check if step 1 data exists
    if 'onboarding_data' not in session:
        return redirect(url_for('onboarding.step1'))
    
    form = BusinessInfoForm()
    
    if form.validate_on_submit():
        session['onboarding_data']['company_name'] = form.company_name.data
        session['onboarding_data']['industry'] = form.industry.data
        session['onboarding_data']['size'] = form.size.data
        session.modified = True
        
        return redirect(url_for('onboarding.step3'))
    
    return render_template('onboarding/step2.html', form=form, step=2)

@onboarding_bp.route('/step3', methods=['GET', 'POST'])
@login_required
def step3():
    if current_user.onboarding_completed:
        return redirect(url_for('dashboard.index'))
    
    # Check if previous steps data exists
    if 'onboarding_data' not in session or 'company_name' not in session['onboarding_data']:
        return redirect(url_for('onboarding.step1'))
    
    form = PreferencesForm()
    
    if form.validate_on_submit():
        # Save all onboarding data to database
        onboarding_data = session['onboarding_data']
        
        # Update user info
        current_user.name = onboarding_data['name']
        current_user.email = onboarding_data['email']
        
        # Create business info
        business_info = BusinessInfo(
            user_id=current_user.id,
            company_name=onboarding_data['company_name'],
            industry=onboarding_data['industry'],
            size=onboarding_data['size']
        )
        
        # Create preferences
        preferences = Preferences(
            user_id=current_user.id,
            theme=form.theme.data,
            layout=form.layout.data
        )
        
        # Mark onboarding as completed
        current_user.onboarding_completed = True
        
        # Save to database
        db.session.add(business_info)
        db.session.add(preferences)
        db.session.commit()
        
        # Clear session data
        session.pop('onboarding_data', None)
        
        flash('Onboarding completed successfully!', 'success')
        return redirect(url_for('dashboard.index'))
    
    return render_template('onboarding/step3.html', form=form, step=3)

@onboarding_bp.route('/back/<int:step>')
@login_required
def back(step):
    if step == 2:
        return redirect(url_for('onboarding.step1'))
    elif step == 3:
        return redirect(url_for('onboarding.step2'))
    else:
        return redirect(url_for('onboarding.step1'))