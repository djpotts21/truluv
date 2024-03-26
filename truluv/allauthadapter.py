from allauth.account.adapter import DefaultAccountAdapter
from django.conf import settings
from django.shortcuts import resolve_url
from datetime import datetime, timedelta


class AccountAdapter(DefaultAccountAdapter):

  def get_login_redirect_url(self, request):
      return '/myprofile/'
