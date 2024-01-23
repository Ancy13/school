from django import forms
from schoolstore.school_app.models import School



class DetailForm(forms.ModelForm):
    class Meta:
        model=School
        fields=['name','dob','age','gender','phone_number','email','address','district','branch','account_type','materials_required']