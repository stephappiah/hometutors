from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from django.contrib.gis.db.models.functions import Distance
from django.contrib.gis.geos import fromstr, Point
from django.contrib.gis.measure import D
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.conf import settings
from .forms import UserTypeForm

import os
from formtools.wizard.views import SessionWizardView
from django.core.files.storage import FileSystemStorage
from .forms import PersonInfoForm, EducationForm, TutorProfileForm, TutorInterestForm
from .models import Profile, UserType
from django.forms.models import construct_instance


class OnboardingTutorWizard(SessionWizardView, LoginRequiredMixin):
    
    template_name = 'findtutors/onboard-tutor.html'

    form_list = [PersonInfoForm, EducationForm, TutorProfileForm, TutorInterestForm, ] 
    file_storage = FileSystemStorage(location=os.path.join(settings.MEDIA_ROOT, 'photos'))

    # Prepopulate with user's first and last names
    def get_form_initial(self, step):
        initial = self.initial_dict.get(step, {})
        firstname = self.request.user.first_name
        lastname = self.request.user.last_name
        initial.update({'fname': firstname, 'lname': lastname})
        return initial

    def done(self, form_list, **kwargs):
        # instantiate model and Add signed-in user to form
        profile_instance = Profile()
        profile_instance.user = self.request.user

        for form in form_list:
            profile_instance = construct_instance(form, profile_instance, form._meta.fields, form._meta.exclude)
            # save form instaces to database(model)
            profile_instance.save()
   
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


def tutor_profile_detail(request, username):
    return render(request, 'findtutors/tutor-profile.html')

class SearchTutor(ListView):
    template_name = 'findtutors/search-results.html'
    model = Profile
    context_object_name = 'tutors'

    def get_queryset(self):
        #Get coordinates from search form in template
        latitude = float(self.request.GET['lat'])
        longitude = float(self.request.GET['lon'])

        # Store coordinates in user session
        self.request.session['lat'] = latitude 
        self.request.session['lon'] = longitude 

        user_location = Point(longitude, latitude, srid=4326)
        # Queryset filtered within a distance of 20km; annotated and orderd by distance
        dist = Distance('location', user_location)
        qs = Profile.objects.filter(location__distance_lte=(user_location, D(km=20))).annotate(distance=dist).order_by('distance')
        return qs

def FilterSearch(request):
    # coordinates from session
    latitude = request.session['lat']
    longitude = request.session['lon']
    user_location = Point(longitude, latitude, srid=4326)
    # Queryset filtered within a distance of 20km; annotated and orderd by distance
    dist = Distance('location', user_location)
    qs = Profile.objects.filter(location__distance_lte=(user_location, D(km=20))).annotate(distance=dist).order_by('distance')
    # Grab search fields
    programme = request.GET.get('programme')
    course = request.GET.get('course')
    
    if programme != '' and programme is not None:
        qs = qs.filter(tutoring_programs__icontains=programme)

    if course != '' and course is not None:
        qs = qs.filter(courses_subjects__icontains=course)

    context = {
        'tutors': qs
    }
    return render(request, 'findtutors/search-results.html', context)