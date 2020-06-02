from django.shortcuts import render, HttpResponse, get_object_or_404
from eventManager.models import event as event_model
from teachers.models import teacher
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from noticeboard.models import notice
from .models import blog
from study_materials.models import free_materials
from django.db.models import Q

def home(request):
	p = event_model.objects.filter()[:3]
	selected_event = []

	for this_event in p:
		temp_dict = {}
		temp_dict['pk'] = this_event.id
		temp_dict['title'] = this_event.title
		temp_dict['date'] = this_event.date
		temp_dict['location'] = this_event.location
		#temp_dict['title_image'] = str(this_event.title_image)
		temp_dict['title_image'] = this_event.title_image.url
		selected_event.append(temp_dict)
		
	context = {}
	context['selected_event'] = selected_event
	return render(request, 'home/index.html', context)


def course_view_science(request):
	p = free_materials.objects.filter(Q(belongs_to='Science') | Q(belongs_to='All Subject')).order_by('-date')
	page = request.GET.get('page', 1)
	paginator = Paginator(p, 8)

	try:
		selected_materials = paginator.page(page)
	except PageNotAnInteger:
		selected_materials = paginator.page(1)
	except EmptyPage:
		selected_materials = paginator.page(paginator.num_pages)

	return render(request, 'home/courses_science.html', { 'selected_materials' : selected_materials})

def course_view_commerce(request):
	p = free_materials.objects.filter(Q(belongs_to='Commerce') | Q(belongs_to='All Subject')).order_by('-date')
	page = request.GET.get('page', 1)
	paginator = Paginator(p, 8)

	try:
		selected_materials = paginator.page(page)
	except PageNotAnInteger:
		selected_materials = paginator.page(1)
	except EmptyPage:
		selected_materials = paginator.page(paginator.num_pages)

	return render(request, 'home/courses_commerce.html', { 'selected_materials': selected_materials})

def course_view_arts(request):
	p = free_materials.objects.filter(Q(belongs_to='Arts') | Q(belongs_to='All Subject')).order_by('-date')
	page = request.GET.get('page', 1)
	paginator = Paginator(p, 8)

	try:
		selected_materials = paginator.page(page)
	except PageNotAnInteger:
		selected_materials = paginator.page(1)
	except EmptyPage:
		selected_materials = paginator.page(paginator.num_pages)

	return render(request, 'home/courses_arts.html', {'selected_materials' : selected_materials})

def course_view_english(request):
	p = free_materials.objects.filter(Q(belongs_to='English') | Q(belongs_to='All Subject')).order_by('-date')
	page = request.GET.get('page', 1)
	paginator = Paginator(p, 8)

	try:
		selected_materials = paginator.page(page)
	except PageNotAnInteger:
		selected_materials = paginator.page(1)
	except EmptyPage:
		selected_materials = paginator.page(paginator.num_pages)

	return render(request, 'home/courses_english.html', {'selected_materials' : selected_materials})

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
		temp_dict['photo'] = str(t.teacher_photo.url)
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

def noticeView(request):
	notice_list = notice.objects.all().order_by('-date')
	page = request.GET.get('page', 1)

	paginator = Paginator(notice_list, 5)

	try:
		selected_notice = paginator.page(page)
	except PageNotAnInteger:
		selected_notice = paginator.page(1)
	except EmptyPage:
		selected_notice = paginator.page(paginator.num_pages)

	return render(request, 'home/notice.html', {'selected_notice': selected_notice} )

def blogList(request):
	bolg_list = blog.objects.all().order_by('-date')
	page = request.GET.get('page', 1)

	paginator = Paginator(bolg_list, 8)

	try:
		selected_blog = paginator.page(page)
	except PageNotAnInteger:
		selected_blog = paginator.page(1)
	except EmptyPage:
		selected_blog = paginator.page(paginator.num_pages)

	return render(request, 'home/bloglist.html', {'selected_blog' : selected_blog} )

def blogView(request, pk=None):
	query = get_object_or_404(blog, pk=pk)

	return render(request, 'home/blog_view.html', {'selected_blog' : query })