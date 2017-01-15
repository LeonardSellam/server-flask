from sqlalchemy import Column, Integer, String
from Appster.database import Base, db_session
from sqlalchemy import or_

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True)
    email = Column(String(120), unique=True)

    def __init__(self, name=None, email=None):
        self.name = name
        self.email = email

    def __repr__(self):
        return '<User %r>' % (self.name)

    def finOneByName(name):
        return User.query.filter(User.name == name).first()

    def findOneByEmail(email):
        return User.query.filter(User.name == email).first()

    def userAlreadyExist(name, email):
        candidates = User.query.filter(or_(User.name == name, User.email == email)).all();
        return len(candidates) > 0;

    def createNewUser(name, email):
        if(User.userAlreadyExist(name, email)):
            return {'info' : "User Already Exists"}
        else:
            u = User(name, email)
            db_session.add(u)
            db_session.commit()
            return {'info' : "New User Created"};
