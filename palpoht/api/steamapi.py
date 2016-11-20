import datetime
import requests
import json

# HAETAAN NIMEN PERUSTEELLA
# http://api.steampowered.com/ISteamApps/GetAppList/v0001/

# HAETAAN APPID:n PERUSTEELLA
# http://store.steampowered.com/api/appdetails?appids=516750

# Returns cleaned content based on appid
def getGameInfo(appid):

	wholeURL = "http://store.steampowered.com/api/appdetails?appids=" + str(appid)
	rGameInfo = requests.get(wholeURL)
	jsonGameInfo = rGameInfo.json()

	genres = []
	cats = []

	for genre in jsonGameInfo[appid]['data']['genres']:
		genres.append(genre['description'])

	for cat in jsonGameInfo[appid]['data']['categories']:
		cats.append(cat['description'])

	content = {
		'gameid': appid,
		'gamename': jsonGameInfo[appid]['data']['name'],
		'gamedescription': jsonGameInfo[appid]['data']['short_description'],
		'gameprice': jsonGameInfo[appid]['data']['price_overview']['final'],
		'gameimage': jsonGameInfo[appid]['data']['header_image'],
		'gamedevelopers': jsonGameInfo[appid]['data']['developers'],
		'gamepublishers': jsonGameInfo[appid]['data']['publishers'],
		'gamegenres': genres,
		'gamecategories': cats
	}

	jsoncontent = json.dumps(content)

	return jsoncontent

# Finds appid:s for games based on search query
def findGames(name):

	rSteamGames = requests.get("http://api.steampowered.com/ISteamApps/GetAppList/v0001/").json()

	found = []

	for game in rSteamGames['applist']['apps']['app']:
		if name.lower() in game['name'].lower():
			found.append({
				'appid': game['appid'],
				'name': game['name']
			})

	to_json = json.dumps(found)

	return to_json
