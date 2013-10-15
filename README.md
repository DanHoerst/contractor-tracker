contractor-tracker
==================

This is a tool that can be ran monthly/weekly as a service or scheduled task. 
It is used to keep track of contractors and their end dates in order to revoke their security/email/etc access in a timely manner. 
An email is sent each time the program runs containing a report of the contractors whose end dates have passed as well as the contractors whose end dates are in the next month.

To run the program, run ~/contractor-tracker/main.py after filling out your configuration settings in the config.py
