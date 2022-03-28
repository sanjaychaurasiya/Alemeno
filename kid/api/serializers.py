from rest_framework import serializers
from kid.models import KidTable, ImageTable


class KidTableSerializer(serializers.ModelSerializer):
    class Meta:
        model = KidTable
        fields = "__all__"


class ImageTableSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageTable
        fields = "__all__"
