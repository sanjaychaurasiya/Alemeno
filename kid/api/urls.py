from django.urls import path, include
from .views import KidListView, ImageTableListView


urlpatterns = [
    path('kids/', KidListView.as_view(), name="Kid-List-View"),
    path('images/', ImageTableListView.as_view(), name='Image-Table-List-View')
]