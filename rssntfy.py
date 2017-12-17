#!/usr/bin/python3
import os, time, importlib
try:
	import feedparser
except:
	print("feedparser missing\r\npip3 install feedparser")
	raise SystemExit()


# settings
timer = 300 # 5 minutes
notify = True
plugin = "pushover"
daily = False
hour = "09"


today = time.strftime("%d")
daily_finds = []
daily_sent = False


if os.path.isfile("feeds.txt"):
	feeds = filter(None, open("feeds.txt", "r").read().splitlines())
else:
	print("Failed to read in feeds.txt")
	raise SystemExit()

if os.path.isfile("keywords.txt"):
	keywords = filter(None, open("keywords.txt", "r").read().splitlines())
else:
	print("Failed to read in keywords.txt")
	raise SystemExit()

if not os.path.exists("findings"):
	os.mkdir("findings")

if notify:
	try:
		module = "plugins.%s" % plugin
		ntfy = importlib.import_module(module)
	except:
		print("Failed to load plugin %s" % plugin)
		raise SystemExit()


def do_ntfy(keyword, title, url):
	if daily:
		# add keyword,url to daily_finds
		# check if sent
		# blah
		print("daily")
	else:
		ntfy.SendMessage(keyword, title, url)

def check_finding(keyword, title, url):
	if os.path.exists("findings/%s.txt" % keyword):
		with open("findings/%s.txt" % keyword, "r") as kf:
			stored_urls = kf.read().splitlines()
		if url not in stored_urls:
			print("[*] Found: %s" % title)
			if notify:
				do_ntfy(keyword, title, url)
	else:
		print("[*] Found: %s" % title)
		if notify:
			do_ntfy(keyword, title, url)
	with open("findings/%s.txt" % keyword, "a") as kf:
		kf.write("%s\r\n" % url)

def check_feeds():
	for feed in feeds:
		fd = feedparser.parse(feed)
		for keyword in keywords:
			for entry in fd.entries:
				title = entry.title.lower()
				if keyword in title:
					check_finding(keyword, title, entry.link)


while True:
	print("Checking feeds...")
	check_feeds()
	time.sleep(timer)