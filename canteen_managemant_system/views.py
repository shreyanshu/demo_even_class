from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, HttpResponse, redirect, reverse
from django.urls import reverse_lazy

from canteen_managemant_system.models import FoodItem, Cook
from canteen_managemant_system.forms import FoodItemForm, FoodItemModelForm, CookModelForm, LoginForm
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib import messages
# from .models import
# Create your views here.

def home(request):
    # data model, design template
    # context
    list_friends = ['ram', 'hari', 'sita']
    return render(request, 'home.html', context={'list_sahti':list_friends})


def list_food(request):
    list_food = FoodItem.objects.all()
    # list_food - list of objects
    return render(request, 'food/list_food.html', context={'list_food': list_food})


@login_required(login_url=reverse_lazy('cms:login'))
def add_food(request):
    if request.method == 'GET':
        food_form = FoodItemModelForm()
        return render(request, 'add_food.html', {'food_form': food_form})
    elif request.method == 'POST':
        food_form = FoodItemModelForm(request.POST)
        if food_form.is_valid():
            food_form.save()
            return redirect('cms:list_food')
        else:
            return render(request, 'add_food.html', {'food_form': food_form})


def edit_food(request, id):
    food = FoodItem.objects.get(id=id)
    if request.method == 'GET':
        form = FoodItemModelForm(instance=food)
        return render(request, 'edit_food.html', {'form': form})
    elif request.method == 'POST':
        form = FoodItemModelForm(request.POST, instance=food)
        if form.is_valid():
            form.save()
            return redirect('cms:list_food')
        else:
            return render(request, 'edit_food.html', {'form': form})


def delete_food(request, id):
    food = FoodItem.objects.get(id=id)
    food.delete()
    return redirect('cms:list_food')


class ListCookView(View):
    def get(self, request):
        cook_list = Cook.objects.all()
        return render(request, 'list_cook.html', {'cook_list': cook_list})
    #
    def post(self):
        pass


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        cooks = Cook.objects.all()
        return {'login': "Login", 'cooks': cooks}


class CookListView(ListView):
    model = Cook
    template_name = 'list_cook.html'
    context_object_name = 'cook_list'
    # queryset = Cook.objects.filter(age__gt=20)


class CookDetailView(DetailView):
    model = Cook
    template_name = 'cook_detail.html'


class CreateCookView(CreateView):
    # model = Cook
    # fields = ['name', 'age', 'profile_pic']
    template_name = 'create_cook.html'
    success_url = reverse_lazy('cms:list_cook')
    form_class = CookModelForm


class UpdateCookView(UpdateView):
    model = Cook
    form_class = CookModelForm
    template_name = 'update_cook.html'
    success_url = reverse_lazy('cms:list_cook')

    # def get_object(self, queryset=None):
    #     return Cook.objects.get(name=self.kwargs.get('name'))


class DeleteCookView(DeleteView):
    model = Cook
    template_name = 'delete_confirmation.html'
    success_url = reverse_lazy('cms:list_cook')


def login_view(request):
    if request.method == 'GET':
        login_form = LoginForm()
        return render(request, 'login.html', {'login_form': login_form})
    elif request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                messages.success(request, 'Login Successful')
                return redirect('cms:list_food')
            else:
                return redirect('cms:login')
        else:
            messages.warning(request, 'Invalid username and password')
            return redirect('cms:login')