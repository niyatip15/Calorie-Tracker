from django.contrib import admin
from calorie_tracker.models import Food, ConsumeFood

# Register your models here.

class FoodAdmin(admin.ModelAdmin):
    list_display = ('food_name', 'carbohydrate', 'protien', 'fats', 'calories')
    search_fields = ('food_name',)

class ConsumeFoodAdmin(admin.ModelAdmin):
    list_display = ('user', 'food_consumed')
    list_filter = ('user',)

admin.site.register(Food, FoodAdmin)
admin.site.register(ConsumeFood, ConsumeFoodAdmin)