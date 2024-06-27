from django.urls import path, include

urlpatterns = [
    path('client/', include('clients.client.urls')),
    path('designation/', include('clients.designation.urls')),
    path('department/', include('clients.department.urls')),
    path('user/', include('clients.user.urls')),
]