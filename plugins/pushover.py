try:
	from pushover import init, Client
except:
	print("pushover missing\r\npip3 install python-pushover")
	raise SystemExit()


pushover_token = ""
pushover_key = ""

init(pushover_token)

def SendMessage(keyword, title, url):
	alert = "Alert for %s" % keyword
	Client(pushover_key).send_message(title=alert, url=url, message=title)