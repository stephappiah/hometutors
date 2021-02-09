from allauth.account.forms import SignupForm
from allauth.socialaccount.forms import SignupForm as SignupSocialForm
from django import forms
from phonenumber_field.formfields import PhoneNumberField
# from homestud.users.models import User

class CustomSignupForm(SignupForm):
    first_name = forms.CharField(max_length=30, label='First name')
    last_name = forms.CharField(max_length=30, label='Last name')
    contact = PhoneNumberField()
    field_order =['first_name', 'last_name', 'email', 'contact']
       
    def save(self, request):
        user = super(CustomSignupForm, self).save(request)

        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.contact = self.cleaned_data['contact']

        user.save()
        return user


class CustomSocialSignupForm(SignupSocialForm):
    first_name = forms.CharField(max_length=30, label='Firstname')
    last_name = forms.CharField(max_length=30, label='Lastname')
    field_order =['first_name', 'last_name', 'email']

    def save(self, request):
        # Ensure you call the parent class's save.
        # .save() returns a User object.
        user = super(CustomSocialSignupForm, self).save(request)
        
        # Add your own processing here.
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.save()

        return user