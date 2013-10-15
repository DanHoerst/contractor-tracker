import smtplib

def emailReport(subj, report, from_, to_, smtpServ, sslTest, login_='', pass_='', ):
    msg = {}
    msg['To'] = to_
    msg['From'] = from_
    msg['Subject'] = subj
    msg[''] = report

    s = smtplib.SMTP(smtpServ)
    if sslTest == True:
        s.login(login_, pass_)
    s.sendmail(from_, [to_], msg.as_string())
    s.quit()