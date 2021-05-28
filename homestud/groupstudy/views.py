from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, UpdateView, DeleteView, ListView, DetailView
from django.views.generic.edit import BaseDeleteView
from .models import GroupClass
from .forms import GroupClassForm
from django.urls import reverse_lazy

class GroupClassView(LoginRequiredMixin, CreateView):
    model = GroupClass
    form_class = GroupClassForm
    template_name = 'groupstudy/create_group.html'

    # restrict to tutors
    success_url = reverse_lazy('groupstudy:group_class_list')

    def form_valid(self, form):
        form.instance.tutor = self.request.user
        total_seats = self.request.POST.get('total_seats')
        print(total_seats)
        form.instance.available_seats = self.request.POST.get('total_seats')
        return super().form_valid(form)

class GroupClassUpdate(LoginRequiredMixin, UpdateView):
    model = GroupClass
    form_class = GroupClassForm
    template_name = 'groupstudy/update_group.html'

    # to do: restrict to related tutor
    success_url = reverse_lazy('groupstudy:group_class_list')

class GroupClassDelete(LoginRequiredMixin, DeleteView):
    
    model = GroupClass
    success_url = reverse_lazy('groupstudy:group_class_list')
    # todo: restrict to related tutor

    # def get_object(self):
    #     id_ = self.kwargs.get('id')
    #     return get_object_or_404(GroupClass, id=id_)

    def render_to_response(self, context, **response_kwargs):
        """ Allow AJAX requests to be handled more gracefully """
        if self.request.is_ajax():
            context = self.get_context_data(**response_kwargs)
            rendered = render_to_string(self.template_name, context, request=self.request)

            return JsonResponse({'delete_form': rendered}, safe=False, **response_kwargs)
        else:
            return super(DeleteView, self).render_to_response(context, **response_kwargs)


class GroupClassList(LoginRequiredMixin, ListView):
    template_name = 'groupstudy/list_group.html'
    context_object_name = 'group_classes'
    def get_queryset(self):
        current_user = self.request.user
        return GroupClass.objects.filter(tutor=current_user)

class GroupClassDetail(LoginRequiredMixin, DetailView):
    pass
