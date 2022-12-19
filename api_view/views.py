from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView

from api_view.models import ShinoCategory, \
    Shino, Jacks, JacksCategory, CarLifts,CarLiftsCategory, Garage, GarageCategory, \
        ConsumablesCategory, Consumables, Spares, SparesCategory, Boxes, BoxesCategory, \
            Stands, StandsCategory, Gasoline,GasolineCategory, CamberToe,CamberToeCategory



# Create your views here.

def MainCategory(request):
    shino = ShinoCategory.objects.all()
    jacks = JacksCategory.objects.all()
    carlifts = CarLiftsCategory.objects.all()
    garage = GarageCategory.objects.all()
    #######################################
    consumables = ConsumablesCategory.objects.all
    spares = SparesCategory.objects.all()
    boxes = BoxesCategory.objects.all()
    stands = StandsCategory.objects.all()
    gasoline = GasolineCategory.objects.all()
    camber = CamberToeCategory.objects.all()
    return render(request, 'main.html', {'shino': shino, 'jacks': jacks, 'carlifts': carlifts,'garage': garage,\
        'consumables': consumables, 'spares': spares, 'boxes': boxes, 'stands': stands, 'gasoline': gasoline,'camber': camber })


class ShinoList(ListView):
    queryset = Shino.objects.all()
    template_name = "list/shino.html"
    context_object_name = "shino"


class ShinoDetailView(DetailView):
    queryset = Shino.objects.all()
    template_name = "detail/shino_detail.html"
    context_object_name = "shino"
    pk_url_kwarg = "id"

    # ДЗ
    def post(self, request, *args, **kwargs):
        blog = self.get_object()
        pass

class JacksList(ListView):
    queryset = Jacks.objects.all()
    template_name = "list/jacks.html"
    context_object_name = "jacks"


class JacksDetailView(DetailView):
    queryset = Jacks.objects.all()
    template_name = "detail/jacks_detail.html"
    context_object_name = "jacks"
    pk_url_kwarg = "id"

    # ДЗ
    def post(self, request, *args, **kwargs):
        blog = self.get_object()
        pass

class CarLiftssList(ListView):
    queryset = CarLifts.objects.all()
    template_name = "list/car_lifts.html"
    context_object_name = "carlifts"


class CarLiftsDetailView(DetailView):
    queryset = CarLifts.objects.all()
    template_name = "detail/car_lifts_detail.html"
    context_object_name = "carlifts"
    pk_url_kwarg = "id"

    # ДЗ
    def post(self, request, *args, **kwargs):
        blog = self.get_object()
        pass

class GarageList(ListView):
    queryset = Garage.objects.all()
    template_name = "list/garage.html"
    context_object_name = "garage"


class GarageDetailView(DetailView):
    queryset = Garage.objects.all()
    template_name = "detail/garage_detail.html"
    context_object_name = "garage"
    pk_url_kwarg = "id"

    # ДЗ
    def post(self, request, *args, **kwargs):
        blog = self.get_object()
        pass

###########################################################
class ConsumablesList(ListView):
    queryset = Consumables.objects.all()
    template_name = "list/consumables.html"
    context_object_name = "consumables"


class ConsumablesDetailView(DetailView):
    queryset = Consumables.objects.all()
    template_name = "detail/consumables_detail.html"
    context_object_name = "consumables"
    pk_url_kwarg = "id"

    # ДЗ
    def post(self, request, *args, **kwargs):
        blog = self.get_object()
        pass

class BoxesList(ListView):
    queryset = Boxes.objects.all()
    template_name = "list/boxes.html"
    context_object_name = "boxes"


class BoxesDetailView(DetailView):
    queryset = Boxes.objects.all()
    template_name = "detail/boxes_detail.html"
    context_object_name = "boxes"
    pk_url_kwarg = "id"

    # ДЗ
    def post(self, request, *args, **kwargs):
        blog = self.get_object()
        pass

class StandsList(ListView):
    queryset = Stands.objects.all()
    template_name = "list/stands.html"
    context_object_name = "stands"


class StandsDetailView(DetailView):
    queryset = Stands.objects.all()
    template_name = "detail/stands_detail.html"
    context_object_name = "stands"
    pk_url_kwarg = "id"

    # ДЗ
    def post(self, request, *args, **kwargs):
        blog = self.get_object()
        pass

class GasolinePumpList(ListView):
    queryset = Gasoline.objects.all()
    template_name = "list/gasoline.html"
    context_object_name = "gasoline"


class GasolinePumpDetailView(DetailView):
    queryset = Gasoline.objects.all()
    template_name = "detail/gasoline_detail.html"
    context_object_name = "gasoline"
    pk_url_kwarg = "id"

    # ДЗ
    def post(self, request, *args, **kwargs):
        blog = self.get_object()
        pass

class SparesDetailView(DetailView):
    queryset = Spares.objects.all()
    template_name = "detail/spares_detail.html"
    context_object_name = "spares"
    pk_url_kwarg = "id"

    # ДЗ
    def post(self, request, *args, **kwargs):
        blog = self.get_object()
        pass

class SparesList(ListView):
    queryset = Spares.objects.all()
    template_name = "list/spares.html"
    context_object_name = "spares"

class CamberToeList(ListView):
    queryset = Garage.objects.all()
    template_name = "list/camber.html"
    context_object_name = "camber"

class CamberToeDetailView(DetailView):
    queryset = CamberToe.objects.all()
    template_name = "detail/camber_detail.html"
    context_object_name = "camber"
    pk_url_kwarg = "id"

    # ДЗ
    def post(self, request, *args, **kwargs):
        blog = self.get_object()
        pass
