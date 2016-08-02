from django.contrib import admin

from .models import Plano
# Register your models here.

class PlanoAdmin(admin.ModelAdmin):

	list_display = ['name' , 'description', 'price']
	search_fields = ['name', 'price']
	prepopulated_fields = {'slug': ('name',)}

admin.site.register(Plano, PlanoAdmin)