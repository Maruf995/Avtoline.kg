from django.urls import path
from . import views

urlpatterns = [
    path("", views.MainCategory),
    path("tire_fitting/", views.ShinoList.as_view()),
    path("tire_fitting/<int:id>/", views.ShinoDetailView.as_view()),
    path("jacks/", views.JacksList.as_view()),
    path("jacks/<int:id>/", views.JacksDetailView.as_view()),
    path("garage/", views.GarageList.as_view()),
    path("garage/<int:id>/", views.GarageDetailView.as_view()),
    #######################################################################
    path("consumables/", views.ConsumablesList.as_view()),
    path("consumables/<int:id>/", views.ConsumablesDetailView.as_view()),
    path("boxes/", views.BoxesList.as_view()),
    path("boxes/<int:id>/", views.BoxesDetailView.as_view()),
    path("stands/", views.StandsList.as_view()),
    path("stands/<int:id>/", views.StandsDetailView.as_view()),
    path("gasoline/", views.GasolinePumpList.as_view()),
    path("gasoline/<int:id>/", views.GasolinePumpDetailView.as_view()),
    path("spares/", views.SparesList.as_view()),
    path("spares/<int:id>/", views.SparesDetailView.as_view()),
    path("camber/", views.CamberToeList.as_view()),
    path("camber/<int:id>/", views.CamberToeDetailView.as_view()),

]