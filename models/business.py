from . import db

class BusinessInfo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    company_name = db.Column(db.String(200), nullable=False)
    industry = db.Column(db.String(100), nullable=False)
    size = db.Column(db.String(50), nullable=False)
    
    def __repr__(self):
        return f'<BusinessInfo {self.company_name}>'
