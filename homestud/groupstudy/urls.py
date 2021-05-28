from django.urls import path
from .views import GroupClassView, GroupClassUpdate, GroupClassDelete, GroupClassList

app_name = 'groupstudy'

urlpatterns = [

    path('class/create', GroupClassView.as_view(), name="create-group"),
    path('class/<int:pk>/update', GroupClassUpdate.as_view(), name='group_class_update'),
    path('class/<int:pk>/delete/', GroupClassDelete.as_view(), name='group_class_delete'),
    path('class/list/', GroupClassList.as_view(), name='group_class_list')

]