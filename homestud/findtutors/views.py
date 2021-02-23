from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from django.contrib.gis.db.models.functions import Distance
from django.contrib.gis.geos import fromstr, Point
from django.contrib.gis.measure import D
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.conf import settings
from users.models import User
from PIL import Image
from io import StringIO

import os
from formtools.wizard.views import SessionWizardView
from django.core.files.storage import FileSystemStorage
from .forms import PersonInfoForm, EducationForm, TutorProfileForm, TutorInterestForm, UpdateTutorForm, AvatarForm
from .models import TutorProfile
from django.forms.models import construct_instance
from django.core.paginator import Paginator
from .courses import courses_choices, programmes_choices
import json 

from homestud.decorators import subcribed_user

class OnboardingTutorWizard(SessionWizardView):

    # checks if user has already filled forms; 
    # redirects to dashboard if true.
    # else proceed to onboarding
    def dispatch(self, request, *args, **kwargs):
        logged_in_user = self.request.user

        if TutorProfile.objects.filter(user=logged_in_user).exists():

            return HttpResponseRedirect(reverse('findtutors:dashboard_profile'))
        else:
            return super(OnboardingTutorWizard, self).dispatch(request, *args, **kwargs)

        

    template_name = 'findtutors/onboard-tutor.html'
    
    form_list = [PersonInfoForm, EducationForm, TutorProfileForm, TutorInterestForm, AvatarForm] 
    file_storage = FileSystemStorage(location=os.path.join(settings.MEDIA_ROOT, 'avatar'))

    # this function returns user to current step in the form they left off at
    def get(self, request, *args, **kwargs):
        try:
            return self.render(self.get_form())
        except KeyError:
            return super().get(request, *args, **kwargs)

    # Prepopulate with user's first and last names
    def get_form_initial(self, step):
        initial = self.initial_dict.get(step, {})
        fullname = self.request.user.get_full_name()
        first_name = self.request.user.first_name
        last_name = self.request.user.last_name

        # algorithm generates slug(username, kinda) from first and lastname
        def generate_slug(fullname):
            firstname = fullname.split()[0]
            lastname = fullname.split()[-1]
            slug = "{0}{1}".format(firstname[:2],lastname).lower()
            x=0
            while True:
                if x == 0 and TutorProfile.objects.filter(slug=slug).count() == 0:
                    return slug
                else:
                    slug = "{0}{1}".format(slug,x)
                    if TutorProfile.objects.filter(slug=slug).count() == 0:
                        return slug
                x += 1
                if x > 1000000:
                    raise Exception("Name is super popular!")
            return slug

        slug = generate_slug(fullname)

        initial.update({'first_name': first_name, 'last_name': last_name, 'slug': slug})
        return initial


    def done(self, form_list, form_dict, **kwargs):
        # instantiate model and Add signed-in user to form
        profile_instance = TutorProfile()
        profile_instance.user = self.request.user
        profile_instance.avatar = self.request.FILES['compressedImage']
        print(self.request.FILES['compressedImage'])

        for form in form_list:
            profile_instance = construct_instance(form, profile_instance, form._meta.fields, form._meta.exclude)

            # print(form.cleaned_data)
            # print(self.request.FILES['compressedImage'])
            form.cleaned_data['avatar'] = self.request.FILES['compressedImage']
            # save form instaces to database(model)
            profile_instance.save()

            #update is_tutor on user.User model to true
            user_email = self.request.user.email
            user_model = User.objects.get(email=user_email)
            user_model.is_tutor = True
            user_model.save()


            # redirect users to share site on social media
        return HttpResponseRedirect(reverse('findtutors:share_profile'))

# ------ End of onboarding-tutor view ---------------------------------------------------
@login_required
# @subcribed_user
def home(request):
    
    return render(request, 'findtutors/home.html')

def share_profile(request):
    return render(request, 'findtutors/tutor-share.html')

def tutor_profile_detail(request, slug_username):
    
    # qs = TutorProfile.objects.get(slug=slug_username)
    qs = get_object_or_404(TutorProfile, slug=slug_username)
    context = {
        'tutor': qs,
    }
    return render(request, 'findtutors/tutor-profile.html', context)

