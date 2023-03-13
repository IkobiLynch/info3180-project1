from . import db
from werkzeug.security import generate_password_hash

class Property(db.Model):
    __tablename__='property'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    bedroom_number = db.Column(db.Integer)
    location = db.Column(db.String(100))
    price = db.Column(db.String(100))
    type = db.Column(db.String(20))
    description = db.Column(db.String(500))
    photo = db.Column(db.String(100))

    def __init__(self, title, bedroom_number, location, price, type, description, photo):
        self.title = title
        self.bedroom_number = bedroom_number
        self.location = location
        self.price =   price
        self.type = type
        self.description = description
        self.photo = photo

    def photo_path(self):
        if self.photo:
            return f'/static/uploads/{self.photo}'
        else:
            return None
        
    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        try:
            return #unicode(self, id) #python 2 support
        except NameError:
            return str(self.id) #python 3 support
        
    def __repr__(self):
        return f'<Property {self.id} - {self.title}>'