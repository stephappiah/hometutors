from allauth.account.forms import SignupForm
from django import forms
# from homestud.users.models import User

class CustomSignupForm(SignupForm):
    first_name = forms.CharField(max_length=30, label='First Name') 
    last_name = forms.CharField(max_length=30, label='Last Name')
    field_order =['first_name', 'last_name', 'email']

   

    def save(self, request):
        user = super(CustomSignupForm, self).save(request)

        user.first_name = self.cleaned_data['first_name'] 
        user.last_name = self.cleaned_data['last_name']

        user.save()
        return user

# class UserType(forms):

#     USER_TYPE_CHOICES = (
#         ('student', 'student'),
#         ('guardian', 'guardian'),
#         ('tutor', 'tutor')
#     )
#     user_type = forms.CharField(label='', widget=forms.RadioSelect(choices=USER_TYPE_CHOICES))
