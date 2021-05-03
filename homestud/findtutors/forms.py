# from django import forms
from django.contrib.gis import forms
from .models import TutorProfile, TutorReview, UserProfile
from phonenumber_field.formfields import PhoneNumberField
from django.forms.widgets import CheckboxSelectMultiple
from .multi_choices import highest_education_choices



class DateInput(forms.DateInput):
    input_type ='date'

class AvatarForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['avatar'].required = False #required set to false to allow form to be submitted without image field, thus making it possible to compress and submit image via xhr
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
        self.fields['address'].required = True
        self.fields['location'].required = True
        self.fields['address'].widget.attrs['placeholder'] = 'Town, City'
        self.fields['address'].help_text = 'Select a location from the autocomplete as you type to continue.'
        self.fields['location'].error_messages.update({
            'required': 'Please wait for places autocomplete to show up as you type and select your address.',
        })

    class Meta:
        model = TutorProfile
        fields = ('first_name', 'last_name', 'dob', 'location', 'address', 'slug', )
        
        labels = {
            'dob': 'Date of Birth',
            'address': 'Your current location',
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
        self.fields['bio'].widget.attrs['placeholder'] = 'I am an engineer/teacher/student/artist...I have an experience in tutoring...I have a degree/certificate in...My philosophies/values are...'
        self.fields['class_type'].widget.attrs.update({'class': 'chips_class_type'})
        self.fields['bio'].widget.attrs.update({'class': 'form-control'})
        self.fields['rate_per_hour'].widget.attrs['placeholder'] = 'Avg. hourly rate: GHS 10'

    class Meta:
        model = TutorProfile
        fields = ('class_type', 'rate_per_hour', 'negotiable', 'free_lesson_duration', 'bio', )
        widgets = {
            'bio': forms.Textarea(attrs={'cols': '60', 'rows': '10'})
            
        }
        labels = {
            'bio': 'Write a catchy bio',
            'negotiable': 'Negotiable?'
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
        widgets = {
            'bio': forms.Textarea(attrs={'cols': '60', 'rows': '10'})
            
    }

class UserProfileForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['user_type'].widget.attrs.update({'class': 'chips_class_type', })
        self.fields['avatar'].required = False #required set to false to allow form to be submitted without image field, thus making it possible to compress and submit image via xhr
        self.fields['avatar'].widget.attrs.update({'class': 'avatar'})
        self.fields['avatar'].label = False
        self.fields['address'].widget.attrs['placeholder'] = 'Town, City'
        
    class Meta:
        model = UserProfile
        fields = ('avatar', 'first_name', 'last_name', 'dob', 'location', 'address', 'user_type',)
        
        labels = {
            'dob': 'Date of Birth',
            'address': 'Your current location',
            'first_name': 'First name',
            'last_name': 'Last name',
            'user_type': 'Which one are you?'
        }

        widgets = {
            'dob': DateInput(),
            'location': forms.HiddenInput(),
        }


class TutorAdminForm(forms.ModelForm):
    class Meta:
        model = TutorProfile
        fields = ('__all__')
        widgets = {
            'bio': forms.Textarea(attrs={'cols': '60', 'rows': '10'})
        }
