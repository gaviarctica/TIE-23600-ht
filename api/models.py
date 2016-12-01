from django.db import models

class SearchHistory(models.Model):
	appid = models.IntegerField(primary_key = True)
	name = models.CharField(max_length = 200)
	searchCount = models.IntegerField(default = 0)
	lastSearchDate = models.DateTimeField(auto_now = True)	

	class Meta:
		ordering = ['-lastSearchDate', 'name']

	def __str__(self):
		return '%s %s' % ( self.appid, self.name )

class NotGames(models.Model):
	appid = models.IntegerField(primary_key = True)

	def __str__(self):
		return '%s' % ( self.appid )
