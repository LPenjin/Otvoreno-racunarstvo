from otvoreno_racunarstvo import app, db
from flask import render_template, send_file
import codecs

statement = "select imeclan, prezimeclan, sifraplave, imanarancastu, pocasnoclanstvo, datrod, kandpoc, predpotstud, datumuclanjenja, clanstvovrijedido, ime, prostor, pocetaksastanka from clan natural join uclanjen_u natural join sekcija"

#statement_download =

def to_dict(clan):
   dict = {}
   dict["imeclan"] = clan._data[0]
   dict["prezimeclan"] = clan._data[1]
   dict["sifraplave"] = clan._data[2]
   dict["imanarancastu"] = clan._data[3]
   dict["pocasnoclanstvo"] = clan._data[4]
   dict["datrod"] = clan._data[5]
   dict["kandpoc"] = clan._data[6]
   dict["predpotstud"] = clan._data[7]
   dict["datumuclanjenja"] = clan._data[8]
   dict["clanstvovrijedido"] = clan._data[9]
   dict["ime"] = clan._data[10]
   dict["prostor"] = clan._data[11]
   dict["pocetaksastanka"] = clan._data[12]
   return dict

@app.route('/')
def index():
    return render_template('index.html', title="index")

@app.route('/download_csv')
def download():
    return send_file('../clanovi_sekcija.csv', as_attachment=True)

@app.route('/datatable')
def datatable():
    return render_template('datatable.html', title='datatable')

@app.route('/api/data')
def data():
    clanovi = db.engine.execute(statement)
    data = {"data": [to_dict(clan) for clan in clanovi]}
    return data

@app.route('/download_json')
def download_json():
    return send_file('../clanovi_sekcija.json')