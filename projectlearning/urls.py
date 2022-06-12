from django.conf.urls.static import static
from django.urls import path, include
from django.contrib import admin
from exam import views
from django.contrib.auth.views import LogoutView
from django.conf import settings
admin.site.site_header = "Project Based Learning Admin Panel"
admin.site.site_title = "PBL Admin"
admin.site.index_title = "Welcome to PBL Portal"

urlpatterns = [
   
    path('admin/', admin.site.urls),
    path('student/', include('student.urls')),
    path('', views.home_view, name=''),
    path('logout', LogoutView.as_view(template_name='exam/index.html'), name='logout'),
    path('contactus', views.contactus_view),
    path('afterlogin', views.afterlogin_view, name='afterlogin'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
