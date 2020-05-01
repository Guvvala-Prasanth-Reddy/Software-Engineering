from django import forms
from .models import content

class content_form(forms.ModelForm):
    class Meta:
        model = content
        fields = ['course_name' , 'semester' ,  'course_code' , 'content' , 'rating' , 'Notes' , 'Textbook' , 'QP'  ]
        widgets = {
            'course_name' : forms.HiddenInput(),
            'course_code' : forms.HiddenInput(),
            'semester'    : forms.HiddenInput(),
        }


