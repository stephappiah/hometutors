# from django import forms
from django.contrib.gis import forms
from .models import TutorProfile, UserType
from phonenumber_field.formfields import PhoneNumberField
from django.forms.widgets import CheckboxSelectMultiple
from .multi_choices import highest_education_choices



class DateInput(forms.DateInput):
    input_type ='date'

class AvatarForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['avatar'].required = True

    class Meta: 
        model = TutorProfile
        fields = ('avatar',)
        labels = {
            'avatar': 'Profile Picture'
        }

class PersonInfoForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['fname'].required = True
        self.fields['lname'].required = True
        self.fields['dob'].required = True
        self.fields['contact'].required = True
        self.fields['address'].required = True

    contact = PhoneNumberField()

    class Meta:
        model = TutorProfile
        fields = ('fname', 'lname', 'dob', 'contact', 'location', 'address', 'slug', )
        
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
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['highest_education'].required = True
        self.fields['school'].required = True
        self.fields['programme'].required = True
        self.fields['start_year'].required = True
        self.fields['end_year'].required = True
        # self.fields['highest_education'].widget.attrs.update({'class': 'chips_class_type'})
        
    class Meta:
        model = TutorProfile
        fields = ( 'highest_education', 'school', 'programme', 'start_year', 'end_year',)

        widgets = {
            'start_year': DateInput(),
            'end_year': DateInput()
        }
   

class TutorProfileForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['class_type'].required = True
        self.fields['rate_per_hour'].required = True
        self.fields['free_lesson_duration'].required = True
        self.fields['bio'].required = True
        self.fields['class_type'].widget.attrs.update({'class': 'chips_class_type'})
        self.fields['bio'].widget.attrs.update({'class': 'form-control'})

    class Meta:
        model = TutorProfile
        fields = ('class_type', 'rate_per_hour', 'free_lesson_duration', 'bio', )
        widgets = {
            'bio': forms.Textarea(attrs={'cols': '60', 'rows': '3'})
            
        }

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.fields['class_type'].widget.attrs.update({'class': 'chips_class_type'})
    #     self.fields['bio'].widget.attrs.update({'class': 'form-control'})

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
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['teach_levels'].required = True
        self.fields['tutoring_programs'].required = True
        self.fields['courses_subjects'].required = True
        self.fields['teach_levels'].widget.attrs.update({'class': 'chips_class_type', })
        self.fields['tutoring_programs'].widget.attrs.update({'class': 'chips_class_type', })
        self.fields['courses_subjects'].widget.attrs.update({'class': 'chips_class_type', })

    class Meta:
        model = TutorProfile
        fields = ('teach_levels', 'tutoring_programs', 'courses_subjects', )

        labels = {
            'courses_subjects': 'Courses'
        }

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.fields['teach_levels'].widget.attrs.update({'class': 'chips_class_type', })
    #     self.fields['tutoring_programs'].widget.attrs.update({'class': 'chips_class_type', })
    #     self.fields['courses_subjects'].widget.attrs.update({'class': 'chips_class_type', })

class UpdateTutorForm(forms.ModelForm):
    class Meta:
        model = TutorProfile
        exclude = ('user', 'slug', 'location',) 