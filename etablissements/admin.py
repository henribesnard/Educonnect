from django.contrib import admin
from .models import EstablishmentType, Establishment

@admin.register(EstablishmentType)
class establishmentTypeAdmin(admin.ModelAdmin):
    pass

@admin.register(Establishment)
class EstablishmentAdmin(admin.ModelAdmin):
    pass