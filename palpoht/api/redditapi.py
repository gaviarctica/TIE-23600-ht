#https://www.reddit.com/search.json?q=counter-strike&sort=top&limit=5&t=week&type=link
#https://www.reddit.com/search.json?sort=top&t=week&limit=5&syntax=cloudsearch&q=%28field+text+%27%22my%20summer%20car%22%27%29

# after	
# fullname of a thing
# before	
# fullname of a thing
# count	
# a positive integer (default: 0)
# include_facets	
# boolean value
# limit	
# the maximum number of items desired (default: 25, maximum: 100)
# q	
# a string no longer than 512 characters
# restrict_sr	
# boolean value
# show	
# (optional) the string all
# sort	
# one of (relevance, hot, top, new, comments)
# sr_detail	
# (optional) expand subreddits
# syntax	
# one of (cloudsearch, lucene, plain)
# t	
# one of (hour, day, week, month, year, all)
# type	
# (optional) comma-delimited list of result types (sr, link)

from collections import OrderedDict
import requests
import time

def getRedditDiscussions(name):

	wholeURL = 'https://www.reddit.com/search.json?sort=top&t=week&limit=5&syntax=cloudsearch&q=(field+text+\'"' + name + '"\')'
	rDiscussionInfo = requests.get(wholeURL, headers = {'User-agent': 'School project by /u/gtpalpo'})
	jsonDiscussionInfo = rDiscussionInfo.json()

	if jsonDiscussionInfo is not None:

		found = []

		try:
			for discussion in jsonDiscussionInfo['data']['children']:
				found.append({
					'title': discussion['data']['title'],
					'url': discussion['data']['url'],
					'permalink': discussion['data']['permalink'],
					'subreddit': discussion['data']['subreddit'],
				})
		except KeyError:
			print(jsonDiscussionInfo)

	foundList = OrderedDict([ ('redditDiscussions', found) ])

	return foundList
