# RSSNTFY
Monitors RSS feeds for keywords and sends notifications

## Setup
* Open up rssntfy.py and edit the settings to your liking.
* Add one keyword per line to the keywords.txt file
* Add one rss feed per line in the feeds.txt file

## Operation
Complete setup and launch rssntfy.py, it will write findings to console as well as creating a folder called findings where each url will be added to a file with the name of the keyword.

## Plugins
Each plugin will need to be configured manually, for example if you decide to use pushover you need to add the api and user key into the pushover.py file.

If you wish to add a plugin just create the .py file with a SendMessage function that accepts keyword, title, url; then add the plugin name to the __init__.py file within the plugins folder.

## TODO
* I have yet to finish the daily notifications, currently immediate notifications do work.
* I don't use the email plugin so I haven't tested it at all, pushover works.
