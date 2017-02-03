from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    uname = db.Column(db.String(20), unique=True)
    upass = db.Column(db.String(20))
    roll_no = db.Column(db.String(20), unique=True)

    def __init__(self, id_, uname, upass, roll_no):
        self.id = id_
        self.uname = uname
        self.upass = upass
        self.roll_no = roll_no

    def __repr__(self):
        return ('<User {}>'.format(self.name))

class Posts(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    post_text = db.Column(db.String(220))
    user_id =  db.Column(db.Integer, db.ForeignKey('user.id'))
    


if __name__=='__main__':
    db.create_all()

