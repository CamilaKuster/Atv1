from app import db
from app import db


class Cliente(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String)
    name = db.Column(db.String)
    email = db.Column(db.String(300), unique=True, nullable=False) 
    cpf = db.Column(db.Integer, unique=True, nullable=False)
    data_nasc = db.Column(db.Date, unique=True, nullable=False)
    rg = db.Column(db.Integer, unique=True, nullable=False)
    celular = db.Column(db.Integer, unique=True, nullable=False)
    endereco = db.Column(db.Text, unique=True, nullable=False)

    def __init__(self,username,password,name,email,cpf,data_nasc,rg,celular,endereco):
        self.username = username
        self.password = password
        self.name = name
       
    
    def __repr__(self):
        return "<User %r>" % self.username

db.create_all()
db.session.commit()

admin = Cliente(username='admin',password='123',name='camz',email='camilaa',cpf=123,data_nasc=6/5/2002,rg=1233,celular=9643981,endereco="kfekfjgnqaeg")
db.session.add(admin)
db.session.commit()
users = Cliente.query.all()
     