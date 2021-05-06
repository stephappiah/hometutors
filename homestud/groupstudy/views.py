from django.shortcuts import render

from django.views.generic import CreateView
from .models import GroupClass
from .forms import GroupClassForm

class GroupClassView(CreateView):
    model = GroupClass
    form_class = GroupClassForm
    template_name = 'groupstudy/create_group.html'

