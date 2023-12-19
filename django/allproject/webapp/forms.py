from webapp.models import registeruser
from django import forms

class Form1(forms.ModelForm):
    class Meta:
        model=registeruser
        fields=['uname','uemail','unum','upass']
        labels={'uname':'User Name', 'uemail':'User Email','unum':'Number','upass':'Password'}

class Form2(forms.Form):
    uemail=forms.CharField(max_length=32, label='Email')
    upass=forms.CharField(max_length=32,label='Password')