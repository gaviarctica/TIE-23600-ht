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

	if jsonGameInfo is not None and jsonGameInfo[appid]['success'] == True and jsonGameInfo[appid]['data']['type'] == 'game':
	
		genres = []
		cats = []

		for genre in jsonGameInfo[appid]['data']['genres']:
			genres.append(genre['description'])

		for cat in jsonGameInfo[appid]['data']['categories']:
			cats.append(cat['description'])

		content = {
			'success': True,
			'gameId': appid,
			'gameName': jsonGameInfo[appid]['data']['name'],
			'gameDescription': jsonGameInfo[appid]['data']['short_description'],
			'gamePrice': jsonGameInfo[appid]['data']['price_overview']['final'],
			'gameImage': jsonGameInfo[appid]['data']['header_image'],
			'gameDevelopers': jsonGameInfo[appid]['data']['developers'],
			'gamePublishers': jsonGameInfo[appid]['data']['publishers'],
			'gameGenres': genres,
			'gameCategories': cats
		}

		return content

	return {'success': False}



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
