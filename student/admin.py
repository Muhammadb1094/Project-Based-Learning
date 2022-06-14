from django.conf import settings
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from django.core.mail import send_mail
import threading
from .models import Student


def send_email(email):
    subject = 'welcome to PBL System'
    message = f'Thank you for registering on PBL System.'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [email, ]
    send_mail(subject, message, email_from, recipient_list)


class ProfileInline(admin.StackedInline):
    model = Student
    can_delete = False
    verbose_name_plural = 'Student'
    fk_name = 'user'


class CustomUserAdmin(UserAdmin):
    inlines = (ProfileInline, )

    def get_inline_instances(self, request, obj=None):
        if not obj:
            return list()
        return super(CustomUserAdmin, self).get_inline_instances(request, obj)

    def save_model(self, request, obj, form, change):
        t1 = threading.Thread(target=send_email, args=(obj.email,))
        t1.start()
        super().save_model(request, obj, form, change)


admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)
