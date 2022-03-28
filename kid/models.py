from django.db import models
from django.utils.translation import gettext_lazy as _


# Create your models here.
class KidTable(models.Model):
    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    parent_phone = models.IntegerField()
    parent_email = models.EmailField(max_length=254)

    def __str__(self):
        return self.name + "  |  " + self.parent_email


class ImageTable(models.Model):
    kid_table = models.ForeignKey(KidTable, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='MEDIA_ROOT/uploads/%Y/%m/%d/', height_field=None, width_field=None, max_length=100)
    image_url = models.URLField(max_length=200)
    created_on = models.DateTimeField(auto_now_add=False)
    updated_on = models.DateTimeField(auto_now_add=False)
    is_approved = models.BooleanField()
    approved_by = models.CharField(max_length=100)

    class Group(models.TextChoices):
        FRUIT = 'Fruit', _('Fruit')
        VEGETABLE = 'Veg', _('Vegetable')
        GRAIN = 'Grain', _('Grain')
        PROTEIN = 'Protein', _('Protein')
        DAIRY = 'Dairy', _('Dairy')
        UNKNOWN = 'Unknown', _('Unknown')

    food_group = models.CharField(max_length=100, choices=Group.choices)

    def __str__(self):
        return self.food_group
