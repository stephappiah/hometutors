from django.urls import path
from .views import GroupClassView

app_name = 'groupstudy'

urlpatterns = [

    path('', GroupClassView.as_view(), name="group"),

]