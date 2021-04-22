from payments.models import Subscription
from findtutors.models import TutorProfile
from datetime import timedelta, datetime
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import redirect

def subcribed_user(function):
    def wrap(request, *args, **kwargs):
        current_user = request.user
        subscription_url = reverse('payment:checkout')
        #next_url = request.path
        next_url = request.get_full_path()

        if current_user.is_anonymous is False:
            # check if user object exists in database
            try:
                # user subscription exist in database
                user_subscription = Subscription.objects.get(user=current_user)

                expiry_date = user_subscription.expiry_date
                todays_date = datetime.today().date()

                # check if expiry date is up
                if todays_date > expiry_date:
                    # subscription expired
                    # redirect to checkout page
                    return redirect('/pay/?next=%s' % next_url)
                else:
                    # subscription active
                    # go ahead to view function
                    return function(request, *args, **kwargs)
                    
            except Subscription.DoesNotExist:
                # user subscription does not exist in database
                # user isn't subscribed!
                # redirect to checkout page
                return redirect('/pay/?next=%s' % next_url)

        
    wrap.__doc__ = function.__doc__
    wrap.__name__ = function.__name__
    return wrap


def check_user_type(function):
    '''
        decorator checks if user is_tutor;
        redirects to tutor dashboard if true;
        else redirect to user profile
    '''
    def wrap(request, *args, **kwargs):
        current_user = request.user
        tutor_dashboard = reverse('findtutors:dashboard_profile')
        if current_user.is_anonymous is False:
            try:
                TutorProfile.objects.get(user=current_user)
                # user has tutor profile
                # redirect to tutor dashboard
                return redirect(tutor_dashboard)
            except TutorProfile.DoesNotExist:
                # user isn't tutor
                # go ahead with view (user profile view)
                return function(request, *args, **kwargs)
        else:
            # user is anonymous
            pass
    

    wrap.__doc__ = function.__doc__
    wrap.__name__ = function.__name__
    return wrap