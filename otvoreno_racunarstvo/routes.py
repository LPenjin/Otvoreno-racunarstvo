from otvoreno_racunarstvo import app, db
from flask import render_template, send_file, jsonify, request, make_response, json
import os

statement = "select imeclan, prezimeclan, sifraplave, imanarancastu, pocasnoclanstvo, datrod, kandpoc, predpotstud, datumuclanjenja, clanstvovrijedido, ime, prostor, pocetaksastanka from clan natural join uclanjen_u natural join sekcija"

statement_id = statement + " where sifraplave = \'"

statement_post = "insert into clan(datumuclanjenja, sifraplave, imanarancastu, pocasnoclanstvo, clanstvovrijedido, datrod, imeclan, prezimeclan, kandpoc, predpotstud) values "

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
   dict["ime_sekcije"] = clan._data[10]
   dict["prostor"] = clan._data[11]
   dict["pocetaksastanka"] = clan._data[12]
   return dict

def to_dict_sekcija(sekcija):
    dict = {}
    dict["ime_sekcije"] = sekcija._data[0]
    dict["pocetak_sastanka"] = sekcija._data[1]
    dict["prostor"] = sekcija._data[2]
    dict["sef_sekcije"] = sekcija._data[3]
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

@app.route('/clan/get', methods=['GET'])
def get_clanovi():
    clanovi = db.engine.execute(statement)
    data = {"data": [to_dict(clan) for clan in clanovi]}
    return jsonify(data), 200

@app.route('/clan/getById', methods=['GET'])
def get_clanovi_po_plavoj():
    args = request.args
    if id:=args.get('id'):
        clanovi = db.engine.execute(statement_id + id + "\'")
        data = {"data": [to_dict(clan) for clan in clanovi]}
        if not data:
            return jsonify({"error": "Clan not found"}), 404
        return jsonify(data), 200
    else:
        return jsonify({"error" : "Invalid Sifra Plave"}), 400

@app.route('/sekcija/get', methods=['GET'])
def get_sekcije():
    sekcije = db.engine.execute("select * from sekcija")
    data = {"data": [to_dict_sekcija(sekcija) for sekcija in sekcije]}
    return jsonify(data), 200

@app.route('/clan/getSef', methods=['GET'])
def get_sefovi():
    sefovi = db.engine.execute(statement + " where sifraplave = sekcija.sef")
    data = {"data": [to_dict(sef) for sef in sefovi]}
    return jsonify(data), 200

@app.route('/sekcija/getByProstor', methods=['GET'])
def get_sekcije_by_prostor():
    args = request.args
    if prostor := args.get('prostor'):
        sekcije = db.engine.execute(f"select * from sekcija where prostor like '{prostor}'")
        data = {"data": [to_dict_sekcija(sekcija) for sekcija in sekcije]}
        if not data:
            return jsonify({"error": "Clan not found"}), 404
        return jsonify(data), 200
    else:
        return jsonify({"error": "Prostor no supplied"}), 400

@app.route('/openapi/get', methods=['GET'])
def get_openapi():
    root = os.path.realpath(os.path.dirname(__file__))
    json_url = os.path.join(root, "static", "openAPI.json")
    print(json_url)
    data = json.load(open(r'C:\Users\lpenj\Desktop\Very important stuff\Fakultetlaz\7. semestar\Otvoreno racunarstvo\Otvoreno-racunarstvo\otvoreno_racunarstvo\openapi.json'))
    return make_response(data, 200)

@app.route('/clan/post', methods=['POST'])
def post_clan():
    datumuclanjenja = request.form['datumuclanjenja']
    sifraplave = request.form['sifraplave']
    imanarancastu = request.form['imanarancastu']
    pocasnoclanstvo = request.form['pocasnoclanstvo']
    clanstvovrijedido = request.form['clanstvovrijedido']
    datrod = request.form['datrod']
    imeclan = request.form['imeclan']
    prezimeclan = request.form['prezimeclan']
    kandpoc = request.form['kandpoc']
    predpotstud = request.form['predpotstud']
    db.engine.execute(statement_post + f"(\'{datumuclanjenja}\', \'{sifraplave}\', {imanarancastu}, {pocasnoclanstvo}, "
                                       f"\'{clanstvovrijedido}\', \'{datrod}\', \'{imeclan}\', \'{prezimeclan}\', "
                                       f"{kandpoc}, {predpotstud})")
    return make_response("Success", 200)


@app.route('/clan/put', methods=['PUT'])
def update_clan():
    datumuclanjenja = request.form['datumuclanjenja']
    sifraplave = request.form['sifraplave']
    imanarancastu = request.form['imanarancastu']
    pocasnoclanstvo = request.form['pocasnoclanstvo']
    clanstvovrijedido = request.form['clanstvovrijedido']
    datrod = request.form['datrod']
    imeclan = request.form['imeclan']
    prezimeclan = request.form['prezimeclan']
    kandpoc = request.form['kandpoc']
    predpotstud = request.form['predpotstud']
    db.engine.execute("update clan set " + f"datumuclanjenja = \'{datumuclanjenja}\', imanarancastu={imanarancastu}, "
                                      f"pocasnoclanstvo={pocasnoclanstvo}, clanstvovrijedido=\'{clanstvovrijedido}\', "
                                        f"datrod=\'{datrod}\', imeclan=\'{imeclan}\', prezimeclan=\'{prezimeclan}\', "
                                      f"kandpoc={kandpoc}, predpotstud={predpotstud} "
                                      f"where sifraplave like \'{sifraplave}\'")
    return make_response("Success", 200)


@app.route('/clan/delete', methods=['DELETE'])
def delete_clan():
    sifraplave = request.form['sifraplave']
    db.engine.execute(f"delete from clan where sifraplave=\'{sifraplave}\'")
    return make_response("Success", 200)

