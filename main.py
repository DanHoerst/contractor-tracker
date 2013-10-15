import datetime
import mail
import reportSet
import config

from dateutil.relativedelta import relativedelta

today = datetime.datetime.now()
nextMonth = today + relativedelta(months=1)
expired = {}
expireNext = {}

def track():
    _file = open(config.contractorFile)
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
    mail.emailReport(config.subj, report, config.from_, config.to_, config.smtpServ, config.sslTest, config.login_, config.pass_)

track()