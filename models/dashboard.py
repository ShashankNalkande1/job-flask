from . import db

class DashboardSummary(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    team_count = db.Column(db.Integer, default=0)
    active_projects = db.Column(db.Integer, default=0)
    notifications = db.Column(db.Integer, default=0)
    
    def __repr__(self):
        return f'<DashboardSummary {self.team_count} team, {self.active_projects} projects>'
