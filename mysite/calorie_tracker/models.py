from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Food(models.Model):
    food_name = models.CharField(max_length=150)
    carbohydrate = models.DecimalField(max_digits=5, decimal_places=2)
    protien = models.DecimalField(max_digits=5, decimal_places=2)
    fats = models.DecimalField(max_digits=5, decimal_places=2)
    calories = models.IntegerField()
    
    
    def __str__(self):
        return self.food_name
    
class ConsumeFood(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    food_consumed = models.ForeignKey(Food,on_delete=models.CASCADE)
    
    def __str__(self):
        return f'{self.user.username} - {self.food_consumed}'
    