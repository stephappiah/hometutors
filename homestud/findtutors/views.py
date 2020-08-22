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
from .forms import PersonInfoForm, EducationForm, TutorProfileForm, TutorInterestForm, UpdateTutorForm
from .models import Profile, UserType
from users.models import User
from django.forms.models import construct_instance


class OnboardingTutorWizard(SessionWizardView):
    
    template_name = 'findtutors/onboard-tutor.html'

    form_list = [PersonInfoForm, EducationForm, TutorProfileForm, TutorInterestForm, ] 
    file_storage = FileSystemStorage(location=os.path.join(settings.MEDIA_ROOT, 'photos'))

    # Prepopulate with user's first and last names
    def get_form_initial(self, step):
        initial = self.initial_dict.get(step, {})
        firstname = self.request.user.first_name
        lastname = self.request.user.last_name

        # algorithm generates slug(username, kinda) from first and lastname
        def generate_slug(firstname, lastname):
            slug = "{0}{1}".format(firstname[:2],lastname).lower()
            x=0
            while True:
                if x == 0 and Profile.objects.filter(slug=slug).count() == 0:
                    return slug
                else:
                    slug = "{0}{1}".format(slug,x)
                    if Profile.objects.filter(slug=slug).count() == 0:
                        return slug
                x += 1
                if x > 1000000:
                    raise Exception("Name is super popular!")
            return slug

        slug = generate_slug(firstname, lastname)

        initial.update({'fname': firstname, 'lname': lastname, 'slug': slug})
        return initial


    def done(self, form_list, **kwargs):
        # instantiate model and Add signed-in user to form
        profile_instance = Profile()
        profile_instance.user = self.request.user

        for form in form_list:
            profile_instance = construct_instance(form, profile_instance, form._meta.fields, form._meta.exclude)
            # save form instaces to database(model)
            profile_instance.save()

            # redirect to profile dashboard
        return HttpResponseRedirect(reverse('findtutors:dashboard_profile'))

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


def tutor_profile_detail(request, slug_username):
    
    qs = Profile.objects.get(slug=slug_username)
    context = {
        'tutor': qs,
    }
    return render(request, 'findtutors/tutor-profile.html', context)

def SearchTutor(request):

    #Get coordinates from search form in template
    latitude = float(request.GET.get('lat'))
    longitude = float(request.GET.get('lon'))

    # Store coordinates in user session
    request.session['lat'] = latitude 
    request.session['lon'] = longitude 

    user_location = Point(longitude, latitude, srid=4326)
    # Queryset filtered within a distance of 20km; annotated and orderd by distance
    dist = Distance('location', user_location)
    qs = Profile.objects.filter(location__distance_lte=(user_location, D(km=20))).annotate(distance=dist).order_by('distance')
    print(user_location)
    context = {
        'tutors': qs,
        'total_tutors': qs.count()
    }
    return render(request, 'findtutors/search-results.html', context)

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

@login_required 
def dashboard_profile(request):
    logged_in_user = request.user
    data = Profile.objects.get(user=logged_in_user)
    form = UpdateTutorForm(instance=data)

    if request.method == 'POST':
        form = UpdateTutorForm(request.POST, instance=data)
        if form.is_valid():
            form.save()
    context = {
        'form': form
    }
    return render(request, 'findtutors/profile-dashboard.html', context)