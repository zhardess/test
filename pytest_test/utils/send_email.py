import smtplib
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.audio import MIMEAudio
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from email.header import Header

sender = 'xxx@qq.com'
receivers = ['xxx@163.com', 'xxx@qq.com']
message = MIMEMultipart()
message['From'] = Header("a xxx@qq.com")
message['To'] =  Header("111", 'utf-8')
message['Subject'] = Header('带附件的邮件测试', 'utf-8')
message.attach(MIMEText('这是用Python编写的邮件发送程序……', 'plain', 'utf-8'))
att1=MIMEApplication(open('/home/lixiang/notes/test/pytest_test/ops_test_report/2023-08-22_16:42:38/add_report.html','rb').read())
att1["Content-Type"]='application/octet-stream'
att1.add_header('content-disposition', 'attachment', filename='add_report.html')
message.attach(att1)
att2=MIMEApplication(open('/home/lixiang/notes/test/pytest_test/ops_test_report/2023-08-22_16:42:38/pow_report.html','rb').read())
att2["Content-Type"]='application/octet-stream'
att2.add_header('content-disposition', 'attachment', filename='pow_report.html')
message.attach(att2)
smtp = smtplib.SMTP()
smtp.connect('smtp.qq.com')
smtp.login('xxx@qq.com', 'xxx')
smtp.sendmail(sender, receivers, message.as_string())
print ("邮件发送成功！！！")
smtp.quit()
