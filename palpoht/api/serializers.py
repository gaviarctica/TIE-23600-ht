from rest_framework import serializers
from api.models import GameID

class GameInfoSerializer(serializers.Serializer):
	gameid = serializers.IntegerField()
	gamename = serializers.CharField(max_length = 100)
	gamedescription = serializers.TextField()
	gameprice = serializers.IntegerField()
	gameimage = serializers.CharField(max_length = 200)
	gamedevelopers = serializers.TextField()
	gamepublishers = serializers.TextField()
	gamegenres = serializers.TextField()
	gamecategories = serializers.TextField()
	gamevideos = serializers.TextField()
