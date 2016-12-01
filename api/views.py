from django.shortcuts import render
from django.http import HttpResponse
from . import steamapi, youtubeapi, redditapi
from .models import SearchHistory, NotGames
import json
import datetime
from collections import OrderedDict

# Default count for popular and recent results
DEFAULT_COUNT = 5

def checkRequest(request):

	if request.method != 'GET':
		falseRequest = {
			'status_code': 400,
			'message': "Please use GET request!"
		}
		return HttpResponse(json.dumps(falseRequest), content_type='application/json')

def gamesearch(request):

	checkRequest(request)

	if request.GET.get('q') is None or request.GET.get('q') == '':
		print("asd")

		falseQuery = {
			'success': False,
			'message': "No query string was given! Use argument 'q' to assign a query string."
		}

		return HttpResponse(json.dumps(falseQuery), content_type='application/json')

	appid_list = steamapi.findGames(request.GET.get('q'))

	return HttpResponse(appid_list, content_type='application/json')


def gameinfo(request):

	checkRequest(request)

	if request.method != 'GET':
		falseRequest = {
			'status_code': 400,
			'message': "Please use GET request!"
		}
		return HttpResponse(json.dumps(falseRequest), content_type='application/json')

	if request.GET.get('appid') is None:
		falseQuery = {
			'success': False,
			'message': "No appid was given! Use argument 'appid' to assign an appid query."
		}

		return HttpResponse(json.dumps(falseQuery), content_type='application/json')

	try:
		appid = int(request.GET.get('appid'))

	except ValueError:
		falseQuery = {
			'success': False,
			'message': "No valid appid was given! Appid has to be a number!"
		}

		return HttpResponse(json.dumps(falseQuery), content_type='application/json')

	if request.GET.get('videos') is not None:

		try:
			videos = int(request.GET.get('videos'))

		except ValueError:
			videos = 0
	else:
		videos = 0

	if request.GET.get('discussions') is not None:

		try:
			discussions = int(request.GET.get('discussions'))

		except ValueError:
			discussions = 0

	else:
		discussions = 0

	steamData = steamapi.getGameInfo(appid)

	if steamData['success'] == False:
		newNotGame = NotGames(appid = appid)
		newNotGame.save()
		jsonContent = json.dumps(steamData)
		return HttpResponse(jsonContent, content_type='application/json')

	# Combine the dicts
	if videos > 0:
		steamData.update(youtubeapi.getVideos(steamData['gameName'], videos))
	if discussions > 0:
		steamData.update(redditapi.getRedditDiscussions(steamData['gameName'], discussions))

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

	checkRequest(request)

	if request.GET.get('count') == None:
		count = DEFAULT_COUNT
	else:
		count = request.GET.get('count')

	try:
		popular = SearchHistory.objects.order_by('-searchCount')[:int(count)]

	except ValueError:
		popular = SearchHistory.objects.order_by('-searchCount')[:int(DEFAULT_COUNT)]

	except AssertionError:
		popular = SearchHistory.objects.order_by('-searchCount')[:int(DEFAULT_COUNT)]

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

	checkRequest(request)

	if request.GET.get('count') == None:
		count = DEFAULT_COUNT
	else:
		count = request.GET.get('count')

	try:
		recent = SearchHistory.objects.all()[:int(count)]

	except ValueError:
		recent = SearchHistory.objects.all()[:int(DEFAULT_COUNT)]

	except AssertionError:
		recent = SearchHistory.objects.all()[:int(DEFAULT_COUNT)]

	results = []

	for result in recent:
		results.append({
				'appid': result.appid,
				'name': result.name
			})	

	jsonContent = json.dumps(results)

	return HttpResponse(jsonContent, content_type='application/json')