from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect, Http404
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django import forms

from .models import Trainings_Workshops,Enroll_TW
from .forms import TWForm,EnrollTWForm

def index(request):
    """The home page for pmt_act"""
    return render(request,'pmt_act/index.html')
    
@login_required    
def trainings_workshops(request):
    """Show all trainings_workshops."""
    trainings_workshops=Trainings_Workshops.objects.order_by('date_added')
    context={'trainings_workshops':trainings_workshops} 
    return render(request,'pmt_act/trainings_workshops.html',context)

@login_required
def training_workshop(request,training_workshop_id):
    """Show about a single training_workshop"""
    detail=Trainings_Workshops.objects.get(id=training_workshop_id)
    context={'detail':detail} 
    return render(request,'pmt_act/training_workshop.html',context)

@login_required
def new_tw(request):
    """Add a new Training/Workshop"""
    if request.method != 'POST':
        #No data submitted so create a blank form
        form = TWForm()
    else:
        #POST data submitted so process data
        form=TWForm(request.POST,request.FILES)
        if form.is_valid():
            new_tw=form.save(commit=False)
            new_tw.owner=request.user
            new_tw.save()
            return HttpResponseRedirect(reverse('pmt_act:trainings_workshops'))
            
    context={'form':form}
    return render(request,'pmt_act/new_tw.html',context)

@login_required
def edit_tw(request,detail_id):
    """Edit an existing entry"""
    
    tw=Trainings_Workshops.objects.get(id=detail_id)
    if tw.owner != request.user:
        raise Http404
    if request.method != 'POST':
        #Inintially, the form is filled with current tw.
        form = TWForm(instance=tw)
    else:
        #POST data submitted so process data
        form=TWForm(request.POST, request.FILES, instance=tw)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('pmt_act:training_workshop',args=[detail_id]))
            
    context={'tw':tw,'form':form}
    return render(request,'pmt_act/edit_tw.html',context)
    
@login_required
def delete_tw(request,detail_id):
    """Delete an existing entry"""
    
    tw=Trainings_Workshops.objects.get(id=detail_id)
    
    if tw.owner != request.user:
        raise Http404
    
    if request.method == 'POST':
        if 'confirm' in request.POST:
            tw.delete()
            return HttpResponseRedirect(reverse('pmt_act:trainings_workshops'))
        
        elif 'cancel' in request.POST:
            return HttpResponseRedirect(reverse('pmt_act:training_workshop',args=[detail_id]))

    context={'tw':tw}
    return render(request,'pmt_act/delete_tw.html',context)

@login_required
def enroll_tw(request,detail_id):
    """Enroll an existing entry"""
    
    tw=Trainings_Workshops.objects.get(id=detail_id)
    if Enroll_TW.objects.filter(tw_id=detail_id,user_id=request.user).count()<1:
        enroll_tw=Enroll_TW.objects.create(tw_id=tw,user_id=request.user,enrolled=False)
    else:
        enroll_tw=Enroll_TW.objects.get(tw_id=detail_id,user_id=request.user)
    
    if request.method == 'POST':
        if 'confirmEn' in request.POST:
            enroll_tw=Enroll_TW.objects.filter(tw_id=tw,user_id=request.user).update(enrolled=True)
            form=EnrollTWForm(request.POST)
            if form.is_valid():
                form.save()
            return HttpResponseRedirect(reverse('pmt_act:trainings_workshops'))
                
        elif 'cancelEn' in request.POST:
            return HttpResponseRedirect(reverse('pmt_act:training_workshop',args=[detail_id]))
            
        elif 'goBack' in request.POST:
            return HttpResponseRedirect(reverse('pmt_act:trainings_workshops'))
            
    context={'tw':tw,'enroll_tw':enroll_tw}
    return render(request,'pmt_act/enroll_tw.html',context)
