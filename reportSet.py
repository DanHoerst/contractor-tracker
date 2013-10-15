## Iterates dictionary returned after analyzing text file. Adds names and dates in list to report

def setupReport(dict_):
    report = ""
    for cname, cvalue in dict_.iteritems():
        report += "%s, %s" % (cname, cvalue)
        return report
