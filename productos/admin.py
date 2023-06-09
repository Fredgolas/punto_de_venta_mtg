from django.contrib import admin
from productos.models import Card

# Register your models here.
class CardAdmin(admin.ModelAdmin):
    pass

admin.site.register(Card, CardAdmin)