from django.shortcuts import render, HttpResponse
from eventManager.models import event as event_model
from teachers.models import teacher
def home(request):
	p = event_model.objects.filter()[:3]
	selected_event = []

	for this_event in p:
		temp_dict = {}
		temp_dict['pk'] = this_event.id
		temp_dict['title'] = this_event.title
		temp_dict['date'] = this_event.date
		temp_dict['location'] = this_event.location
		temp_dict['title_image'] = str(this_event.title_image)
		selected_event.append(temp_dict)
		
	context = {}
	context['selected_event'] = selected_event
	return render(request, 'home/index.html', context)


def course_view_science(request):
	return render(request, 'home/courses_science.html')

def course_view_commerce(request):
	return render(request, 'home/courses_commerce.html')

def course_view_arts(request):
	return render(request, 'home/courses_arts.html')

def events(request):
	p = event_model.objects.filter()[0]
	selected_event = {}
	selected_event['pk'] = p.id
	selected_event['title'] = p.title
	selected_event['date'] = p.date
	selected_event['location'] = p.location
	selected_event['title_image'] = str(p.title_image)
	selected_event['short_description'] = p.short_description
	selected_event['youtube_vide_link'] = p.youtube_vide_link

	q = event_model.objects.filter()[1:]

	all_event = []

	for event in q:
		temp_dict = {}
		temp_dict['pk'] = event.id
		temp_dict['title'] = event.title
		temp_dict['date'] = event.date
		temp_dict['location'] = event.location
		temp_dict['title_image'] = str(event.title_image)
		temp_dict['short_description'] = event.short_description
		temp_dict['youtube_vide_link'] = event.youtube_vide_link
		all_event.append(temp_dict)

	context = {}
	context['selected_event'] = selected_event
	context['all_event'] = all_event

	return render(request, 'home/events.html', context)

def events_param(request, pk=None):
	p = event_model.objects.get(pk=pk)
	selected_event = {}
	selected_event['pk'] = p.id
	selected_event['title'] = p.title
	selected_event['date'] = p.date
	selected_event['location'] = p.location
	selected_event['title_image'] = str(p.title_image)
	selected_event['short_description'] = p.short_description
	selected_event['youtube_vide_link'] = p.youtube_vide_link
	
	q = event_model.objects.filter().exclude(id=pk)

	all_event = []

	for event in q:
		temp_dict = {}
		temp_dict['pk'] = event.id
		temp_dict['title'] = event.title
		temp_dict['date'] = event.date
		temp_dict['location'] = event.location
		temp_dict['title_image'] = str(event.title_image)
		temp_dict['short_description'] = event.short_description
		temp_dict['youtube_vide_link'] = event.youtube_vide_link
		all_event.append(temp_dict)

	context = {}
	context['selected_event'] = selected_event
	context['all_event'] = all_event

	return render(request, 'home/events.html', context)

def teachers(request):
	p = teacher.objects.filter()

	teacher_list = []

	for t in p:
		temp_dict = {}
		temp_dict['name'] = t.name
		temp_dict['subject'] = t.subject
		temp_dict['photo'] = str(t.teacher_photo)
		temp_dict['facebook'] = t.facebook_profile
		temp_dict['twitter'] = t.twitter_profile
		temp_dict['instagram'] = t.instagram_profile
		temp_dict['googleplus'] = t.googlePlus_profile
		teacher_list.append(temp_dict)

	context = {}
	context['teacher_list'] = teacher_list

	return render(request, 'home/teachers.html', context)

def contact(request):
	return render(request, 'home/contact.html')

def test(request, pk=None):
	return render(request, 'home/events.html')