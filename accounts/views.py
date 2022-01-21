from django.shortcuts import render, redirect
from .forms import EditProfile
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.decorators import login_required


# Create your views here.

class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

@login_required(login_url='/accounts/login/')
def profile(request):
    user = request.user
    return render(request, 'registration/profile.html', {'user': user})

@login_required(login_url='/accounts/login/')
def update_profile(request):
    editprofile = EditProfile
    user = request.user
    if request.method == 'POST':
        user.first_name = request.POST.get('first_name')
        user.last_name = request.POST.get('last_name')
        user.profile.bio = request.POST.get('bio')
        user.profile.location = request.POST.get('location')
        user.profile.birth_date = request.POST.get('birth_date')
        user.email = request.POST.get('email')
        user.save()
        return redirect('accounts:profile')
    return render(request, 'registration/update.html', {'user': user, 'editprofile': editprofile})
