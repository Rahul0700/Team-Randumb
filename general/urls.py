from django.urls import path
from . import views
app_name = 'general'

urlpatterns = [
    path('<id>/',views.Eventview,name='event'),
    path('<slug>/createevent/',views.Eventform,name='createevent'),
    path('<id>/updateevent/',views.EventUpdateform,name='updateevent'),
    path('<id>/removeevent/',views.Eventdelete,name='removeevent'),
    path('question/<id>/',views.AnswerFaq,name='answerfaq'),
    path("model",views.predict,name="model_predict"),
]
