from django import forms

from .models import Trainings_Workshops,Enroll_TW

class TWForm(forms.ModelForm):
    
    class Meta:
        model = Trainings_Workshops
        fields = '__all__'
        help_texts = {'registration_Begins':'(Use Format:YYYY-MM-DD HH:MM:SS)',
            'registration_Ends':'(Use Format:YYYY-MM-DD HH:MM:SS)',
            'event_Begins':'(Use Format:YYYY-MM-DD HH:MM:SS)'}
        initial = {'owner':'admin'}
        widgets = {'registration_Begins':forms.DateTimeInput(attrs={'class': 'datetime-input'}),
            'registration_Ends':forms.DateTimeInput(attrs={'class': 'datetime-input'}),
            'event_Begins':forms.DateTimeInput(attrs={'class': 'datetime-input'}),
            'valid': forms.HiddenInput(),'owner': forms.HiddenInput()}

class EnrollTWForm(forms.ModelForm):
    
    class Meta:
        model = Enroll_TW
        fields = '__all__'
        widgets = {'user_id': forms.HiddenInput(),
            'tw_id_id': forms.HiddenInput()}
