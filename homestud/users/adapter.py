from allauth.socialaccount.adapter import DefaultSocialAccountAdapter
from allauth.account.utils import perform_login, user_email, user_field, user_username
from .models import User
from django.urls import reverse
from django.shortcuts import redirect

class MySocialAccountAdapter(DefaultSocialAccountAdapter):
    # adapter object checks if user already is signed up by quering the social email
    # if user exists,
    # it logs in
    # else pass
    def pre_social_login(self, request, sociallogin): 
        logged_user = sociallogin.user
        if logged_user.id:  
            return          
        try:
            user = User.objects.get(email=logged_user.email)  # if user exists, connect the account to the existing account and login
            sociallogin.state['process'] = 'connect'                
            perform_login(request, user, 'none')
        except User.DoesNotExist:
            pass
  
    def get_connect_redirect_url(self, request, socialaccount):
        """
        Returns the default URL to redirect to after successfully
        connecting a social account.
        """
        assert request.user.is_authenticated
        url = redirect('/') #my code
        # url = reverse('socialaccount_connections') #default
        return url