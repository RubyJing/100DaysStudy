from smtplib import SMTP
from email.header import Header
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart

import urllib


def main():
    # 创建一个带附件的邮件消息对象
    message = MIMEMultipart()

    # 创建文本内容
    text_content = MIMEText('附件中有本月数据请查收', 'plain', 'utf-8')
    message['Subject'] = Header('本月数据', 'utf-8')
    # 将文本内容添加到邮件消息对象中
    message.attach(text_content)

    # 读取文件并将文件作为附件添加到邮件消息对象中
    with open('介绍.txt', 'rb') as f:
        txt = MIMEText(f.read(), 'base64', 'utf-8')
        txt["Content-Type"] = 'text/plain'
        # txt["Content-Disposition"] = 'attachment; filename=introduction.txt'
        # 文件名为中文时
        txt.add_header("Content-Disposition", "attachment", filename=("gbk", "", "介绍.txt"))
        message.attach(txt)

    # 创建SMTP对象
    smtper = SMTP('smtp.qq.com')
    # 开启安全连接
    smtper.starttls()
    sender = 'xx@qq.com'
    receivers = ['zhoujing@lii.com.cn']
    # 登录到SMTP服务器
    smtper.login(sender, '')
    # 发送邮件
    smtper.sendmail(sender, receivers, message.as_string())
    # 与邮件服务器断开连接
    smtper.quit()
    print('发送完成')


if __name__ == '__main__':
    main()
