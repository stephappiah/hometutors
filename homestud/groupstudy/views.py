from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, UpdateView, DeleteView, ListView, DetailView
from django.views.generic.edit import BaseDeleteView
from .models import GroupClass
from .forms import GroupClassForm
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect, JsonResponse
import json
from findtutors.courses import courses_choices, programmes_choices
from django.contrib.gis.db.models.functions import Distance
from django.contrib.gis.geos import fromstr, Point
from django.contrib.gis.measure import D
from django.core.paginator import Paginator
from django.template.loader import render_to_string, get_template


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
    # allows only the user related to the class to delete 
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

class ShowGroupClass(ListView):
    template_name = 'groupstudy/show_group.html'
    context_object_name = 'group_classes'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        qs = qs = GroupClass.objects.all()
        
        context['total_groups'] = qs.count()
        context['programme_list'] = json.dumps(dict(programmes_choices))
        context['course_list'] = json.dumps(dict(courses_choices))

        print(qs.count())
        return context

    def get_queryset(self):
        
        qs = GroupClass.objects.all()
        paginator = Paginator(qs, 10) #show 10 tutors per page

        page_number = self.request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        return page_obj


def FilterSearch(request):
    #for dropdown
    programme_list = json.dumps(dict(programmes_choices))
    course_list = json.dumps(dict(courses_choices))

    # check if search form has coordinates
    # else use coordinates from session
    def get_latitude():
        if request.GET.get('latitude') is not None or '':
            # coordinates from search form
            latitude = request.GET.get('latitude')

            # Store coordinates in user session
            request.session['lat'] = latitude

            return latitude
        else:
            # coordinates from session
            latitude = request.session['lat']
            return latitude

    def get_longitude():
        if request.GET.get('longitude') is not None or '':
            # coordinates from search form
            longitude = request.GET.get('longitude')

            # Store coordinates in user session
            request.session['lon'] = longitude 

            return longitude
        else:
            # coordinates from session
            longitude = request.session['lon']
            return longitude
    
    # check if long and lat returns a value & are not empty
    if get_longitude() != '' or get_latitude() != '':

        # get coordinates
        longitude = float(get_longitude())
        latitude = float(get_latitude())
        print(longitude, latitude)
        user_location = Point(longitude, latitude, srid=4326)
        # Queryset filtered within a distance of 100km; annotated and orderd by distance
        dist = Distance('location', user_location)
        qs = GroupClass.objects.filter(location__distance_lte=(user_location, D(km=100))).annotate(distance=dist).order_by('distance')
    else:
        qs = GroupClass.objects.all()

    # Grab search fields
    programme = request.GET.get('programme')
    course = request.GET.get('course')
    
    if programme != '' and programme is not None:
        qs = qs.filter(programs__icontains=programme)

    if course != '' and course is not None:
        qs = qs.filter(subjects__icontains=course)

    paginator = Paginator(qs, 10) #show 10 tutors per page

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
                'group_classes': page_obj,
                'total_groups': qs.count(),
                'programme_list': programme_list,
                'course_list': course_list
    }
    return render(request, 'groupstudy/show_group.html', context)
