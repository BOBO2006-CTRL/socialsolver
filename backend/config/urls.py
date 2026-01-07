from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

def root_redirect(request):
    return redirect('/issues/')

urlpatterns = [
    path('', root_redirect),          # ← ВАЖНО
    path('admin/', admin.site.urls),
    path('issues/', include('issues.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/', include('users.auth_urls')),
]