from . import db

class Property(db.model):
    __tablename__='properties'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    bedroom_number = db.Column(db.Integer)
    location = db.Column(db.String(100))
    price = db.Column(db.String(100))
    type = db.Column(db.String(20))
    description = db.Column(db.String(500))
    photo = db.Column(db.String(100))

    def photo_path(self):
        if self.photo:
            return f'/static/uploads/{self.photo}'
        else:
            return None
        
    def get_id(self):
        try:
            return #unicode(self, id) #python 2 support
        except NameError:
            return str(self.id) #python 3 support
        
    def __repr__(self):
        return f'<Property {self.id} - {self.title}>'