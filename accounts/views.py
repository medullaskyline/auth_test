from django.shortcuts import render


def allauth_profiles(request):
    return render(request, 'accounts/allauth_base.html')