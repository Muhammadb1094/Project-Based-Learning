from django.conf.urls.static import static
from django.urls import path, include
from django.contrib import admin
from django.contrib.auth.views import LogoutView
from django.conf import settings

admin.site.site_header = "Project Based Learning Admin Panel"
admin.site.site_title = "PBL Admin"
admin.site.index_title = "Welcome to PBL Portal"

urlpatterns = [
   
    path('admin/', admin.site.urls),
    path('student/', include('student.urls')),
    path('', include('exam.urls'), name=''),
    path('logout', LogoutView.as_view(template_name='exam/index.html'), name='logout'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
