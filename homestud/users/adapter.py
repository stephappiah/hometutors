from allauth.socialaccount.adapter import DefaultSocialAccountAdapter
from allauth.account.utils import perform_login, user_email, user_field, user_username
from allauth.socialaccount.signals import social_account_added
from .models import User


class MySocialAccountAdapter(DefaultSocialAccountAdapter):
    # adapter object checks if user already is signed up by quering the social email
    # if user exists,
    # it logs in
    # else
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
    
    def get_signup_form_initial_data(self, sociallogin):
        user = sociallogin.user
        initial = {
            'email': user_email(user) or '',
            'username': user_username(user) or '',
            'first_name': user_field(user, 'first_name') or '',
            'last_name': user_field(user, 'last_name') or '',
            'name': user_field(user, 'name') or ''}
        return initial


    def social_account_added(self, request, sociallogin):
        
        pass