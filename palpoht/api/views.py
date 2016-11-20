from django.shortcuts import render
from django.http import HttpResponse
import json
from . import steamapi, youtubeapi

def gameinfo(request, name):

	#steaminfo = getGameInfo(name)
	gameid = 123
	gamename = 'name'
	gamedescription = 'desc'
	gameprice = 9001
	gameimage = 'imagelink'
	gamedevelopers = 'devs'
	gamepublishers = 'pubs'
	gamegenres = 'genres'
	gamecategories = 'cats'
	#gamevideos = getVideos(name)
	gamevideos = 'vids'

	content = {
		'gameid': gameid,
		'gamename': gamename,
		'gamedescription': gamedescription,
		'gameprice': gameprice,
		'gameimage': gameimage,
		'gamedevelopers': gamedevelopers,
		'gamepublishers': gamepublishers,
		'gamegenres': gamegenres,
		'gamecategories': gamecategories,
		'gamevideos': gamevideos
	}

	jsoncontent = json.dumps(content)

	return HttpResponse(jsoncontent)
