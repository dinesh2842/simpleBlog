from members.views import PasswordsChangeView
from django.contrib import admin
from django.urls import path,include
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from django.conf import settings



urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('theblog.urls')),
    path('members/',include('django.contrib.auth.urls')),
    path('members/',include('members.urls')),
    #path('<int:id>/password/',auth_views.PasswordChangeView.as_view(template_name='registration/change-password.html')),
    path('<int:id>/password/',PasswordsChangeView.as_view(template_name='registration/change-password.html')),


    

]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
