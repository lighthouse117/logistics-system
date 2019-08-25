from django.contrib import admin
from .models import Stock, Base, Staff, Distribution, Food

class StockAdmin(admin.ModelAdmin):
    list_display = ('id', 'food', 'date', 'quantity', 'base')
    list_display_links = ('food', )

class BaseAdmin(admin.ModelAdmin):
    list_display = ('name_ja', 'name_en', 'no')

class FoodAdmin(admin.ModelAdmin):
    list_display = ('name', 'category')


admin.site.register(Stock, StockAdmin)
admin.site.register(Base, BaseAdmin)
admin.site.register(Staff)
admin.site.register(Distribution)
admin.site.register(Food, FoodAdmin)