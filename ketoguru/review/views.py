from django.shortcuts import render
from django.contrib.gis.measure import D
from django.contrib.gis.geos import Point

from review.models import Venue


# Create your views here.


def get_location_nearby(start_point: Point, distance_in_metres: int = 1000):
    """ take a point object eg `Point(115.75082274177393, -32.047240439099056)` and a distance in metres
    and return all items in the database within a radius of the point """
    return Venue.objects.filter(point__distance_lte=(start_point, D(m=distance_in_metres)))
