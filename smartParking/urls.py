from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('', include('homeApp.urls')),
                  path('dashboard/', include('dashboardApp.urls')),
                  path('register/', include('register.urls')),
                  path('login/', include('loginApp.urls')),
                  path('logout/', include('logoutApp.urls')),
                  path('add-parking/', include('addParkingApp.urls')),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
