#from otvoreno_racunarstvo import db
#from sqlalchemy import ForeignKey

class Clan:
    sifraplave = db.Column(db.String(5), unique=True, nullable=False)
    datumucljanjenja = db.Column(db.DateTime, nullable=False)
    pocasnoclanstvo = db.Column(db.Boolean, nullable=False)
    clanstvovrijedido = db.Column(db.DateTime, nullable=False)
    datrod = db.Column(db.DateTime, nullable=False)
    imeclan = db.Column(db.String(50), nullable=False)
    prezimeclan = db.Column(db.String(50), nullable=False)
    kandpoc = db.Column(db.Boolean, nullable=False)
    predpotstud = db.Column(db.Boolean, nullable=False)

    def __repr__(self):
        return f"{self.imeclan} {self.prezimeclan}, {self.sifraplave}"

class sekcija:
    ime = db.Column(db.String(20), nullable=False)
    pocetaksastanka = db.Column(db.String(5), nullable=False)
    prostor = db.Column(db.String(20), nullable=False)
    sef = ForeignKey("")

class jediouprave:
    pozicija = db.Column(db.String(20), nullable=False)

class uclanjen_u:
    sifraplave = db.Column(db.String(5), nullable=False)
    ime = db.Column(db.String(20))

class uprava:
    godina = db.Column(db.Integer, nullable=False)
    pocetaksastanka = db.Column(db.String(5), nullable=False)

