
# pages/views.py
from django.views.generic import TemplateView


class HomePageView(TemplateView):
    template_name = 'index.html'


class KitchenPageView(TemplateView):
    template_name = 'Kitchen.html'


class BathroomPageView(TemplateView):
    template_name = 'bathroom.html'


class DrivewaysPageView(TemplateView):
    template_name = 'driveways.html'


class ExpandingPageView(TemplateView):
    template_name = 'expanding.html'


class FloorsPageView(TemplateView):
    template_name = 'floors.html'


class PaintPageView(TemplateView):
    template_name = 'paint.html'


class PatiosPageView(TemplateView):
    template_name = 'patios.html'


class RoofingPageView(TemplateView):
    template_name = 'roofing.html'


class WindowsPageView(TemplateView):
    template_name = 'windows.html'



