# from django import forms
from django.contrib.gis import forms
from .models import Profile, UserType
from phonenumber_field.formfields import PhoneNumberField
from django.forms.widgets import CheckboxSelectMultiple
from .multi_choices import highest_education_choices



class DateInput(forms.DateInput):
    input_type ='date'

class PersonInfoForm(forms.ModelForm):
    contact = PhoneNumberField(required=False)

    class Meta:
        model = Profile
        fields = ('avatar', 'fname', 'lname', 'dob', 'contact', 'location', 'address', 'slug' )
        
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
            'location': forms.HiddenInput(),
            'slug': forms.HiddenInput()
        }

class EducationForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ( 'highest_education', 'school', 'programme', 'start_year', 'end_year',)

        widgets = {
            'start_year': DateInput(),
            'end_year': DateInput(),
            'highest_education': forms.RadioSelect(choices=highest_education_choices)
        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['highest_education'].widget.attrs.update({'class': 'chips_class_type'})

class TutorProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('class_type', 'rate_per_hour', 'free_lesson_duration', 'bio', )
        widgets = {
            'bio': forms.Textarea(attrs={'cols': '60', 'rows': '3'})
            
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['class_type'].widget.attrs.update({'class': 'chips_class_type'})
        self.fields['bio'].widget.attrs.update({'class': 'form-control'})

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

        labels = {
            'courses_subjects': 'Courses'
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['teach_levels'].widget.attrs.update({'class': 'chips_class_type', })
        self.fields['tutoring_programs'].widget.attrs.update({'class': 'chips_class_type', })
        self.fields['courses_subjects'].widget.attrs.update({'class': 'chips_class_type', })

class UpdateTutorForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ('user', 'slug', )