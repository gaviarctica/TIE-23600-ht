from django.shortcuts import render
from django.http import HttpResponse
from . import steamapi, youtubeapi

def gamesearch(request, name):

	appid_list = steamapi.findGames(name)

	return HttpResponse(appid_list, content_type='application/json')

def gameinfo(request, appid):

	parsed_data = steamapi.getGameInfo(appid)
	return HttpResponse(parsed_data, content_type='application/json')
