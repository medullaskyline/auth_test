from django.shortcuts import render


def choose_authentication_system(request):
    return render(request, 'auth_test/home.html', {'request': request})