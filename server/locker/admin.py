from django.contrib import admin
from .models import Favorites, Locker, MeMo
# Register your models here.
admin.site.register(Locker)

admin.site.register(MeMo)

admin.site.register(Favorites)