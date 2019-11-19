from django.shortcuts import render
from django.http import HttpResponseRedirect, Http404
from django.urls import reverse
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import AnonymousUser

def logout_view(request):
    """Log the user out"""
    logout(request)
    return HttpResponseRedirect(reverse('pmt_act:index'))

def register(request):
    """Register s new user"""
    if request.user == AnonymousUser():
        if request.method != 'POST':
            #Display blank registration form.
            form = UserCreationForm()
        else:
            #Process completed form.
            form = UserCreationForm(data=request.POST)
            
            if form.is_valid():
                new_user=form.save()
                #Log the user in and then redirect to home page.
                authenticated_user = authenticate(username=new_user.username,
                    password=request.POST['password1'])
                login(request, authenticated_user)
                return HttpResponseRedirect(reverse('pmt_act:index'))
                
        context = {'form': form}
        return render(request, 'users/register.html', context)
    else:
        raise Http404
