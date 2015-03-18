from userena_app.models import MyProfile
from django.contrib import admin
from django.contrib.auth.models import User


class MyProfileAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'mugshot',
        'privacy',
        'favourite_snack',
        'linked_to'
    )

    def linked_to(self, obj):
        return User.objects.get(pk=obj.user_id).username


# admin.site.register(MyProfile, MyProfileAdmin)
