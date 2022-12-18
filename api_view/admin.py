from django.contrib import admin

from .models import ShinoCategory, \
    BalansCategory, Shino, Balans

# Register your models here.


admin.site.register(ShinoCategory)
admin.site.register(BalansCategory)
admin.site.register(Shino)
admin.site.register(Balans)