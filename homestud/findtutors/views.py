from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.conf import settings
from .forms import UserTypeForm

import os
from formtools.wizard.views import SessionWizardView
from django.core.files.storage import FileSystemStorage
from .forms import PersonInfoForm, EducationForm, TutorProfileForm, TutorInterestForm
from .models import Profile, Education, TutorProfile, TutorInterest
from django.forms.models import construct_instance


class OnboardingTutorWizard(SessionWizardView, LoginRequiredMixin):
    
    template_name = 'findtutors/onboard-tutor.html'

    def get_user_details(self):
        firstname = self.request.user.firstname
        lastname = self.request.user.firstname

        return lastname


    initial_dict = {
        '0': {
            'fname': 'firstname', 
            'lname': 'lastname'
            }
    }
    form_list = [PersonInfoForm, EducationForm, TutorProfileForm, TutorInterestForm, ] 
    file_storage = FileSystemStorage(location=os.path.join(settings.MEDIA_ROOT, 'photos'))

    def get_form_initial(self, step):
        initial = {}
        if step ==0:
            initial['fname'] = 'Stephen'
        return self.initial_dict.get(step, initial)

    def done(self, form_list, **kwargs):
        # instantiate form
        profile_instance = Profile()
        education_instance = Education()
        tutor_profile_instance = TutorProfile()
        tutor_interest_instance = TutorInterest()
        # Add signed-in user to form
        profile_instance.user = self.request.user
        education_instance.user = self.request.user 
        tutor_profile_instance.user = self.request.user 
        tutor_interest_instance.user = self.request.user

      

        for form in form_list:
            profile_instance = construct_instance(form, profile_instance, form._meta.fields, form._meta.exclude)
            education_instance = construct_instance(form, education_instance, form._meta.fields, form._meta.exclude)
            tutor_profile_instance = construct_instance(form, tutor_profile_instance, form._meta.fields, form._meta.exclude)
            tutor_interest_instance = construct_instance(form, tutor_interest_instance, form._meta.fields, form._meta.exclude)

            # save form instaces to database
            profile_instance.save()
            education_instance.save()
            tutor_profile_instance.save()
            tutor_interest_instance.save()
            
        return render(self.request, 'done.html', {
            'form_data': [form.cleaned_data for form in form_list],
        })

# ------ End of onboarding-tutor view ---------------------------------------------------

def home(request):
    return render(request, 'findtutors/home.html')

@login_required 
def onboarding_usertype(request):

    if request.method == 'POST':
        form = UserTypeForm(request.POST)
       
        current_user = request.user
        if form.is_valid():
            user_type_form = form.save(commit=False)
            user_type_form.user = request.user # silently fill in user field with the logged in user
            user_type_form.save()

            # Redirect url based on usertype
            if user_type_form.user_type == 'tutor':
                return HttpResponseRedirect(reverse('findtutors:onboarding_tutor'))
            else:
                return HttpResponseRedirect(reverse('findtutors:home'))
            
    else:
        form = UserTypeForm()
    return render(request, 'findtutors/onboard-user-type.html', {'form': form}) 


def tutor_profile_view(request, username):
    return render(request, 'findtutors/tutor-profile.html')
