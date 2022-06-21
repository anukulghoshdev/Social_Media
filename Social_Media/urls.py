    
from django.contrib import admin
from django.urls import path, include

from App_Posts import views

from django.conf import settings
from django.contrib.staticfiles.urls import static, staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/', include('App_RegLog.urls')),
    path('posts/', include('App_Posts.urls')),
    path('', views.home, name='home'),

]
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
