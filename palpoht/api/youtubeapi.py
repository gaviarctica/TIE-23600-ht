import requests

def getVideos(name):
	API_KEY = 'AIzaSyBuVlLJ3GLgSKIon98nvkWZW4q8q-01H7E'
	requestURL = 'https://www.googleapis.com/youtube/v3/search?part=id&maxResults=3&type=video&q=' + name + '&key=' + API_KEY
	requestResult = requests.get(requestURL).json()
	
	videoIDs = []

	for video in requestResult['items']:
		videoIDs.append(video['id']['videoId'])

	print(videoIDs)

	videoIDList = { 'videoIDs': videoIDs }

	print(videoIDList)

	return videoIDList
	