from django.contrib import admin
from django.urls import path
#added manually
from django.urls import include
from myapp.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    #added manually
    path('api/', include('myapp.urls')),
    path('', home, name='home'),
]
