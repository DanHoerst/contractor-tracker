import datetime
import mail
import reportSet

from dateutil.relativedelta import relativedelta



today = datetime.datetime.now()
nextMonth = today + relativedelta(months=1)

contractorFile = "/home/dan/PycharmProjects/ContractorTrack/contractors.txt"
expired = {}
expireNext = {}

## Necessary info for report to be emailed via SMTP
subj = "Subject of Email"
from_ = "From Email Address"
to_ = "To Email Address"
smtpServ = "Your SMTP Server"
## ## If your SMTP Server uses SSL, set sslTest to True and add login, pass
sslTest = False
#login_ = ""
#pass_ = ""


def track():
    _file = open(contractorFile)
    content = _file.readlines()

    ## Runs through each contractor in text file, separates name and date for comparison, sends email with summary
    for contractor in content:
        sepPoint = contractor.find(',')
        name = contractor[:sepPoint].strip(', \n')
        endDatePrep = contractor[sepPoint:].strip(', \n')
        endDate = datetime.datetime.strptime(endDatePrep, '%m/%d/%Y')
        if today >= endDate:
            expired[name] = endDate
        elif nextMonth >= endDate:
            expireNext[name] = endDate


    ## Setup email report
    report = "The following contracts have expired. Please remove the credentials for these contractors:\n\n"
    report += reportSet.setupReport(expired)
    report += "\n\n\nThe following contracts will expire before next months report. Please prepare to remove the credentials.\n\n"
    report += reportSet.setupReport(expireNext)

    ## Sends email
    mail.emailReport(subj, report, from_, to_, smtpServ, sslTest, login_='', pass_='')