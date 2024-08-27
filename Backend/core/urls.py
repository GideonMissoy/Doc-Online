from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/users/auth/', include('Accounts.urls')),
    path("api/", include("Api.urls")),
]