from django.urls import path
from .views import index, trigger_list
from . import views  # <--- det här saknades

urlpatterns = [
    path('', views.index, name='index'),
    path('api/triggers/', trigger_list, name='api_triggers'),
]
