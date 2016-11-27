from django.contrib import admin
from .models import SearchHistory, NotGames

# Register your models here.
class SearchHistoryAdmin(admin.ModelAdmin):
	pass

class NotGamesAdmin(admin.ModelAdmin):
 	pass

admin.site.register(SearchHistory, SearchHistoryAdmin)
admin.site.register(NotGames, NotGamesAdmin)