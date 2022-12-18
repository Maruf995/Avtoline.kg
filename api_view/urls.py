from django.urls import path
from . import views

urlpatterns = [
    path("", views.MainCategory),
    # path("equipment/", views.EquipmentList.as_view()),
    path("tire_fitting/", views.ShinoList.as_view()),
    path("balans/", views.BalansList.as_view()),
    path("tire_fitting/<int:id>/", views.ShinoDetailView.as_view()),
    path("balans/<int:id>/", views.BalansDetailView.as_view()),
]