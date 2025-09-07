from flask import Flask, render_template_string, url_for, send_from_directory, request
import os

app = Flask(__name__)

@app.route('/src/<path:filename>')
def src(filename):
    return send_from_directory(os.path.join(app.root_path, 'src'), filename)

users = [
    {"id": 1, "nama": "Andi", "email": "andi@mail.com"},
    {"id": 2, "nama": "Siti", "email": "siti@mail.com"},
]

@app.route('/')
def home():
    html = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Contoh Web Dev Python</title>
        <link rel="stylesheet" href="{url_for('src', filename='style.css')}">
    </head>
    <body>
    <div class="container">
        <h2>Selamat Datang di Web Dev Python</h2>
        <p>Ini adalah contoh aplikasi web sederhana menggunakan Flask.</p>
        <nav style="margin-bottom:20px;">
            <a href="/">Home</a> | 
            <a href="/users">Daftar User</a> | 
            <a href="/tambah">Tambah User</a> | 
            <a href="/src/coba1"><button style="padding:8px 20px;">Ke Materi Dasar (coba1.py)</button></a>
        </nav>
        <div class="section">
            <b>Fitur:</b>
            <ul>
                <li>Menampilkan halaman utama</li>
                <li>Menampilkan daftar user</li>
                <li>Menambah user baru</li>
            </ul>
        </div>
    </div>
    </body>
    </html>
    """
    return render_template_string(html)

@app.route('/users')
def daftar_user():
    user_list = ""
    for user in users:
        user_list += f"<tr><td>{user['id']}</td><td>{user['nama']}</td><td>{user['email']}</td></tr>"
    html = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Daftar User</title>
        <link rel="stylesheet" href="{url_for('src', filename='style.css')}">
    </head>
    <body>
    <div class="container">
        <h2>Daftar User</h2>
        <nav style="margin-bottom:20px;">
            <a href="/">Home</a> | 
            <a href="/users">Daftar User</a> | 
            <a href="/tambah">Tambah User</a> | 
            <a href="/src/coba1"><button style="padding:8px 20px;">Ke Materi Dasar (coba1.py)</button></a>
        </nav>
        <table border="1" cellpadding="8" style="width:100%;background:#fff;">
            <tr style="background:#eee;"><th>ID</th><th>Nama</th><th>Email</th></tr>
            {user_list}
        </table>
    </div>
    </body>
    </html>
    """
    return render_template_string(html)

@app.route('/tambah', methods=['GET', 'POST'])
def tambah_user():
    pesan = ""
    if request.method == 'POST':
        nama = request.form.get('nama')
        email = request.form.get('email')
        if nama and email:
            users.append({"id": len(users)+1, "nama": nama, "email": email})
            pesan = "User berhasil ditambahkan!"
        else:
            pesan = "Nama dan email harus diisi!"
    html = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Tambah User</title>
        <link rel="stylesheet" href="{url_for('src', filename='style.css')}">
    </head>
    <body>
    <div class="container">
        <h2>Tambah User Baru</h2>
        <nav style="margin-bottom:20px;">
            <a href="/">Home</a> | 
            <a href="/users">Daftar User</a> | 
            <a href="/tambah">Tambah User</a> | 
            <a href="/src/coba1"><button style="padding:8px 20px;">Ke Materi Dasar (coba1.py)</button></a>
        </nav>
        <form method="post">
            <div class="section">
                <label>Nama:</label><br>
                <input type="text" name="nama" style="width:100%;padding:8px;"><br><br>
                <label>Email:</label><br>
                <input type="email" name="email" style="width:100%;padding:8px;"><br><br>
                <button type="submit" style="padding:8px 16px;">Tambah</button>
            </div>
        </form>
        <div class="section" style="color:green;">{pesan}</div>
    </div>
    </body>
    </html>
    """
    return render_template_string(html)

# Route untuk pindah ke coba1.py
@app.route('/src/coba1')
def goto_coba1():
    return """
    <script>
        window.location.href = 'http://localhost:5000/';
    </script>
    """

if __name__ == '__main__':
    app.run()