def SearchTutor(request):

    programme_list = json.dumps(dict(programmes_choices))
    course_list = json.dumps(dict(courses_choices))

    #Get coordinates from search form in template
    lat = request.GET.get('lat')
    lon = request.GET.get('lon')
   
    # Check if latitude and longitude fields are not empty
    if lat != '' or lon != '':
        #when pagination is >1, lat and lon returns none. This if checks that and returns lat and lon from SESSION
        if lat is None or lon is None:
            latitude = request.session['lat']
            longitude = request.session['lon']

            user_location = Point(longitude, latitude, srid=4326)
            # Queryset filtered within a distance of 100km; annotated and orderd by distance
            dist = Distance('location', user_location)
            qs = TutorProfile.objects.filter(location__distance_lte=(user_location, D(km=100))).annotate(distance=dist).order_by('distance')
            paginator = Paginator(qs, 10) #show 10 tutors per page

            page_number = request.GET.get('page')
            page_obj = paginator.get_page(page_number)

            
            context = {
                'tutors': page_obj,
                'total_tutors': qs.count(),
                'programme_list': programme_list,
                'course_list': course_list
            }
            return render(request, 'findtutors/search-results.html', context)
        else:
            latitude = float(lat)
            longitude = float(lon)
            # Store coordinates in user session
            request.session['lat'] = latitude 
            request.session['lon'] = longitude 

            
            user_location = Point(longitude, latitude, srid=4326)
            # Queryset filtered within a distance of 100km; annotated and orderd by distance
            dist = Distance('location', user_location)
            qs = TutorProfile.objects.filter(location__distance_lte=(user_location, D(km=100))).annotate(distance=dist).order_by('distance')
            paginator = Paginator(qs, 10) #show 10 tutors per page

            page_number = request.GET.get('page')
            page_obj = paginator.get_page(page_number)

            
            context = {
                'tutors': page_obj,
                'total_tutors': qs.count(),
                'programme_list': programme_list,
                'course_list': course_list
            }
            return render(request, 'findtutors/search-results.html', context)

    # return an error message if latitude and longitude fields are empty
    else:
        errorMessage = "Please wait for places to show up as you type or click on 'SEARCH NEAR ME' below to use your current location."
        message = {
            'errCoord': errorMessage
        }
        return render(request, 'findtutors/home.html', message)

def FilterSearch(request):
    #for dropdown
    programme_list = json.dumps(dict(programmes_choices))
    course_list = json.dumps(dict(courses_choices))

    # check if search form has coordinates
    # else use coordinates from session
    def get_latitude():
        if request.GET.get('latitude') is not None or '':
            # coordinates from search form
            latitude = request.GET.get('latitude')
            return latitude
        else:
            # coordinates from session
            latitude = request.session['lat']
            return latitude

    def get_longitude():
        if request.GET.get('longitude') is not None or '':
            # coordinates from search form
            longitude = request.GET.get('longitude')
            return longitude
        else:
            # coordinates from session
            longitude = request.session['lon']
            return longitude
    
    # get coordinates
    longitude = float(get_longitude())
    latitude = float(get_latitude())
    print(longitude, latitude)
    user_location = Point(longitude, latitude, srid=4326)
    # Queryset filtered within a distance of 100km; annotated and orderd by distance
    dist = Distance('location', user_location)
    qs = TutorProfile.objects.filter(location__distance_lte=(user_location, D(km=100))).annotate(distance=dist).order_by('distance')

    # Grab search fields
    programme = request.GET.get('programme')
    course = request.GET.get('course')
    
    if programme != '' and programme is not None:
        qs = qs.filter(tutoring_programs__icontains=programme)

    if course != '' and course is not None:
        qs = qs.filter(courses_subjects__icontains=course)

    paginator = Paginator(qs, 10) #show 10 tutors per page

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
                'tutors': page_obj,
                'total_tutors': qs.count(),
                'programme_list': programme_list,
                'course_list': course_list
    }
    return render(request, 'findtutors/search-results.html', context)

