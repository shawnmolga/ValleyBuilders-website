from django.urls import path

from .views import HomePageView, KitchenPageView, BathroomPageView, FloorsPageView, ExpandingPageView, DrivewaysPageView, RoofingPageView, WindowsPageView, PaintPageView, PatiosPageView
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    path('kitchen/', KitchenPageView.as_view(), name='kitchen'),
    path('bathroom/', BathroomPageView.as_view(), name='bathroom'),
    path('windows_and_doors/', WindowsPageView.as_view(), name='windows'),
    path('roofing/', RoofingPageView.as_view(), name='roofing'),
    path('paint_jobs/', PaintPageView.as_view(), name='paint'),
    path('floors/', FloorsPageView.as_view(), name='floors'),
    path('expanding/', ExpandingPageView.as_view(), name='expanding'),
    path('driveways_and_walkways/', DrivewaysPageView.as_view(), name='driveways'),
    path('patios/', PatiosPageView.as_view(), name='patios'),
    path('', HomePageView.as_view(), name='home')

]

urlpatterns += staticfiles_urlpatterns()
