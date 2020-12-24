from allauth.account.forms import SignupForm
from allauth.socialaccount.forms import SignupForm
from django import forms
# from homestud.users.models import User

class CustomSignupForm(SignupForm):
    name = forms.CharField(max_length=30, label='Name')
    field_order =['name', 'email']
       
    def save(self, request):
        user = super(CustomSignupForm, self).save(request)

        user.name = self.cleaned_data['name']

        user.save()
        return user


class CustomSocialSignupForm(SignupForm):
    name = forms.CharField(max_length=30, label='Name')
    field_order =['name', 'email']

    def save(self, request):
        # Ensure you call the parent class's save.
        # .save() returns a User object.
        user = super(CustomSocialSignupForm, self).save(request)
        
        # Add your own processing here.
        user.name = self.socialaccount
        user.save()

        return user