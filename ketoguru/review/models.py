from django.contrib.gis.db import models
from django.urls import reverse
from django.utils.translation import gettext as _


# Create your models here.


class Location(models.Model):
    address = models.CharField(_("Address"), max_length=150)
    suburb = models.CharField(_("Suburb"), max_length=50)  # should have validations
    state = models.CharField(_("State"), max_length=50, default='WA')  # should be a choice field and limited to country options
    postcode = models.CharField(_("Postcode"), max_length=50)  # should have validations
    country = models.CharField(_("Country"), max_length=50, default='Australia')  # should be a choice field

    point = models.PointField(_("Location"), null=True, unique=True)

    class Meta:
        abstract = True


class Venue(Location):
    name = models.CharField(_("Name"), max_length=100)

    class Meta:
        verbose_name = _("venue")
        verbose_name_plural = _("venues")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("venue_detail", kwargs={"pk": self.pk})


class Meal(models.Model):
    venue = models.ForeignKey(Venue, related_name="meals", on_delete=models.CASCADE)
    name = models.CharField(_("Name"), max_length=50)
    description = models.TextField(_("Description"), blank=True)

    class Meta:
        verbose_name = _("meal")
        verbose_name_plural = _("meals")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("meal_detail", kwargs={"pk": self.pk})


class Review(models.Model):
    meal = models.ForeignKey(Meal, related_name='reviews', on_delete=models.CASCADE)
    rating = models.FloatField(_("Rating"))
    detail = models.TextField(_("Detail"), blank=True)
    image = models.ImageField(_("Image"), null=True, blank=True)

    class Meta:
        verbose_name = _("review")
        verbose_name_plural = _("reviews")

    def __str__(self):
        return f"Meal:{self.meal_id}-Rating:{self.rating}"

    def get_absolute_url(self):
        return reverse("review_detail", kwargs={"pk": self.pk})
