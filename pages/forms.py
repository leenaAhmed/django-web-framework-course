from django import forms
from .models import Contact
SEMESTER_CHOICES = ( 
    ("1", "Civil"), 
    ("2", "Electrical"), 
    ("3", "Mechanical"), 
    ("4", "CompSci"), 
) 

genderList = [
        ('male' , 'Male'),
        ('female' , 'Female'),
    ]


# 1
# class ContactForm(forms.Form):
#     FullName = forms.CharField(label="Full Name", initial="Enter your name")
#     email = forms.EmailField(required=False, label="Email" , initial="Enter your email address")
#     message = forms.CharField(required=False,
#                                widget=forms.Textarea(attrs={'row':5}),
#                                label="Message" , initial="Enter your message")
#     created_at = forms.DateField(widget= forms.NumberInput(attrs={'type':  'date'}))
#     # gender = forms.ChoiceField(choices=genderList, widget=forms.RadioSelect);


# 2 

class ContactForm(forms.ModelForm):
    class Meta:
          model = Contact
          fields = '__all__'
            


# class UserForm(forms.Form):
#     gender = forms.ChoiceField(choices=genderList, widget=forms.RadioSelect);
#     profession = forms.ChoiceField(choices=SEMESTER_CHOICES) 
 