from django.shortcuts import render, HttpResponse
from userena.views import activate, activate_retry, direct_to_user_template, email_change, email_confirm, password_change, profile_detail, profile_edit, signup, signin, signin_redirect, signout, userena_settings, userena_signals


# def signup(request):
#     return HttpResponse('')
#
#
# def signin(request):
#     return HttpResponse('')
#
#
# def signout(request):
#     return HttpResponse('')
#
#
# def profile(request):
#     return HttpResponse('')
