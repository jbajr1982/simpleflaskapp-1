from flask import Flask, render_template, request
from sqlite3 import connect
from pandas import read_sql_query

app = Flask(__name__)

@app.route('/', methods = ['POST', 'GET'])

def gfg():
    con = connect("database.db")
    cur = con.cursor()
    dt_av = read_sql_query("SELECT * FROM parametros", con).iloc[0,1]
    if request.method == 'POST':
        dt_av = request.form['ht_dtav']
        cur.execute(f"UPDATE parametros SET DT_AVAL = '{dt_av}' WHERE NR = 1" )
        con.commit()
        return render_template("home.html", dt_av = dt_av )    
    return render_template("home.html", dt_av = dt_av)    

@app.route('/', methods = ['POST', 'GET'])

def f_salv():
    ht_dtav = request.form['ht_dtav']
    return render_template("home.html", ht_dtav = ht_dtav)    

if __name__ == '__main__':
   app.run(debug = True)
