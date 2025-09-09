from flask import Flask
from coba1 import coba1_bp
from coba2 import coba2_bp
import os

app = Flask(__name__)

# daftar blueprint
app.register_blueprint(coba1_bp, url_prefix="/coba1")
app.register_blueprint(coba2_bp, url_prefix="/coba2")

# route untuk serve static CSS
@app.route('/src/<path:filename>')
def src(filename):
    return app.send_static_file(filename)

if __name__ == "__main__":
    # agar file style.css bisa dipakai
    app.static_folder = os.path.join(os.path.dirname(__file__), "src")
    app.run(debug=True)
