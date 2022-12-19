from django.contrib import admin

from .models import ShinoCategory, \
    Shino, Jacks, JacksCategory, CarLifts,CarLiftsCategory, Garage, GarageCategory, \
        ConsumablesCategory, Consumables, Spares, SparesCategory, Boxes, BoxesCategory, \
            Stands, StandsCategory, Gasoline,GasolineCategory, CamberToe,CamberToeCategory

# Register your models here.


admin.site.register(ShinoCategory)
admin.site.register(Shino)
admin.site.register(JacksCategory)
admin.site.register(Jacks)
admin.site.register(CarLiftsCategory)
admin.site.register(CarLifts)
admin.site.register(GarageCategory)
admin.site.register(Garage)

#####################################
admin.site.register(ConsumablesCategory)
admin.site.register(Consumables)
admin.site.register(SparesCategory)
admin.site.register(Spares)
admin.site.register(BoxesCategory)
admin.site.register(Boxes)
admin.site.register(Stands)
admin.site.register(StandsCategory)
admin.site.register(Gasoline)
admin.site.register(GasolineCategory)
admin.site.register(CamberToe)
admin.site.register(CamberToeCategory)
