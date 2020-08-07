# from django import forms
from django.contrib.gis import forms
from .models import UserType, Profile, Education, TutorProfile, TutorInterest
from phonenumber_field.formfields import PhoneNumberField
from django.forms.widgets import CheckboxSelectMultiple
from .multi_choices import shs_choices



class DateInput(forms.DateInput):
    input_type ='date'

class PersonInfoForm(forms.ModelForm):
    contact = PhoneNumberField(required=False)

    class Meta:
        model = Profile
        fields = ('fname', 'lname', 'avatar', 'dob', 'contact', 'location', 'address', )
        
        labels = {
            'avatar': 'Profile Picture',
            'dob': 'Date of Birth',
            'contact': 'Contact',
            'address': 'Address',
            'fname': 'First name',
            'lname': 'Last name'
        }

        widgets = {
            'dob': DateInput(),
            'location': forms.OSMWidget(
                attrs={
                    'map_width': 800,
                    'map_height': 500,
                }
            )
        }

class EducationForm(forms.ModelForm):
    class Meta:
        model = Education
        fields = ('school', 'programme', 'start_year', 'end_year',)

class TutorProfileForm(forms.ModelForm):
    class Meta:
        model = TutorProfile
        exclude = ('user',)

class UserTypeForm(forms.ModelForm):

    USER_TYPE_CHOICES = (
        ('student', 'Student'),
        ('guardian', 'Guardian'),
        ('tutor', 'Tutor')
    )
    user_type = forms.CharField(label='User type', widget=forms.RadioSelect(choices=USER_TYPE_CHOICES))

    class Meta:
        model = UserType
        fields = ('user_type',)


class TutorInterestForm(forms.ModelForm):
    shs_programs = forms.CharField(label='SHS Programmes', widget=forms.RadioSelect(choices=shs_choices))
    class Meta:
        model = TutorInterest
        exclude = ('user',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['teach_levels'].widget.attrs.update({'class': 'myClass', })
        self.fields['primary_programs'].widget.attrs.update({'class': 'myClass', })
        self.fields['jhs_programs'].widget.attrs.update({'class': 'myClass', })
        self.fields['shs_programs'].widget.attrs.update({'class': 'd-none', })
        
        