# -*- coding:utf-8 -*-
"""This module help to send email for server."""

from threading import Thread
from email import charset
from flask_mail import Message
from flask import render_template
from flask import current_app    # 这样就不用使用from manager import app
from . import mail

charset.add_charset('utf-8', charset.SHORTEST, charset.BASE64, 'utf-8')

def send_async_mail(app, msg):
    """
    This function is a thread function. Each of these threads will send mail.
    """
    with app.app_context():
        mail.send(msg)


def send_mail(receiver, subject, template, **kw):
    app = current_app._get_current_object()
    msg = Message(subject=subject, sender=app.config[
        'FLASKY_MAIL_SENDER'], recipients=[receiver], charset='utf-8')
    msg.body = render_template(template + '.txt', **kw)
    msg.html = render_template(template + '.html', **kw)
    thr = Thread(target=send_async_mail, args=[app, msg])
    thr.start()
    return thr
