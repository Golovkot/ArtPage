from flask import Flask, render_template, request, jsonify
from flask.ext.mail import Mail
from threading import Thread
from flask.ext.mail import Message
from config import MAIL_USERNAME, SEND_TO

# -*- coding: utf-8 -*-
DEFAULT_PORT = 5000
ADDITIVE_FOR_UID = 1000

try:
    from os import getuid

except ImportError:
    def getuid():
        return DEFAULT_PORT - ADDITIVE_FOR_UID


def send_async_email(msg):
    with app.app_context():
        mail.send(msg)


def send_email(subject, sender, recipients, text_body):
    msg = Message(subject, sender=sender, recipients=[recipients])
    msg.body = text_body
    mail.send(msg)
    thr = Thread(target=send_async_email, args=[msg])
    thr.start()


def send_comment(name, email, comments):
    subject = 'ArtPage Feedback'
    recipients = SEND_TO
    text_body = "sender: "+str(name)+"\n e-mail: "+str(email)+"\n Message: "+str(comments)
    send_email(subject, MAIL_USERNAME, recipients, text_body)


mail = Mail()
app = Flask(__name__)

try:
    app.config.from_object('config')
except FileNotFoundError:
    print('Отсутствует файл конфигурации')
mail.init_app(app)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/Feedback', methods=['POST'])
def feedback():
    name = request.form.get('name')
    email = request.form.get('email')
    comments = request.form.get('comments')
    send_comment(name, email, comments)

    return jsonify({'status': 'OK'})

if __name__ == '__main__':
    app.run(port=getuid() + ADDITIVE_FOR_UID, debug=True)
