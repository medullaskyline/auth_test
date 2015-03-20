from userena_app.models import MyProfile
from django.contrib import admin
from django.contrib.auth.models import User, Permission
from guardian.models import UserObjectPermission
from django.contrib.contenttypes.models import ContentType
from userena.models import UserenaSignup


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


class UserObjectPermissionAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'linked_to',
        'permission',
        'content_type',
        'object_pk'

    )

    def linked_to(self, obj):
        return User.objects.get(pk=obj.user_id).username

    def content_type(self, obj):
        return ContentType.objects.get(pk=obj.content_type_id).name

    def permission(self, obj):
        return Permission.objects.get(pk=obj.permission_id).name

admin.site.register(UserObjectPermission, UserObjectPermissionAdmin)


class UserenaSignupAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'last_active',
        'activation_key',
        'activation_notification_send',
        'email_unconfirmed',
        'email_confirmation_key',
        'email_confirmation_key_created',
        'linked_to'
    )

    def linked_to(self, obj):
        return User.objects.get(pk=obj.user_id).username

admin.site.register(UserenaSignup, UserenaSignupAdmin)
