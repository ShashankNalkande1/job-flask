from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField
from wtforms.validators import DataRequired, Length

class PersonalInfoForm(FlaskForm):
    name = StringField('Full Name', validators=[DataRequired(), Length(min=2, max=100)])
    email = StringField('Email', validators=[DataRequired(), Length(max=120)])
    submit = SubmitField('Next')

class BusinessInfoForm(FlaskForm):
    company_name = StringField('Company Name', validators=[DataRequired(), Length(min=2, max=200)])
    industry = SelectField('Industry', choices=[
        ('technology', 'Technology'),
        ('healthcare', 'Healthcare'),
        ('finance', 'Finance'),
        ('education', 'Education'),
        ('retail', 'Retail'),
        ('manufacturing', 'Manufacturing'),
        ('consulting', 'Consulting'),
        ('other', 'Other')
    ], validators=[DataRequired()])
    size = SelectField('Company Size', choices=[
        ('1-10', '1-10 employees'),
        ('11-50', '11-50 employees'),
        ('51-200', '51-200 employees'),
        ('201-500', '201-500 employees'),
        ('501+', '501+ employees')
    ], validators=[DataRequired()])
    submit = SubmitField('Next')

class PreferencesForm(FlaskForm):
    theme = SelectField('Theme', choices=[
        ('light', 'Light'),
        ('dark', 'Dark')
    ], validators=[DataRequired()])
    layout = SelectField('Dashboard Layout', choices=[
        ('default', 'Default'),
        ('compact', 'Compact'),
        ('expanded', 'Expanded')
    ], validators=[DataRequired()])
    submit = SubmitField('Complete Onboarding')
