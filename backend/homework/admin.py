from django.contrib import admin
from homework.models import HomeWork

@admin.register(HomeWork)
class HomeWorkAdmin(admin.ModelAdmin):
	list_display = [
        'id',
        'title',
        'description'
        ]