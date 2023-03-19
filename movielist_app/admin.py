from django.contrib import admin
from movielist_app.models import Review, Watchlist,StreamPlatform,Review
# Register your models here.
admin.site.register(Watchlist)
admin.site.register(StreamPlatform)
admin.site.register(Review)