@login_required 
def dashboard_profile(request):
    logged_in_user = request.user
    # raise html404 when obj not found
    data = get_object_or_404(TutorProfile, user=logged_in_user)
   
    # PersonalForm = PersonInfoForm(instance=data) 
    # EducationalForm = EducationForm(instance=data) 
    # ProfileForm = TutorProfileForm(instance=data, auto_id='id-2_%s') 
    # InterestForm = TutorInterestForm(instance=data)

    if request.method == 'POST':
        if 'personal_info' in request.POST:
            PersonalForm = PersonInfoForm(request.POST, prefix='personal_info', instance=data)
            if PersonalForm.is_valid():
                PersonalForm.save()

            EducationalForm = EducationForm(instance=data, prefix='education') 
            ProfileForm = TutorProfileForm(instance=data, prefix='tutor_profile') 
            InterestForm = TutorInterestForm(instance=data, prefix='interest')
            AvtForm = AvatarForm(instance=data, prefix='avatar')

        elif 'education' in request.POST:
            EducationalForm = EducationForm(request.POST, prefix='education', instance=data)
            if EducationalForm.is_valid():
                EducationalForm.save()

            PersonalForm = PersonInfoForm(instance=data, prefix='personal_info') 
            ProfileForm = TutorProfileForm(instance=data, prefix='tutor_profile') 
            InterestForm = TutorInterestForm(instance=data, prefix='interest')
            AvtForm = AvatarForm(instance=data, prefix='avatar')

        elif 'tutor_profile' in request.POST:
            ProfileForm = TutorProfileForm(request.POST, prefix='tutor_profile', instance=data)
            if ProfileForm.is_valid():
                ProfileForm.save()

            PersonalForm = PersonInfoForm(instance=data, prefix='personal_info') 
            EducationalForm = EducationForm(instance=data, prefix='education') 
            InterestForm = TutorInterestForm(instance=data, prefix='interest')
            AvtForm = AvatarForm(instance=data, prefix='avatar')

        elif 'interest' in request.POST:
            InterestForm = TutorInterestForm(request.POST, prefix='interest', instance=data)
            if InterestForm.is_valid():
                InterestForm.save()

            PersonalForm = PersonInfoForm(instance=data, prefix='personal_info') 
            EducationalForm = EducationForm(instance=data, prefix='education') 
            ProfileForm = TutorProfileForm(instance=data, prefix='tutor_profile') 
            AvtForm = AvatarForm(instance=data, prefix='avatar')

        elif 'avatar' or '' in request.POST:
            AvtForm = AvatarForm(request.POST, prefix='avatar', instance=data)
            if AvtForm.is_valid():
                AvtForm.save()

                if request.FILES.get('compressedImage', None) != None:
                    try:
                        os.remove(data.avatar.url)
                    except Exception as e:
                        #print(data.avatar.url)
                        print('Exception in removing old profile image: ', e)
                    img = request.FILES['compressedImage']
                    data.avatar = img
                    data.save()

            PersonalForm = PersonInfoForm(instance=data, prefix='personal_info') 
            EducationalForm = EducationForm(instance=data, prefix='education') 
            ProfileForm = TutorProfileForm(instance=data, prefix='tutor_profile') 
            InterestForm = TutorInterestForm(instance=data, prefix='interest')

    else:
        PersonalForm = PersonInfoForm(instance=data, prefix='personal_info') 
        EducationalForm = EducationForm(instance=data, prefix='education') 
        ProfileForm = TutorProfileForm(instance=data, prefix='tutor_profile') 
        InterestForm = TutorInterestForm(instance=data, prefix='interest')
        AvtForm = AvatarForm(instance=data, prefix='avatar')

        

    
    context = {
        'PersonalForm': PersonalForm,
        'EducationalForm': EducationalForm,
        'ProfileForm': ProfileForm,
        'InterestForm': InterestForm,
        'AvatarForm': AvtForm,
        'userAvatarLink': data.avatar.url,
    }
    return render(request, 'findtutors/profile-dashboard.html', context)

def cities(request):

    return render(request, 'findtutors/cities.html')

def privacyPolicy(request):

    return render(request, 'findtutors/privacy.html')

def termsNCondition(request):

    return render(request, 'findtutors/terms.html')


@login_required
#@subcribed_user
def bookClass(request):
    
    return redirect()