"""djangOauth URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Oauth import views as oauth_views
from Oauth.master import obtain_jwt_token as new_obtain_jwt_token
from Oauth.master import refresh_jwt_token as new_refresh_jwt_token
from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='djangOauth API')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/login/', new_obtain_jwt_token),
    path('api/token-refresh/', new_refresh_jwt_token),
    path('api/logout/', oauth_views.LogoutViewSet.as_view({'get':'logout'})),
    path('api/doc/', schema_view),
]
