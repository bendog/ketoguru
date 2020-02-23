from django.contrib.gis import admin

from .models import Venue, Meal, Review


# Register your models here.


class VenueAdmin(admin.ModelAdmin):
    pass


admin.site.register(Venue, admin.OSMGeoAdmin)


@admin.register(Meal)
class MealAdmin(admin.ModelAdmin):
    pass


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    pass
