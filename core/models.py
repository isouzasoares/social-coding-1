from django.db import models

from django.utils.translation import ugettext_lazy as _

from django_extensions.db.fields import CreationDateTimeField

# Create your models here.


class Place(models.Model):
    """
    """
    class Meta:
        verbose_name = _('Place')
        verbose_name_plural = _('Places')

    venue_id = models.CharField(
        _("Foursquare Venue ID"),
        max_length=12
    )

    def __unicode__(self):
        pass


class Consumer(models.Model):
    """
    """
    class Meta:
        verbose_name = _('Consumer')
        verbose_name_plural = _('Consumers')

    foursquare_uid = models.CharField(
        _("Foursquare UID"),
        max_length=12)

    sex = models.CharField(
        max_length="1",
        choices=("m", _("Male"), "f", _("Female"))
    )

    def __unicode__(self):
        pass


class Rating(models.Model):
    """
    """
    class Meta:
        verbose_name = _('Rating')
        verbose_name_plural = _('Ratings')

    consumer = models.ForeignKey("Consumer")

    place = models.ForeignKey("Place")

    created_at = CreationDateTimeField(_("Created_at"))

    description = models.TextField(
        null=True,
        blank=True)

    CHOICES = (
        ("po", _("Positive")),
        ("ne", _("Negative")),
    )

    rating = models.CharField(max_length=2,
                              choices=CHOICES,
                              default="po")

    median_age = models.PositiveSmallIntegerField(
        null=True,
        blank=True
    )

    def __unicode__(self):
        return "{0}: {1}".format(self.consumer, self.place)
