from django.shortcuts import (
    render,
    redirect,
    reverse,
    get_object_or_404,
    HttpResponse,
    )
from django.views.decorators.http import require_POST
from django.contrib import messages
from django.conf import settings
from datetime import timedelta

from .forms import UpgradeAccountForm
from .models import UpgradeOrder

from myprofile.models import Profile

import stripe
import json


# Cached Upgrade Order Data
@require_POST
def cache_upgrade_data(request):
    try:
        pid = request.POST.get('client_secret').split('_secret')[0]
        stripe.api_key = settings.STRIPE_SECRET_KEY
        stripe.PaymentIntent.modify(pid, metadata={
            'upgrade_order': json.dumps(request.session.get('upgrade_order')),
            'save_info': request.POST.get('save_info'),
            'username': request.user,
        })
        return HttpResponse(status=200)
    except Exception as e:
        messages.error(request, 'Sorry, your payment cannot be\
                        processed right now. Please try again later.')
        return HttpResponse(content=e, status=400)


# Upgrade Account
def upgrade_account(request):
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    if request.method == 'POST':

        upgrade_order_form = UpgradeAccountForm(request.POST)

        if upgrade_order_form.is_valid():
            order = upgrade_order_form.save()
            pid = request.POST.get('client_secret').split('_secret')[0]
            order.stripe_pid = pid
            order.save()
            request.session['upgrade_order'] = order.order_number
            return redirect(reverse('checkout_success',
                                    args=[order.order_number]))
        else:
            messages.error(request,
                           'There was an error with your form.\
                            Please double check your information.')
    else:
        upgrade_order_form = UpgradeAccountForm()

    if not stripe_public_key:
        messages.warning(request,
                         'Stripe public key is missing. Did you forget\
                              to set it in your environment?')

    # Create Stripe Intent
    total = settings.UPGRADE_COST
    stripe_total = round(total * 100)
    stripe.api_key = stripe_secret_key
    intent = stripe.PaymentIntent.create(
        amount=stripe_total,
        currency=settings.STRIPE_CURRENCY,
    )

    # Attempt to prefill the form with any info the user maintains
    # in their profile
    if request.user.is_authenticated:
        try:
            profile = Profile.objects.get(user=request.user)
            user = request.user
            firstname = user.first_name
            lastname = user.last_name
            full_name = f'{firstname} {lastname}'
            upgrade_order_form = UpgradeAccountForm(initial={
                'full_name': full_name,
                'email': profile.user.email,
                'phone_number': profile.phone,
            })
        except Profile.DoesNotExist:
            upgrade_order_form = UpgradeAccountForm()
    else:
        upgrade_order_form = UpgradeAccountForm()

    # Render Template and Context
    template = 'upgradeaccount/upgrade_account.html'
    context = {
        'upgrade_order_form': upgrade_order_form,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,
    }

    return render(request, template, context)


# Checkout Success
def upgrade_success(request, order_number):
    """
    Handle successful upgrade
    """
    save_info = request.session.get('save_info')
    order = get_object_or_404(UpgradeOrder, order_number=order_number)

    # Attach the user's profile to the order
    if request.user.is_authenticated:
        profile = Profile.objects.get(user=request.user)
        order.user_profile = profile
        order.save()

        # Save the user's info
        if save_info:
            profile_data = {
                'default_full_name': order.full_name,
                'default_email': order.email,
                'default_phone_number': order.phone_number,
            }
            user_profile_form = UpgradeAccountForm(
                profile_data,
                instance=profile)
            if user_profile_form.is_valid():
                user_profile_form.save()

        # Update the user's profile to premium
        profile.premium_user_account = True
        # If the user's premium account has expired, set the
        # expiry date to UPGRADE_TIME_DAYS from order date
        # Otherwise, add UPGRADE_TIME_DAYS to the existing expiry date
        if not profile.premium_expiry:
            profile.premium_expiry = order.date + timedelta(
                days=settings.UPGRADE_TIME_DAYS)
        else:
            profile.premium_expiry += timedelta(
                days=settings.UPGRADE_TIME_DAYS)

    messages.success(request, f'Order successfully processed! \
        Your order number is {order_number}. A confirmation \
        email will be sent to {order.email}.')

    if 'upgrade_order' in request.session:
        del request.session['upgrade_order']

    template = 'upgradeaccount/checkout_success.html'
    context = {
        'order': order,
    }

    return render(request, template, context)
