from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView

from api_view.models import ShinoCategory, BalansCategory, Shino, Balans


# Create your views here.

def MainCategory(request):
    shino = ShinoCategory.objects.all()
    balans = BalansCategory.objects.all()
    return render(request, 'main.html', {'shino': shino, 'balans': balans})


class ShinoList(ListView):
    queryset = Shino.objects.all()
    template_name = "shino.html"
    context_object_name = "shino"

class BalansList(ListView):
    queryset = Balans.objects.all()
    template_name = "balans.html"
    context_object_name = "balans"

class ShinoDetailView(DetailView):
    queryset = Shino.objects.all()
    template_name = "shino_detail.html"
    context_object_name = "shino"
    pk_url_kwarg = "id"

    # ДЗ
    def post(self, request, *args, **kwargs):
        blog = self.get_object()
        pass

class BalansDetailView(DetailView):
    queryset = Shino.objects.all()
    template_name = "balans_detail.html"
    context_object_name = "balans"
    pk_url_kwarg = "id"

    # ДЗ
    def post(self, request, *args, **kwargs):
        blog = self.get_object()
        pass