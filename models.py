from database import db


class User(db.Model):
    __tablename__ = 'users_table'


    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)


    def __repr__(self):
        return f'<User {self.name}>'
    
    def to_dict(self):
        return {"id": self.id, "name": self.name}
