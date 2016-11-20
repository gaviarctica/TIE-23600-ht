from django.db import models

class LastDBUpdate(models.Model):
	lastupdate = models.DateTimeField()

class GameID(models.Model):
	appid = models.IntegerField()
	name = models.CharField(max_length = 100)

	class Meta:
		ordering = ['name']
