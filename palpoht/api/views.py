from django.shortcuts import render
from django.http import HttpResponse
from . import steamapi, youtubeapi, redditapi
from .models import SearchHistory, NotGames
import json
import datetime
from collections import OrderedDict

def gamesearch(request, name):

	appid_list = steamapi.findGames(name)

	return HttpResponse(appid_list, content_type='application/json')


def gameinfo(request, appid):

	steamData = steamapi.getGameInfo(appid)

	if steamData['success'] == False:
		newNotGame = NotGames(appid = appid)
		newNotGame.save()
		jsonContent = json.dumps(steamData)
		return HttpResponse(jsonContent, content_type='application/json')

	youtubeData = youtubeapi.getVideos(steamData['gameName'], 4)
	redditData = redditapi.getRedditDiscussions(steamData['gameName'])

	# Combine the dicts
	steamData.update(youtubeData)
	steamData.update(redditData)
	combinedData = steamData

	#Add to database search history
	if SearchHistory.objects.filter(appid = int(combinedData['gameId'])).exists():
		editHistory = SearchHistory.objects.get(appid = int(combinedData['gameId']))
		editHistory.lastSearchDate = datetime.datetime.now()
		editHistory.searchCount = editHistory.searchCount + 1
		editHistory.save()
	else:		
		newSearch = SearchHistory(appid = int(combinedData['gameId']), name = combinedData['gameName'], searchCount = 1, lastSearchDate = datetime.datetime.now())
		newSearch.save()

	jsonContent = json.dumps(combinedData)
	return HttpResponse(jsonContent, content_type='application/json')


def popular(request):
	count = request.GET.get('count')
	popular = SearchHistory.objects.order_by('-searchCount')[:int(count)]

	results = []

	for result in popular:
		results.append({
				'appid': result.appid,
				'name': result.name,
				'searchCount': result.searchCount
			})	

	jsonContent = json.dumps(results)

	return HttpResponse(jsonContent, content_type='application/json')


def recent(request):
	count = request.GET.get('count')
	recent = SearchHistory.objects.all()[:int(count)]

	results = []

	for result in recent:
		results.append({
				'appid': result.appid,
				'name': result.name
			})	

	jsonContent = json.dumps(results)

	return HttpResponse(jsonContent, content_type='application/json')