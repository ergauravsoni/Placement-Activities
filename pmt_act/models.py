from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import User

class Trainings_Workshops(models.Model):
    """New Trainings/Workshops where students can register."""
    
    class Meta:
        verbose_name='Training/Workshop'
        verbose_name_plural='Trainings/Workshops'
        
    name = models.CharField(max_length=200)
    date_added=models.DateTimeField(auto_now_add=True)
    banner = models.ImageField(upload_to = 'banners/',null=True,
    blank=True)
    
    registration_Begins=models.DateTimeField(blank=False,null=True)
    registration_Ends=models.DateTimeField(blank=False,null=True)
    event_Begins=models.DateTimeField(blank=False,null=True)
    event_Fee=models.DecimalField(max_digits=7,decimal_places=2,
        blank=False,null=True)
    event_URL=models.URLField(null=True,blank=True)
    additional_Details=models.TextField(null=True,blank=True)
    contact_Name=models.CharField(max_length=50,blank=False,null=True)
    contact_Email=models.EmailField(blank=False,null=True)
    contact_No=PhoneNumberField(blank=False,null=True,
        unique=False)
    document=models.FileField(upload_to='document/',blank=True,
        null=True)
    valid = models.BooleanField(default=False,blank=False)
    owner = models.ForeignKey(User,on_delete=models.CASCADE,blank=True,
        null=False,default=1)
    
    def __str__(self):
        """return a string representation of the model"""
        return self.name

class Enroll_TW(models.Model):
    """Enroll Trainings/Workshops where students can register."""
    
    tw_id = models.ForeignKey(Trainings_Workshops,on_delete=models.CASCADE,blank=False,
        null=False,unique=False)
    user_id = models.ForeignKey(User,on_delete=models.CASCADE,blank=False,
        null=False,unique=False)
    enrolled = models.BooleanField(default=True)
    
    class Meta:
        verbose_name_plural='Enroll_TW'
        unique_together = (('user_id', 'tw_id'),)
    
    def __str__(self):
        """return a string representation of the model"""
        return ("User: " + str(self.user_id) + " enrolled to " 
            + "Training/Workshop: " + str(self.tw_id))
