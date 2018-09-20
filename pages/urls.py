from django.urls import path

from .views import HomePageView, KitchenPageView, BathroomPageView
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    path('kitchen/', KitchenPageView.as_view(), name='kitchen'),
    path('bathroom/', BathroomPageView.as_view(), name='bathroom'),
    path('windows_and_doors/', BathroomPageView.as_view(), name='windows'),
    path('roofing/', BathroomPageView.as_view(), name='roofing'),
    path('paint_jobs/', BathroomPageView.as_view(), name='paint'),
    path('floors/', BathroomPageView.as_view(), name='floors'),
    path('expanding/', BathroomPageView.as_view(), name='expanding'),
    path('driveways_and_walkways/', BathroomPageView.as_view(), name='driveways'),
    path('', HomePageView.as_view(), name='home')
]

urlpatterns += staticfiles_urlpatterns()
