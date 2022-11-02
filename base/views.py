from multiprocessing import context
from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from base.models import User
from .forms import CreateUserForm
# Create your views here.


class CustomLoginView(LoginView):
    template_name = 'base/login.html'
    field = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('users')

@login_required
def users(request):
    return render(request, 'base/admin.html')


def settings(request):
    return render(request, 'base/settings.html')
def profile(request):
    return render(request, 'base/profile.html')


def RegisterPage(request):
    form = CreateUserForm

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
    context = {'form':form}
    return render(request,'base/register.html', context)
# class RegisterPage(FormView):
#     template_name = 'base/register.html'
#     form_class = UserCreationForm
#     redirect_authenticated_user = True
#     success_url = reverse_lazy('users')

# class UserList(LoginRequiredMixin, ListView):
#     model = User
#     context_object_name = 'users'
#     template_name = 'base/admin.html'