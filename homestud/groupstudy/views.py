from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, UpdateView, DeleteView, ListView, DetailView
from django.views.generic.edit import BaseDeleteView
from .models import GroupClass
from .forms import GroupClassForm
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect
import json
from findtutors.courses import courses_choices, programmes_choices

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
    # check if logged in user matches the user saved with the
    # group class object
    def dispatch(self, request, *args, **kwargs):
        id_ = self.kwargs.get('pk')
        gClass = get_object_or_404(GroupClass, id=id_)
        logged_in_user = self.request.user

        if not gClass.tutor == logged_in_user:
            print('user didnt create this class')
            return HttpResponseRedirect(reverse('groupstudy:group_class_list'))
        else:
            print('user created this class')
            return super(GroupClassUpdate, self).dispatch(request, *args, **kwargs)
    
    model = GroupClass
    form_class = GroupClassForm
    template_name = 'groupstudy/update_group.html'

    success_url = reverse_lazy('groupstudy:group_class_list')

class GroupClassDelete(LoginRequiredMixin, DeleteView):
    # check if logged in user matches the user saved with the
    # group class object
    def dispatch(self, request, *args, **kwargs):
        id_ = self.kwargs.get('pk')
        gClass = get_object_or_404(GroupClass, id=id_)
        logged_in_user = self.request.user

        if not gClass.tutor == logged_in_user:
            print('user didnt create this class')
            return HttpResponseRedirect(reverse('groupstudy:group_class_list'))
        else:
            print('user created this class')
            return super(GroupClassDelete, self).dispatch(request, *args, **kwargs)
    
    model = GroupClass
    success_url = reverse_lazy('groupstudy:group_class_list')

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

class ShowGroupClass(LoginRequiredMixin, ListView):
    template_name = 'groupstudy/show_group.html'
    context_object_name = 'group_classes'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # check if search form has coordinates
        # else use coordinates from session
        def get_latitude():
            if self.request.GET.get('latitude') is not None or '':
                # coordinates from search form
                latitude = self.request.GET.get('latitude')
                return latitude
            else:
                # coordinates from session
                latitude = self.request.session['lat']
                return latitude

        def get_longitude():
            if request.GET.get('longitude') is not None or '':
                # coordinates from search form
                longitude = self.request.GET.get('longitude')
                return longitude
            else:
                # coordinates from session
                longitude = self.request.session['lon']
                return longitude
    

        context['programme_list'] = json.dumps(dict(programmes_choices))
        context['course_list'] = json.dumps(dict(courses_choices))
        return context

    def get_queryset(self):
        current_user = self.request.user

        
        return GroupClass.objects.filter(tutor=current_user)



    def render_to_response(self, context, **response_kwargs):
        """ Allow AJAX requests to be handled more gracefully """
        if self.request.is_ajax():
            context = self.get_context_data(**response_kwargs)
            rendered = render_to_string(self.template_name, context, request=self.request)

            return JsonResponse({'update_form': rendered}, safe=False, **response_kwargs)
        else:
            return super(ShowGroupClass, self).render_to_response(context, **response_kwargs)
