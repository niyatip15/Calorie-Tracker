from django.shortcuts import render, redirect
from calorie_tracker.models import Food,ConsumeFood
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import FormView
from django.urls import reverse_lazy
from django.contrib.auth import login
# Create your views here.

class CustomLoginView(LoginView):
    template_name = 'login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('index')
    
    
class Registeration(FormView):
    template_name = 'register.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('index')
    redirect_authenticated_user = True

    def form_valid(self,form):
        user = form.save()
        if user is not None:
            login(self.request,user)
        return super(Registeration,self).form_valid(form)
    
    def get(self,*args,**kwargs):
        if self.request.user.is_authenticated:
            return redirect('index')
        return super(Registeration,self).get(*args, **kwargs)
    

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

