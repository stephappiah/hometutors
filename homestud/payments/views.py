from django.shortcuts import render, redirect
from django.conf import settings
from django.http import HttpResponse, JsonResponse
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from pypaystack import Transaction, Customer, Plan
from datetime import timedelta, datetime
from dateutil.relativedelta import relativedelta

from .models import Subscription, UserTransaction

import json

# Paystack keys
public_key = settings.PAYSTACK_PUBLIC_KEY
secret_key = settings.PAYSTACK_SECRET_KEY

@login_required
def checkout(request):
    # to-do: check whenever url is visited to see if user has active subscription
    # if true, redirect; else continue
    current_user = request.user
    url = request.get_full_path()
    print(url)
    def subscriptionStatus():
        '''
            returns active or inactive status of user subscription
        '''
        try: 
            # user subscription exist in database
            user_subscription = Subscription.objects.get(user=current_user)

            expiry_date = user_subscription.expiry_date
            todays_date = datetime.today().date()
            # check if expiry date is up
            if todays_date > expiry_date:
                # subscription expired
                # return inactive status
                return 'inactive'
            else:
                # subscription active
                # return active
                return 'active'          
        except Subscription.DoesNotExist:
            # user subscription does not exist in database
            # user isn't subscribed!
            # return inactive status
            return 'inactive'

    if subscriptionStatus == 'inactive':
        email = request.user.email
        amount = 33
        print(email)
        print(request.path)

        context = {
            'pk_public': public_key,
            'email': email,
            'amount': amount
        }
        
        return render(request, 'payments/checkout.html', context)
    else:
        return redirect(request.GET.get('next'))   

@login_required
def verify_payment(request, id):
    
    # verify transaction
    transaction = Transaction(authorization_key=secret_key)
    response = transaction.verify(id)

    data = JsonResponse(response, safe=False)
    

    # save transaction to database if it returns 'success'
    status = response[3]['status']
    if status == 'success':

        user = request.user
        channel = response[3]['channel']
        amount = response[3]['amount']
        transaction_date = datetime.now()
        ref = response[3]['reference']

        print(transaction_date)

        # pass transaction details
        user_trans = UserTransaction()

        user_trans.user = user
        user_trans.channel = channel
        user_trans.amount = amount / 100 #divide by 100 since paystack multiplies amt by 100 at api level
        user_trans.date = transaction_date
        user_trans.reference = ref
        user_trans.status = status
        # save
        user_trans.save()

        # save subscription after transaction is saved
        
        # check if user subscription exist already; update if true, create new one if false
        if Subscription.objects.filter(user=user).exists():
            # subscription exists
            # update model
            subs_exits = Subscription.objects.get(user=user)

            subs_exits.start_date = transaction_date
            subs_exits.expiry_date = transaction_date + relativedelta(months=+1)

            subs_exits.save()
            # redirect
            #redirect(request.GET.get('next'))
        else:
            # save new model
            user_subscription = Subscription()

            user_subscription.user = user
            user_subscription.start_date = transaction_date
            user_subscription.expiry_date = transaction_date + relativedelta(months=+1)

            # save subscription
            user_subscription.save()
            # redirect
            #redirect(request.GET.get('next'))      
    else:
        pass
    
    return data
