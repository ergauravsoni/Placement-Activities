"""Define URL Patterns for pmt_act"""

from django.urls import path

from . import views

urlpatterns = [
    #Home Page
    path('',views.index,name='index'),
    
    #page for viewing all trainings/workshops
    path('trainings_workshops/',views.trainings_workshops,
        name='trainings_workshops'),

    #page for viewing details of a single training/workshop
    path('trainings_workshops/<int:training_workshop_id>/',
        views.training_workshop,name='training_workshop'),
    
    #page for adding a new training/workshop
    path('new_tw/',views.new_tw, name='new_tw'),
    
    #page for editing a training/workshop
    path('edit_tw/<int:detail_id>/',
        views.edit_tw,name='edit_tw'),
        
    #page for deleting a training/workshop
    path('delete_tw/<int:detail_id>/',
        views.delete_tw,name='delete_tw'),

    #page for enrolling a training/workshop
    path('enroll_tw/<int:detail_id>/',
        views.enroll_tw,name='enroll_tw'),
]
