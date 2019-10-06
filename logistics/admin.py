from django.contrib import admin
from .models import Stock, Base, Staff, Distribution, Food, StaffSchedule

class StockAdmin(admin.ModelAdmin):
    list_display = ('id', 'food', 'date', 'quantity', 'base')
    list_display_links = ('food', )

class BaseAdmin(admin.ModelAdmin):
    list_display = ('name_ja', 'name_en', 'no')

class FoodAdmin(admin.ModelAdmin):
    list_display = ('name', 'category')

class StaffAdmin(admin.ModelAdmin):
    list_display = ('name', 'base')

class StaffScheduleAdmin(admin.ModelAdmin):
    list_display= ('staff', 'task', 'start', 'end')


admin.site.register(Stock, StockAdmin)
admin.site.register(Base, BaseAdmin)
admin.site.register(Staff, StaffAdmin)
admin.site.register(Distribution)
admin.site.register(Food, FoodAdmin)
admin.site.register(StaffSchedule, StaffScheduleAdmin)