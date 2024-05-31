from django.shortcuts import render, redirect
from calorie_tracker.models import Food,ConsumeFood
# Create your views here.

def index(request):
    context = {}
    if request.method == 'POST':
        food_consumed = request.POST.get('food_consumed')
        consumed_food = Food.objects.get(food_name=food_consumed)
        user = request.user
        consume_food = ConsumeFood.objects.create(user=user, food_consumed=consumed_food)
        consume_food.save()
        return redirect('index')  # Redirect after successful POST to avoid resubmission on refresh
    else:
        foods = Food.objects.all()
        food_consumption = ConsumeFood.objects.filter(user=request.user)
        context['foods'] = foods
        context['food_consumption'] = food_consumption
        return render(request, 'index.html', context)
    

def delete_consumed_food(request,id):
    cosumed_food = ConsumeFood.objects.get(id=id)
    if request.method == "POST":
        cosumed_food.delete()
        return redirect('index')
    return render(request, 'delete.html', {'cosumed_food':cosumed_food})

