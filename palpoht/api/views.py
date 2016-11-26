from django.shortcuts import render
from django.http import HttpResponse
from . import steamapi, youtubeapi
import json

def gamesearch(request, name):

	appid_list = steamapi.findGames(name)

	return HttpResponse(appid_list, content_type='application/json')

def gameinfo(request, appid):

	steamData = steamapi.getGameInfo(appid)

	if steamData['success'] == False:
		jsonContent = json.dumps(steamData)
		return HttpResponse(jsonContent, content_type='application/json')

	youtubeData = youtubeapi.getVideos(steamData['gameName'], 4)

	# Combine the dicts
	combinedData = { **steamData, **youtubeData }
	
	jsonContent = json.dumps(combinedData)
	return HttpResponse(jsonContent, content_type='application/json')
