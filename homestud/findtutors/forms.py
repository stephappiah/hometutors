# from django import forms
from django.contrib.gis import forms
from .models import TutorProfile
from phonenumber_field.formfields import PhoneNumberField
from django.forms.widgets import CheckboxSelectMultiple
from .multi_choices import highest_education_choices



class DateInput(forms.DateInput):
    input_type ='date'

class AvatarForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['avatar'].required = False
        self.fields['avatar'].widget.attrs.update({'class': 'avatar'})
        self.fields['avatar'].label = False

    class Meta: 
        model = TutorProfile
        fields = ('avatar',)


class PersonInfoForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['first_name'].required = True
        self.fields['last_name'].required = True
        self.fields['dob'].required = True
        self.fields['contact'].required = True
        self.fields['address'].required = True

    contact = PhoneNumberField()

    class Meta:
        model = TutorProfile
        fields = ('first_name', 'last_name', 'dob', 'contact', 'location', 'address', 'slug', )
        
        labels = {
            'dob': 'Date of Birth',
            'contact': 'Contact',
            'address': 'Address',
            'first_name': 'First name',
            'last_name': 'Last name',
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
        self.fields['rate_per_hour'].help_text = "How much (in GHC) will you charge for a one hour lesson?"
        self.fields['free_lesson_duration'].required = True
        self.fields['free_lesson_duration'].help_text = "The first lesson offered for free is a chance for you and your student to get to know each other."
        self.fields['bio'].required = True
        self.fields['bio'].widget.attrs['placeholder'] = 'I am an engineer/teacher/student...I have an experience in tutoring...I have a degree/certificate in...'
        self.fields['class_type'].widget.attrs.update({'class': 'chips_class_type'})
        self.fields['bio'].widget.attrs.update({'class': 'form-control'})

    class Meta:
        model = TutorProfile
        fields = ('class_type', 'rate_per_hour', 'free_lesson_duration', 'bio', )
        widgets = {
            'bio': forms.Textarea(attrs={'cols': '60', 'rows': '3'})
            
        }
        labels = {
            'bio': 'Write a catchy bio'
        }

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.fields['class_type'].widget.attrs.update({'class': 'chips_class_type'})
    #     self.fields['bio'].widget.attrs.update({'class': 'form-control'})


class TutorInterestForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['teach_levels'].required = True
        self.fields['tutoring_programs'].required = True
        self.fields['courses_subjects'].required = True
        self.fields['teach_levels'].widget.attrs.update({'class': 'chips_class_type', })
        self.fields['tutoring_programs'].widget.attrs.update({'class': 'chips_class_type programs', })
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