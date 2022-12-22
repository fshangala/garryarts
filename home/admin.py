from django.contrib import admin
from . import models

# Register your models here.
@admin.action(description="Mark as sold")
def mark_as_sold(modeladmin,request,queryset):
    queryset.update(available=False)
    
@admin.register(models.Art)
class ArtAdmin(admin.ModelAdmin):
    list_display=["image","price","available"]
    actions=[mark_as_sold]

@admin.register(models.Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display=["phone","name"]

@admin.register(models.ArtOrder)
class ArtOrderAdmin(admin.ModelAdmin):
    list_display=["date","customer"]