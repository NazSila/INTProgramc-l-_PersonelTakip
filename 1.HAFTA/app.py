from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def login():
    return render_template('login.html')

@app.route('/kayit')
def kayit():
    return render_template('kayit.html')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@app.route('/personel')
def personel():
    return render_template('personel.html')

@app.route('/personel/ekle')
def personel_ekle():
    return render_template('personel_ekle.html')

@app.route('/personel/duzenle/<int:id>')
def personel_duzenle(id):
    return render_template('personel_duzenle.html')

@app.route('/personel/giris-cikis')
def personel_giris_cikis():
    return render_template('personel_giris_cikis.html')

@app.route('/raporlar')
def raporlar():
    return render_template('raporlar.html')

if __name__ == '__main__':
    app.run(debug=True) 