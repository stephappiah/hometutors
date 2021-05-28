from django.contrib.gis import forms
from .models import GroupClass
from bootstrap_datepicker_plus import TimePickerInput
from multiselectfield import MultiSelectField
from findtutors.courses import courses_choices

class DateInput(forms.DateInput):
    input_type ='date'

class GroupClassForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(GroupClassForm, self).__init__(*args, **kwargs)
        self.fields['subjects'].widget.attrs.update({'class': 'chips_class_type', })
        self.fields['programs'].widget.attrs.update({'class': 'chips_class_type programs', })
        self.fields['course_description'].widget.attrs.update({'class': 'form-control', })
        self.fields['address'].widget.attrs['placeholder'] = 'Town, City'
        self.fields['title'].widget.attrs['placeholder'] = 'Elective Maths for Final Year SHS'
        self.fields['course_description'].widget.attrs['placeholder'] = '...this is a special course to help final year wassce students to prepare...'
        self.fields['levels'].widget.attrs.update({'class': 'chips_class_type', })
        self.fields['title'].required = True
        self.fields['programs'].required = True
        self.fields['subjects'].required = True
        self.fields['levels'].required = True
        self.fields['course_description'].required = True
        self.fields['address'].required = True
        self.fields['start_date'].required = True
        self.fields['end_date'].required = True
        self.fields['start_time'].required = True
        self.fields['end_time'].required = True
        self.fields['total_seats'].required = True
        self.fields['price'].required = True


    class Meta:
        model = GroupClass
        exclude = ( 'tutor', 'available_seats', )
        
        widgets = {
            'start_date': DateInput(),
            'end_date': DateInput(),
            'location': forms.HiddenInput(),
            'end_time': TimePickerInput(),
            'start_time': TimePickerInput(),
            'course_description': forms.Textarea(attrs={'cols': '60', 'rows': '10'})
        }