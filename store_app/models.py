from django.db import models
from django import forms
# Create your models here.
class RegistrationForm(models.Model):
    name = forms.CharField()
    dob = forms.DateField()
    age = forms.IntegerField()
    gender = forms.ChoiceField(choices=[('male','Male'), ('female', 'Female'), ('transgender', 'Transgender')])
    phone_number = forms.CharField()
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    address = forms.CharField(widget=forms.Textarea)
    district = forms.ChoiceField(choices=[('thrissur', 'Thrissur'), ('ernamkulam', 'Ernamkulam'), ('palakkad', 'Palakkad'), ('kottayam', 'Kottayam'), ('trivandrum', 'Trivandrum')])
    branch = forms.ChoiceField()
    account_type = forms.ChoiceField(choices=[('savings', 'Savings'), ('current', 'Current')])
    materials_required = forms.MultipleChoiceField(choices=[('debit',' Debit Card'), ('credit', 'Credit Card'), ('cheque', 'Chequebook')], widget=forms.CheckboxSelectMultiple)

    def __str__(self):
        return self.name