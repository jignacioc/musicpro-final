from django.urls import path
from .views import index, base, aboutus

urlpatterns = [
    path('', base, name="base"),
    path('index/', index, name="index"),
    path('about-us/', aboutus, name="aboutus"),
]
