import requests
import json
from collections import OrderedDict
from .models import NotGames

# HAETAAN NIMEN PERUSTEELLA
# http://api.steampowered.com/ISteamApps/GetAppList/v0001/

# HAETAAN APPID:n PERUSTEELLA
# http://store.steampowered.com/api/appdetails?appids=516750


# Returns cleaned content based on appid
def getGameInfo(appid):

	wholeURL = "http://store.steampowered.com/api/appdetails?appids=" + str(appid)
	rGameInfo = requests.get(wholeURL)
	jsonGameInfo = rGameInfo.json()
	if jsonGameInfo is not None and jsonGameInfo[str(appid)]['success'] == True and jsonGameInfo[str(appid)]['data']['type'] == 'game':
	
		genres = []
		cats = []

		for genre in jsonGameInfo[str(appid)]['data']['genres']:
			genres.append(genre['description'])

		for cat in jsonGameInfo[str(appid)]['data']['categories']:
			cats.append(cat['description'])

		if 'price_overview' in jsonGameInfo[str(appid)]['data']:
			price = jsonGameInfo[str(appid)]['data']['price_overview']['final']
		else:
			price = 'Free'

		content = OrderedDict([
			('success', True),
			('gameId', str(appid)),
			('gameName', jsonGameInfo[str(appid)]['data']['name']),
			('gameDescription', jsonGameInfo[str(appid)]['data']['detailed_description']),
			('gamePrice', price),
			('gameImage', jsonGameInfo[str(appid)]['data']['header_image']),
			('gameDevelopers', jsonGameInfo[str(appid)]['data']['developers']),
			('gamePublishers', jsonGameInfo[str(appid)]['data']['publishers']),
			('gameGenres', genres),
			('gameCategories', cats)
		])

		return content

	return {
		'success': False,
		'message': "Game was not found with this appid!"
	}



# Finds appid:s for games based on search query
def findGames(name):

	rSteamGames = requests.get("http://api.steampowered.com/ISteamApps/GetAppList/v0001/").json()

	found = []

	for game in rSteamGames['applist']['apps']['app']:
		if name.lower() in game['name'].lower() and not NotGames.objects.filter(appid = game['appid']).exists():
			found.append({
				'appid': game['appid'],
				'name': game['name']
			})			

	to_json = json.dumps(found)

	return to_json
