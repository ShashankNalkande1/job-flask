from . import db

class Preferences(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    theme = db.Column(db.String(20), default='light')
    layout = db.Column(db.String(20), default='default')
    
    def __repr__(self):
        return f'<Preferences {self.theme}, {self.layout}>'
