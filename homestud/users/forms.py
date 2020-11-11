from allauth.account.forms import SignupForm
from django import forms
# from homestud.users.models import User

class CustomSignupForm(SignupForm):
    fullname = forms.CharField(max_length=30, label='Name')
    field_order =['fullname', 'email']

   

    def save(self, request):
        user = super(CustomSignupForm, self).save(request)

        user.fullname = self.cleaned_data['fullname']

        user.save()
        return user
