from django.urls import path
from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from . import views
from .views import OnboardingTutorWizard, SearchTutor, FilterSearch, dashboard_profile, share_profile, cities, privacyPolicy, termsNCondition
from .forms import PersonInfoForm, EducationForm, TutorProfileForm

app_name = 'findtutors'

urlpatterns = [

    path('', views.home, name="home"),
    path("tutor/<str:slug_username>", views.tutor_profile_detail, name="view_tutor_profile"),
    url(r'^onboarding-tutor/$', login_required(OnboardingTutorWizard.as_view(), login_url='account_signup'), name="onboarding_tutor"),
    path("search/", SearchTutor, name="search"),
    path('filter/', FilterSearch, name='filter'),
    path('dashboard/profile', dashboard_profile, name='dashboard_profile'),
    path('share-profile/', share_profile, name='share_profile'),
    path('cities/', cities, name='cities'),
    path('privacy-policy/', privacyPolicy, name='privacy'),
    path('terms-and-conditions/', termsNCondition, name='terms'),

]
