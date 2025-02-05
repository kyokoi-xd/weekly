from database import db


class User(db.Model):
    __tablename__ = 'users_table'


    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)


    def __repr__(self):
<<<<<<< HEAD
        return f'<User {self.name}>'
    
    def to_dict(self):
        return {"id": self.id, "name": self.name}
=======
        return f'<User {self.name}>'
>>>>>>> 0cd55705017f3957d85537e17e07e3d3a0c9f602
