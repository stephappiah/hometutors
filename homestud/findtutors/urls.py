from django.urls import path
from django.conf.urls import url
from . import views
from .views import OnboardingTutorWizard
from .forms import PersonInfoForm, EducationForm, TutorProfileForm

app_name = 'findtutors'

# initial = {
#     '0': {'fname': 'Stephen', 'lname': 'Appiah'}
# }

urlpatterns = [

    path('', views.home, name="home"),
    path("onboarding-usertype/", views.onboarding_usertype, name="onboarding_usertype"),
    path("tutor/<str:username>", views.tutor_profile_view, name="view_tutor_profile"),
    url(r'^onboarding-tutor/$', OnboardingTutorWizard.as_view(), name="onboarding_tutor"),

]
