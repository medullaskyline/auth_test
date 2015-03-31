from django.shortcuts import render


def allauth_profiles(request):
    return render(request, 'allauth_app/allauth_base.html')