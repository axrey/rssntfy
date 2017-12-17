import smtplib

# Untested code - I don't use email function
#
# Fill out below before use

gmail_user = "user"
gmail_pwd =  "password"
FROM = "from@gmail.com"
TO = "to@gmail.com"

def SendMessage(keyword, title, url):
	server_ssl = smtplib.SMTP_SSL("smtp.gmail.com", 465)
	server_ssl.login(gmail_user, gmail_pwd)
	SUBJECT = "Alert for %s" % keyword
	TEXT = "<a href='%s'>%s</a>" % (url, title)
	message = """From: %s\nTo: %s\nSubject: %s\n\n%s
	""" % (FROM, ", ".join(TO), SUBJECT, TEXT)
	server_ssl.sendmail(FROM, TO, message)
	server_ssl.close()