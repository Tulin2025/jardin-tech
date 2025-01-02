import os
from flask import Flask, request, jsonify, render_template_string, send_from_directory

app = Flask(__name__)

# Statik dosyalar için klasör ayarla
@app.route('/static/<path:filename>')
def static_files(filename):
    return send_from_directory(os.path.join(app.root_path, 'static'), filename)

# Sabit cevaplar
plant_info = {
    "orkide": "Orkide haftada bir sulanmalı, doğrudan güneş ışığından uzak tutulmalı.",
    "orkide neden çiçek açmıyor": "Orkideniz çiçek açmıyorsa daha fazla ışığa veya düzenli gübrelemeye ihtiyaç duyabilir.",
    "fesleğen": "Fesleğen sık sulanmalı, ancak drenajı iyi olan bir saksı kullanılmalı.",
    "kaktüs sulama": "Kaktüs az su sever, 2-3 haftada bir sulayın.",
    "kompost yapımı": "Organik atıklardan kompost üretmek için yeşil ve kahverengi malzemeleri karıştırın. Düzenli karıştırmayı unutmayın.",
    "doğal gübreler": "Kimyasal kullanmadan bahçenizi beslemek için hayvan gübresi, yumurta kabuğu ve kahve telvesi kullanabilirsiniz.",
    "yağmur suyu hasadı": "Yağmur suyunu bir varilde biriktirerek bahçenizi sulamak için kullanabilirsiniz.",
    "feng shui bahçe tasarımı": "Feng Shui bahçesi için yolları kıvrımlı yapın ve su elementi ekleyin.",
    "bahçe planlama": "Bahçenize uygun bitkiler seçin ve güneş ışığı alanlarını değerlendirin.",
    "toprak analizi": "Toprağın pH değerini ölçerek hangi bitkilerin uygun olduğunu belirleyebilirsiniz.",
    "mevsimsel öneriler": "Kışın soğuğa dayanıklı bitkiler ekin, yazın bol su isteyen bitkiler tercih edin.",
    "sebze ve meyve yetiştirme": "Küçük alanlarda domates, nane ve biber gibi sebzeler yetiştirebilirsiniz.",
    "ağaç dikme kampanyaları": "Yerel ağaç dikme etkinliklerine katılabilir veya kendi kampanyanızı başlatabilirsiniz.",
    "jarden tech nedir": "Jarden Tech, Jardin De Nini'nin bir alt kuruluşudur. Bitki bakımı, bahçe tasarımı ve doğal çözümler için teknolojik destek sağlar.",
    "jarden de nini nedir": "Jardin De Nini, doğaya ve sürdürülebilirliğe odaklanan bir peyzaj tasarım şirketidir."
}

# Chatbot Endpoint
@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.form.get("message").lower()
    reply = plant_info.get(user_message, "Bu konuda bilgim yok. Daha fazla detay verirseniz yardımcı olabilirim.")
    return f"<h1>Chatbot Cevabı:</h1><p>{reply}</p><a href='/'>Geri Dön</a>"

# Gelişmiş HTML Tasarım
HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>Jardin Chatbot</title>
    <style>
        body { font-family: Arial, sans-serif; background-color: #f9f9f9; color: #333; text-align: center; padding: 20px; }
        .container { background-color: #fff; border-radius: 8px; padding: 20px; box-shadow: 0 0 10px rgba(0,0,0,0.1); max-width: 400px; margin: auto; }
        input[type="text"] { width: 100%; padding: 10px; margin: 10px 0; border: 1px solid #ddd; border-radius: 4px; }
        button { background-color: #4CAF50; color: white; padding: 10px 15px; border: none; border-radius: 4px; cursor: pointer; }
        button:hover { background-color: #45a049; }
    </style>
</head>
<body>
    <img src="/static/jardin logo.jpeg" alt="Jardin Logo" width="150" height="150" />
    <h1>Jardin Chatbot’a Hoş Geldiniz!</h1>
    <form method="POST" action="/chat">
        <label for="message">Sorunuzu yazın:</label><br>
        <input type="text" id="message" name="message" required><br><br>
        <button type="submit">Gönder</button>
    </form>
</body>
</html>
"""

@app.route("/", methods=["GET"])
def index():
    return render_template_string(HTML_TEMPLATE)

if __name__ == "__main__":
    app.run(debug=True)
