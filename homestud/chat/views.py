from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.http import HttpResponseRedirect, JsonResponse, Http404
from django.contrib.auth import logout, get_user_model
from django.core.exceptions import PermissionDenied
from django.conf import settings
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.base import TemplateView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import get_object_or_404

from homestud.decorators import subcribed_user


from .models import Room, Message
from .utils import create_room

# import the logging library
import logging

# Get an instance of a logger
logger = logging.getLogger(__name__)

def import_base_template():
	try:
		return settings.CHATTER_BASE_TEMPLATE
	except AttributeError as e:
		try:
			if settings.CHATTER_DEBUG == True:
				logger.info("chat.views: "
				"(Optional) settings.CHATTER_BASE_TEMPLATE not found. You can "
				"set it to point to your base template in your settings file.")
		except AttributeError as e:
			logger.info("chat.views: "
			"(Optional) settings.CHATTER_BASE_TEMPLATE not found. You can "
			"set it to point to your base template in your settings file.")
			logger.info("chat.views: to turn off this message, set "
			"your settings.CHATTER_DEBUG to False.")
		return 'chat/base.html'


class IndexView(LoginRequiredMixin, View):

	def get(self, request, *args, **kwargs):
		rooms_list = Room.objects.filter(members=request.user).order_by('-date_modified')
		if rooms_list.exists():
			latest_room_uuid = rooms_list[0].id
			return HttpResponseRedirect(
				reverse('chat:chatroom', args=[latest_room_uuid])
			)
		else:
			# create room with the user themselves
			user = get_object_or_404(get_user_model(), username=request.user.username) #my code
			# user = get_user_model().objects.get(username=request.user) #original
			room_id = create_room([user])
			return HttpResponseRedirect(
				reverse('chat:chatroom', args=[room_id])
			)


# This fetches a chatroom given the room ID if a user diretly wants to access the chat.
class ChatRoomView(LoginRequiredMixin, TemplateView):
	template_name = 'chat/chat-window.html'

	# This gets executed whenever a room exists
	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		uuid = kwargs.get('uuid')
		try:
			room = Room.objects.get(id=uuid)
			user=get_user_model().objects.get(username=self.request.user.username)
		except Exception as e:
			logger.exception("\n\nException in chat.views.ChatRoomView:\n")
			raise Http404("Sorry! What you're looking for isn't here.")
		all_members = room.members.all()
		if user in all_members:
			latest_messages_curr_room = room.message_set.all()[:50]
			if latest_messages_curr_room.exists():
				message = latest_messages_curr_room[0]
				message.recipients.add(user)
			if all_members.count() == 1:
				room_name = "Notes to Yourself"
				# get user's contact in template --> my code
				contact = ''
			elif all_members.count() == 2:
				room_name = all_members.exclude(pk=user.pk)[0].get_full_name()

				# get user's contact in template --> my code
				contact = all_members.exclude(pk=user.pk)[0].get_call_contact()
			else:
				room_name = room.__str__()

			context['room_uuid_json'] = kwargs.get('uuid')
			context['latest_messages_curr_room'] = latest_messages_curr_room
			context['room_name'] = room_name
			context['base_template'] = import_base_template()
			context['contact'] = contact

			# Add rooms with unread messages
			rooms_list = Room.objects.filter(members=self.request.user)\
				.order_by('-date_modified')[:10]
			rooms_with_unread = []
			# Go through each list of rooms and check if the last message was unread
			# and add each last message to the context
			for room in rooms_list:
				try:
					message = room.message_set.all().order_by('-id')[0]
				except IndexError as e:
					continue
				if self.request.user not in message.recipients.all():
					rooms_with_unread.append(room.id)
			context['rooms_list'] = rooms_list
			context['rooms_with_unread'] = rooms_with_unread

			return context
		else:
			raise Http404("Sorry! What you're looking for isn't here.")


#The following functions deal with AJAX requests
@login_required
def users_list(request):
	if (request.is_ajax()):
		data_array = []
		for user in get_user_model().objects.all():
			data_dict = {}
			data_dict['id'] = user.pk
			data_dict['text'] = user.username
			data_array.append(data_dict)
		return JsonResponse(data_array, safe=False)


@login_required
@subcribed_user 
def get_chat_url(request):

	# user = get_user_model().objects.get(username=request.user.username)
	user = get_object_or_404(get_user_model(), username=request.user.username) #my code
	# target_user = get_user_model().objects.get(username=request.POST.get('target_user')) #changed from pk to username mycode
	target_user = get_object_or_404(get_user_model(), username=request.GET.get('target_user')) #my code
	
	print(user)
	print(target_user)
	'''
	AI-------------------------------------------------------------------
		Use the util room creation function to create room for one/two
		user(s). This can be extended in the future to add multiple users
		in a group chat.
	-------------------------------------------------------------------AI
	'''
	if (user == target_user):
		room_id = create_room([user])
	else:
		room_id = create_room([user, target_user])
	return HttpResponseRedirect(
		reverse('chat:chatroom', args=[room_id])
	)

# Ajax request to fetch earlier messages
@login_required
def get_messages(request, uuid):
	if request.is_ajax():
		room = Room.objects.get(id=uuid)
		if request.user in room.members.all():
			messages = room.message_set.all()
			page = request.GET.get('page')

			paginator = Paginator(messages, 20)
			try:
				selected = paginator.page(page)
			except PageNotAnInteger:
				selected = paginator.page(1)
			except EmptyPage:
				selected = []
			messages_array = []
			for message in selected:
				dict = {}
				dict['sender'] = message.sender.username
				dict['message'] = message.text
				dict['received_room_id'] = uuid
				dict['date_created'] = message.date_created.strftime("%d %b %Y %H:%M:%S %Z")
				messages_array.append(dict)

			return JsonResponse(messages_array, safe=False)

		else:
			return Http404("Sorry! We can't find what you're looking for.")
	else:
		return Http404("Sorry! We can't find what you're looking for.")
