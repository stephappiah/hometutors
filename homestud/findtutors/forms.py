# from django import forms
from django.contrib.gis import forms
from .models import Profile, UserType
from phonenumber_field.formfields import PhoneNumberField
from django.forms.widgets import CheckboxSelectMultiple



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
            'location': forms.HiddenInput()
        }

class EducationForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('school', 'programme', 'start_year', 'end_year',)

class TutorProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('bio', 'highest_education', 'class_type', 'rate_per_hour', 'free_lesson_duration',)

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

    class Meta:
        model = Profile
        fields = ('teach_levels', 'tutoring_programs', 'courses_subjects', )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['teach_levels'].widget.attrs.update({'class': 'myClass', })
        self.fields['tutoring_programs'].widget.attrs.update({'class': 'myClass', })
        self.fields['courses_subjects'].widget.attrs.update({'class': 'myClass', })
        