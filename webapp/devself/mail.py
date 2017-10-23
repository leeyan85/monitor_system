def send_mail(subject, attachment='',content='', smtp_server='smtp.letv.cn', sender='SEE@le.com', receiver=['yangaofeng@le.com','leitao@le.com'], cc_receiver=[]):
    from email.mime.multipart import MIMEMultipart
    from email.mime.text import MIMEText
    from smtplib import SMTP as smtp
    all_receivers = receiver
    container = MIMEMultipart('alternative')
    container['Subject'] = subject
    container['From'] = sender
    container['To'] = ', '.join(receiver)
    container['CC'] = ', '.join(cc_receiver)
    container['Reply-to'] = 'SEE@le.com'
    content_plain = MIMEText(content)
    if attachment:
        att = MIMEText(open('%s'%attachment, 'rb').read(), 'base64', 'utf-8')
        att["Content-Type"] = 'application/octet-stream'
        att["Content-Disposition"] = 'attachment;filename="%s"'%attachment
        container.attach(att)
    container.attach(content_plain)

    smtp_conn = smtp(smtp_server)
    smtp_conn.sendmail(sender, all_receivers, container.as_string())
    smtp_conn.quit()


if __name__=='__main__':
    send_mail('test', sender='cm_monitor@le.com',receiver=['yangaofeng@le.com'], cc_receiver=['yangaofeng@le.com'])
