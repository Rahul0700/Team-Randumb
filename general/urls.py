from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
app_name = 'general'

urlpatterns = [
    path("model",views.predict,name="model_predict"),
]
