from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from django.core.mail import send_mail
from .serializers import KidTableSerializer, ImageTableSerializer
from kid.models import KidTable, ImageTable
from .serializers import KidTableSerializer, ImageTableSerializer
from .send_email import send_data


# class KidListView(generics.ListAPIView):
#     queryset = KidTable.objects.all()
#     serializer_class = KidSerializer


class KidListView(APIView):
    """Class based view to get all the object's details and to post data."""

    def get(self, request):
        kids = KidTable.objects.all()
        serializer = KidTableSerializer(kids, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = KidTableSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)


# class ImageTableListView(generics.ListAPIView):
#     queryset = ImageTable.objects.all()
#     serializer_class = ImageTableSerializer


class ImageTableListView(APIView):
    def get(self, request):
        images = ImageTable.objects.all().prefetch_related()
        serializer = ImageTableSerializer(images, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ImageTableSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            if serializer.data['food_group'] == "Unknown":
                send_data(serializer.data['parent_email'])
                # send_mail(
                #     'Unknown',
                #     'The image does not contain food.',
                #     'smtptesting404@gmail.com',
                #     'smtptesting404@gmail.com', # serializer.data['parent_email'],
                #     fail_silently=True,
                # )
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
