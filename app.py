from flask import Flask, render_template_string, abort
import json
import os

app = Flask(__name__)

# Veriyi JSON dosyasından al
with open("veritabani.json", "r", encoding="utf-8") as f:
    plakalar = json.load(f)

TEMPLATE = """
<!DOCTYPE html>
<html lang="tr">
<head>
    <meta charset="UTF-8">
    <title>Plaka Bilgisi</title>
    <style>
        body { font-family: Arial; margin: 40px; }
        h1 { color: #333; }
        .kutu { border: 1px solid #aaa; padding: 15px; border-radius: 10px; max-width: 400px; }
    </style>
</head>
<body>
    <h1>Plaka Bilgisi</h1>
    <div class="kutu">
        <p><strong>Heat No:</strong> {{ plaka["heat_no"] }}</p>
        <p><strong>Kalınlık:</strong> {{ plaka["kalinlik"] }}</p>
        <p><strong>Cinsi:</strong> {{ plaka["cins"] }}</p>
        <p><strong>Proje:</strong> {{ plaka["proje"] }}</p>
        <p><strong>Boyutlar:</strong> {{ plaka["boyutlar"] }}</p>
        <p><strong>Durum:</strong> {{ "Geldi" if plaka["geldi"] else "Gelmedi" }}</p>
    </div>
</body>
</html>
"""

@app.route("/plaka/<heat_no>")
def plaka_goster(heat_no):
    for p in plakalar:
        if p["heat_no"] == heat_no:
            return render_template_string(TEMPLATE, plaka=p)
    return abort(404)

# Render.com için gerekli: PORT üzerinden çalış
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)

