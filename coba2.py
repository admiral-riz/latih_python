from flask import Blueprint, render_template_string, url_for, request

coba2_bp = Blueprint("coba2", __name__)

# gunakan nama berbeda agar tidak bentrok dengan fungsi
users_data = [
    {"id": 1, "nama": "Andi", "email": "andi@mail.com"},
    {"id": 2, "nama": "Siti", "email": "siti@mail.com"},
]

@coba2_bp.route("/")
def home():
    html = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Coba2 - Web Dev</title>
        <link rel="stylesheet" href="/src/style.css">
    </head>
    <body>
        <div class="container">
        <h2>Selamat Datang di Web Dev Python</h2>
        <p>Contoh aplikasi Flask sederhana.</p>
        <nav style="margin-bottom:20px;">
            <a href="{url_for('coba1.home')}"><button>Ke Materi Dasar (coba1.py)</button></a>
            <a href="{url_for('coba2.daftar_user')}"><button>Lihat User</button></a>
            <a href="{url_for('coba2.tambah_user')}"><button>Tambah User</button></a>
        </nav>
        </div>
    </body>
    </html>
    """
    return render_template_string(html)

@coba2_bp.route("/users")
def daftar_user():
    rows = "".join(
        f"<tr><td>{u['id']}</td><td>{u['nama']}</td><td>{u['email']}</td></tr>"
        for u in users_data
    )
    html = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Daftar User</title>
        <link rel="stylesheet" href="/src/style.css">
    </head>
    <body>
        <div class="container">
        <h2>Daftar User</h2>
        <table border="1" cellpadding="5" style="width:100%;background:#fff;">
            <tr style="background:#eee;"><th>ID</th><th>Nama</th><th>Email</th></tr>
            {rows}
        </table>
        <br><a href="{url_for('coba2.home')}">Kembali</a>
        </div>
    </body>
    </html>
    """
    return render_template_string(html)

@coba2_bp.route("/tambah", methods=["GET", "POST"])
def tambah_user():
    pesan = ""
    if request.method == "POST":
        nama = request.form.get("nama")
        email = request.form.get("email")
        if nama and email:
            users_data.append({"id": len(users_data)+1, "nama": nama, "email": email})
            pesan = "User berhasil ditambahkan!"
        else:
            pesan = "Nama dan email harus diisi!"
    html = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Tambah User</title>
        <link rel="stylesheet" href="/src/style.css">
    </head>
    <body>
        <div class="container">
        <h2>Tambah User</h2>
        <form method="post">
            <label>Nama:</label><br>
            <input type="text" name="nama" style="width:100%;padding:8px;"><br><br>
            <label>Email:</label><br>
            <input type="email" name="email" style="width:100%;padding:8px;"><br><br>
            <button type="submit" style="padding:8px 16px;">Tambah</button>
        </form>
        <p style="color:green;">{pesan}</p>
        <a href="{url_for('coba2.home')}">Kembali</a>
        </div>
    </body>
    </html>
    """
    return render_template_string(html)
