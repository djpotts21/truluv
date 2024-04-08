from django.shortcuts import render
from django.contrib import messages
from django.conf import settings
from datetime import timedelta

from .models import UpgradeOrder

from myprofile.models import Profile
from checkuserpremium.models import check_user_premium


# Upgrade Account
def upgrade_account(request):
    # Run premium user check
    check_user_premium(request)

    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    # Render Template and Context
    template = 'upgradeaccount/upgrade_account.html'
    context = {
        'stripe_public_key': stripe_public_key,
        'client_secret': stripe_secret_key,
    }

    return render(request, template, context)


# Checkout Success
def upgrade_success(request):
    # Run premium user check
    check_user_premium(request)

    """
    Handle successful upgrade
    """

    stripe_token = request.POST.get('stripeToken')
    order_total = request.POST.get('order_total')
    print(order_total)

    order_number = request.POST.get('order_number')

    # Get user data from stripe_email
    user = request.user
    full_name = user.first_name + ' ' + user.last_name
    profile = Profile.objects.get(user=user)
    phone_number = profile.phone

    # Create Order
    order = UpgradeOrder(
        full_name=full_name,
        email=user.email,
        phone_number=phone_number,
        total=order_total,
        stripe_pid=stripe_token,
    )
    order.save()

    # Update the user's profile to premium

    profile.premium_user_account = True
    profile.save()

    # Determin the plan type
    if order_total == "0.99":
        upgradedays = settings.PLAN1_DAYS
    elif order_total == "1.50":
        upgradedays = settings.PLAN2_DAYS
    else:
        upgradedays = 0

    # If the user's premium account has expired, set the
    # expiry date to UPGRADE_TIME_DAYS from order date
    # Otherwise, add UPGRADE_TIME_DAYS to the existing expiry date
    print(order.date)
    print(profile.premium_expiry)

    if profile.premium_expiry is None:
        newdate = order.date + timedelta(days=upgradedays)
        profile.premium_expiry = newdate
        print("Step 1")
    elif profile.premium_expiry > order.date:
        profile.premium_expiry += timedelta(days=upgradedays)
        print("Step 2")
    else:
        newdate = order.date + timedelta(days=upgradedays)
        profile.premium_expiry = newdate
        print("Step 3")
    profile.save()

    messages.success(request, f'Order successfully processed! \
        Your order number is {order_number}. A confirmation \
        email will be sent to {order.email}.')

    if 'upgrade_order' in request.session:
        del request.session['upgrade_order']

    template = 'upgradeaccount/upgrade_success.html'
    context = {
        'order': order,
    }

    return render(request, template, context)
