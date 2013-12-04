from django.contrib import admin
from core.models import Consumer, Place, Rating


class ConsumerAdmin(admin.ModelAdmin):
    pass

admin.site.register(Consumer, ConsumerAdmin)


class PlaceAdmin(admin.ModelAdmin):
    pass

admin.site.register(Place, PlaceAdmin)


class RatingAdmin(admin.ModelAdmin):
    pass

admin.site.register(Rating, RatingAdmin)
