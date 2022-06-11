import hashlib
import functools
from flask import Flask, render_template, request, session, flash, url_for, redirect, g
from flask_bootstrap import Bootstrap
from flask_mysqldb import MySQL
import os

app = Flask(__name__, static_folder='staticsFiles')
Bootstrap(app)

app.config['MYSQL_HOST'] = 'localhost'  # Lokasi server database yang digunakan
app.config['MYSQL_USER'] = 'root'  # Username dari akun pengguna database
app.config['MYSQL_PASSWORD'] = ''  # Password dari akun pengguna database
app.config['MYSQL_DB'] = 'hotel_uyu'  # Database yang digunakan
app.config['MYSQL_CURSORCLASS'] = "DictCursor"

mysql = MySQL(app)

app.config['SECRET_KEY'] = os.urandom(24)

@app.route('/api/jenis/<no>',methods=['GET'])
def getJenis(no):
    try:
        cur = mysql.connection.cursor()
        sql = "SELECT jenis_kamar FROM kamar WHERE no_kamar={}".format(no)
        result = cur.execute(sql)
        data = cur.fetchone()
        return render_template('jenis.html',jenis=data)
    except:
        return render_template('jenis.html',jenis="None")

@app.route('/pesanan', methods=['GET', 'POST'])
def pesanan():
    uid = session.get('uid')
    if uid is None:
        g.user = None
        return redirect(url_for('login'))
    elif request.method == 'POST':
        data = None
        try:
            form = request.form
            searchKey = form['in_searchKey']
            cur = mysql.connection.cursor()
            sql = "SELECT id_reservasi,admin.username,kamar.jenis_kamar,kamar.no_kamar,nama_pemesan,tanggal_pemesanan FROM reservasi INNER JOIN admin ON reservasi.id_admin=admin.id_admin INNER JOIN kamar ON kamar.no_kamar=reservasi.id_kamar WHERE tanggal_pemesanan=\'{}\'".format(
                searchKey)
            result = cur.execute(sql)
            data = cur.fetchall()
        except Exception as e:
            flash(e, "danger")
        return render_template('pesanan.html', datas=data)
    else:
        data = None
        try:
            cur = mysql.connection.cursor()
            result = cur.execute(
                "SELECT id_reservasi,admin.username,kamar.jenis_kamar,kamar.no_kamar,nama_pemesan,tanggal_pemesanan FROM reservasi INNER JOIN admin ON reservasi.id_admin=admin.id_admin INNER JOIN kamar ON kamar.no_kamar=reservasi.id_kamar")
            data = cur.fetchall()
        except Exception as e:
            flash(e, "danger")
        return render_template('pesanan.html', datas=data)


@app.route('/add-pesanan', methods=['GET', 'POST'])
def add():
    uid = session.get('uid')
    if uid is None:
        g.user = None
        return redirect(url_for('login'))
    elif request.method == 'POST':
        error = None
        try:
            form = request.form
            nama_pemesan = form['in_nama_pemesan']
            tgl_pemesanan = form['in_tgl_pemesanan']
            no_kamar = form['in_no_kamar']
            cur = mysql.connection.cursor()
            sql = "INSERT INTO reservasi(id_admin, id_kamar, tanggal_pemesanan, nama_pemesan) VALUES({},{},\'{}\',\"{}\")".format(
                uid, no_kamar, tgl_pemesanan, nama_pemesan)
            cur.execute(sql)
            mysql.connection.commit()
            flash("Successfully inserted data", "success")
        except Exception as e:
            flash(e, "danger")
    return render_template('add-pesanan.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    uid = session.get('uid')
    if uid is not None:
        g.user = None
        return redirect(url_for('pesanan'))
    if request.method == 'POST':
        error = None
        form = request.form
        username = form['in_username']
        pwd = hashlib.md5(form['in_password'].encode('utf-8'))
        cur = mysql.connection.cursor()
        sql = "SELECT * FROM admin WHERE username = \"{}\"".format(
            username)
        cur.execute(sql)
        user = cur.fetchone()
        if user is None:
            error = "Username tidak ada"
        elif not user["kata_sandi"] == pwd.hexdigest():
            error = "Password salah"

        if error is None:
            session.clear()
            session['uid'] = user['id_admin']
            session['username'] = user['username']
            return redirect(url_for('index'))
        else:
            flash(error)

    return render_template('auth-base.html')


@app.route('/', methods=['GET', 'POST'])
def index():
    uid = session.get('uid')
    if uid is None:
        g.user = None
        return redirect(url_for('login'))
    else:
        return redirect(url_for('pesanan'))


@app.route('/logout', methods=['GET'])
def logout():
    uid = session.get('uid')
    if uid is None:
        g.user = None
        return redirect(url_for('login'))
    session.clear()
    return redirect(url_for('index'))


@app.errorhandler(404)
def page_not_found(e):
    return 'This page was not found'
