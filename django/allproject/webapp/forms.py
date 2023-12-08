from webapp.models import registeruser
from django.forms import ModelForm

class Form1(ModelForm):
    class Meta:
        model=registeruser
        fields=['uname','uemail','unum','upass','upass1']
        labels={'uname':'User Name', 'uemail':'User Email','unum':'Number','upass':'Password','upass1':'Retype Password'}
