from django.core.mail import send_mail
from twilio.rest import Client, TwilioRestClient
from django.shortcuts import render, get_list_or_404, get_object_or_404, redirect
from django.conf import settings
from django.db.models import Count, Sum, Q, F
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.http import Http404, HttpResponse, HttpResponseRedirect
# from django.core.urlresolvers import resolve, reverse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.urls import resolve, reverse
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from datetime import datetime, timedelta, time
from .functions import *
from .models import *
from .global_data import *
from .search_users import *



# home

def home_view(request):

	on_home_page = 'current'
	title = 'Bienvenue à la Renaissance'

	today = datetime.now().date()
	
	sliders_list = Slider.objects.all().filter(active=True).order_by('rank')
	gallery_categories = GalleryCategory.objects.all().filter(active=True)
	our_gallery = Gallery.objects.all().filter(active=True).order_by('?')[:9]

	global_context = get_global_data(request)

	page_context = {

		'title': title,
		'onHomePage': on_home_page,
		'homeSliders': sliders_list,
		'galleryGategories': gallery_categories,
		'ourGallery': our_gallery,
	}

	home_context = global_context.copy()
	home_context.update(page_context)

	return render(request, 'main_app/home.html', home_context)




def newsletter_registration_view(request):

	newsletter_email = request.POST.get('newsletterEmail', None)

	if newsletter_email == None or newsletter_email == '':
		return HttpResponseRedirect(reverse('mainAppNamespace:HomeName'))
	else:
		newsletter_email=newsletter_email.lower()

		try:
			user = User.objects.get(username=newsletter_email)
		except:
			generated_password = generate_random_string()

			User.objects.create_user(username=newsletter_email, password=generated_password)

			get_newsletter_user_data = User.objects.all().filter(username=newsletter_email)
			for newsletter_user_data in get_newsletter_user_data:
				user = User.objects.get(username=newsletter_user_data.username)

			UserAccount.objects.create(user=user, first_name='Newsletter', last_name='Anonyme', show=False, email=newsletter_email)

		UserAccount.objects.filter(user=user).update(registered_for_newsletter=True)

		messages.success(request, "Inscription au newsletter réussie!")

		return HttpResponseRedirect(reverse('mainAppNamespace:HomeName'))




# about us

def about_us_view(request):

	on_about_us_page = 'current'
	title = 'La Renaissance | Presentation'

	global_context = get_global_data(request)

	page_context = {

		'title': title,
		'onAboutUsPage': on_about_us_page,
	}

	about_us_context = global_context.copy()
	about_us_context.update(page_context)

	return render(request, 'main_app/about_us.html', about_us_context)







# historique

def historique_view(request):

	on_about_us_page = 'current'
	title = 'La Renaissance | Historique'

	global_context = get_global_data(request)

	page_context = {

		'title': title,
		'onAboutUsPage': on_about_us_page,
	}

	historique_context = global_context.copy()
	historique_context.update(page_context)

	return render(request, 'main_app/historique.html', historique_context)







# directions

def directions_view(request):

	on_about_us_page = 'current'
	title = 'La Renaissance | Directions'

	our_directions = Direction.objects.all().filter(active=True)

	global_context = get_global_data(request)

	page_context = {

		'title': title,
		'onAboutUsPage': on_about_us_page,
		'ourDirections': our_directions,
	}

	directions_context = global_context.copy()
	directions_context.update(page_context)

	return render(request, 'main_app/directions.html', directions_context)







# direction

def direction_view(request, direction_slug):

	on_about_us_page = 'current'
	title = 'La Renaissance | Direction'

	check_direction = Direction.objects.filter(slug=direction_slug).count()
	if check_direction == 0:
		messages.error(request, "Désolé, nous n'avons pas trouvé la direction!")
		return HttpResponseRedirect(reverse('mainAppNamespace:DirectionsName'))

	requested_direction = Direction.objects.all().filter(slug=direction_slug)

	global_context = get_global_data(request)

	page_context = {

		'title': title,
		'onAboutUsPage': on_about_us_page,
		'requestedDirection': requested_direction,
	}

	direction_context = global_context.copy()
	direction_context.update(page_context)

	return render(request, 'main_app/direction.html', direction_context)







# projects

def projects_view(request):

	on_about_us_page = 'current'
	title = 'La Renaissance | Projets'

	our_projects_list = OurProject.objects.all().filter(active=True)

	paginator = Paginator(our_projects_list, 9)
	page = request.GET.get('page')
	try:
		our_projects = paginator.page(page)
	except PageNotAnInteger:
		our_projects = paginator.page(1)
	except EmptyPage:
		our_projects = paginator.page(paginator.num_pages)

	global_context = get_global_data(request)

	page_context = {

		'title': title,
		'onAboutUsPage': on_about_us_page,
		'ourProjects': our_projects,
	}

	projects_context = global_context.copy()
	projects_context.update(page_context)

	return render(request, 'main_app/projects.html', projects_context)




# project

def project_view(request, projet_slug):

	on_about_us_page = 'current'
	title = 'La Renaissance | Projet'

	check_project = OurProject.objects.filter(slug=projet_slug).count()
	if check_project == 0:
		messages.error(request, "Désolé, nous n'avons pas trouvé le projet!")
		return HttpResponseRedirect(reverse('mainAppNamespace:ProjectsName'))

	requested_project = OurProject.objects.all().filter(slug=projet_slug)

	global_context = get_global_data(request)

	page_context = {

		'title': title,
		'onAboutUsPage': on_about_us_page,
		'requestedProject': requested_project,
	}

	project_context = global_context.copy()
	project_context.update(page_context)

	return render(request, 'main_app/project.html', project_context)




# service

def service_view(request, service_slug):

	on_service_page = 'current'
	title = 'La Renaissance | Service'

	check_service = OurService.objects.filter(slug=service_slug).count()
	if check_service == 0:
		messages.error(request, "Désolé, nous n'avons pas trouvé le service!")
		return HttpResponseRedirect(reverse('mainAppNamespace:HomeName'))

	requested_service = OurService.objects.all().filter(slug=service_slug)

	global_context = get_global_data(request)

	page_context = {

		'title': title,
		'onServicePage': on_service_page,
		'requestedService': requested_service,
	}

	service_context = global_context.copy()
	service_context.update(page_context)

	return render(request, 'main_app/service.html', service_context)






# timetable

def timetable_view(request):

	on_doctors_page = 'current'
	title = 'La Renaissance | Plage Horaires'

	days_of_the_week = DayOfTheWeek.objects.all()
	working_hours = WorkingHour.objects.all()
	our_timetable = Timetable.objects.all().order_by('ranking')

	global_context = get_global_data(request)

	page_context = {

		'title': title,
		'onDoctorsPage': on_doctors_page,
		'daysOfTheWeek': days_of_the_week,
		'workingHours': working_hours,
		'ourTimetable': our_timetable,
	}

	timetable_context = global_context.copy()
	timetable_context.update(page_context)

	return render(request, 'main_app/timetable.html', timetable_context)




# our team

def our_team_view(request):

	on_doctors_page = 'current'
	title = 'La Renaissance | Notre Equipe'

	doctor = request.GET.get('doctor', None)
	active = request.GET.get('active', None)
	position_slug = request.GET.get('position_slug', None)
	is_patient = request.GET.get('is_patient', None)
	country_slug = request.GET.get('country_slug', None)
	town_slug = request.GET.get('town_slug', None)
	registered_from_date = request.GET.get('registered_from_date', None)
	registered_to_date = request.GET.get('registered_to_date', None)
	custom_search = request.GET.get('custom_search', None)	

	returned_users_ids, returned_users_title = list_users(active, position_slug, is_patient, country_slug, town_slug, registered_from_date, registered_to_date, custom_search)

	if doctor == 'true' :
		get_users_list = UserAccount.objects.all().filter(id__in=returned_users_ids, show=True, is_doctor=True)
	else:
		get_users_list = UserAccount.objects.all().filter(id__in=returned_users_ids, show=True)
		
	paginator = Paginator(get_users_list, 12)
	page = request.GET.get('page')
	try:
		users_list = paginator.page(page)
	except PageNotAnInteger:
		users_list = paginator.page(1)
	except EmptyPage:
		users_list = paginator.page(paginator.num_pages)

	global_context = get_global_data(request)

	page_context = {

		'title': title,
		'onDoctorsPage': on_doctors_page,
		'usersList': users_list,
		'returnedUsersTitle': returned_users_title,
	}

	our_team_context = global_context.copy()
	our_team_context.update(page_context)

	return render(request, 'main_app/our_team.html', our_team_context)



# member

def member_view(request, member_slug):

	on_doctors_page = 'current'
	title = 'La Renaissance | Projet'

	check_user = UserAccount.objects.filter(slug=member_slug).count()
	if check_user == 0:
		messages.error(request, "Désolé, nous n'avons pas trouvé le member!")
		return HttpResponseRedirect(reverse('mainAppNamespace:OurTeamName'))

	requested_user = UserAccount.objects.all().filter(slug=member_slug)

	global_context = get_global_data(request)

	page_context = {

		'title': title,
		'onDoctorsPage': on_doctors_page,
		'requestedUser': requested_user,
	}

	member_context = global_context.copy()
	member_context.update(page_context)

	return render(request, 'main_app/member.html', member_context)



# prepare admission

def prepare_admission_view(request):

	on_patient_space_page = 'current'
	title = 'La Renaissance | Préparer Votre Séjour'

	global_context = get_global_data(request)

	page_context = {

		'title': title,
		'onPatientSpacePage': on_patient_space_page,
	}

	prepare_admission_context = global_context.copy()
	prepare_admission_context.update(page_context)

	return render(request, 'main_app/prepare_admission.html', prepare_admission_context)





# daily life

def daily_life_view(request):

	on_patient_space_page = 'current'
	title = 'La Renaissance | Vie Quotidienne'

	global_context = get_global_data(request)

	page_context = {

		'title': title,
		'onPatientSpacePage': on_patient_space_page,
	}

	daily_life_context = global_context.copy()
	daily_life_context.update(page_context)

	return render(request, 'main_app/daily_life.html', daily_life_context)






# rights and duties

def rights_and_duties_view(request):

	on_patient_space_page = 'current'
	title = 'La Renaissance | Droits & Devoir'

	global_context = get_global_data(request)

	page_context = {

		'title': title,
		'onPatientSpacePage': on_patient_space_page,
	}

	rights_and_duties_context = global_context.copy()
	rights_and_duties_context.update(page_context)

	return render(request, 'main_app/rights_and_duties.html', rights_and_duties_context)




# media

def media_view(request, category_slug):

	on_media_page = 'current'
	title = 'La Renaissance | Média'

	check_news_category = NewsCategory.objects.filter(slug=category_slug).count()
	if check_news_category == 0:
		messages.error(request, "Désolé, nous n'avons pas trouvé le média!")
		return HttpResponseRedirect(reverse('mainAppNamespace:HomeName'))

	news_category_data = NewsCategory.objects.all().filter(slug=category_slug)
	news_category_instance = NewsCategory.objects.get(slug=category_slug)

	get_news_list = News.objects.all().filter(category=news_category_instance, active=True)

	paginator = Paginator(get_news_list, 9)
	page = request.GET.get('page')
	try:
		news_list = paginator.page(page)
	except PageNotAnInteger:
		news_list = paginator.page(1)
	except EmptyPage:
		news_list = paginator.page(paginator.num_pages)

	global_context = get_global_data(request)

	page_context = {

		'title': title,
		'onMediaPage': on_media_page,
		'newsCategoryData': news_category_data,
		'newsList': news_list,
	}

	media_context = global_context.copy()
	media_context.update(page_context)

	return render(request, 'main_app/media.html', media_context)




# our gallery

def our_gallery_view(request):

	on_media_page = 'current'
	title = 'La Renaissance | Gallerie'

	today = datetime.now().date()

	gallery_categories = GalleryCategory.objects.all().filter(active=True)
	our_gallery = Gallery.objects.all().filter(active=True).order_by('?')

	global_context = get_global_data(request)

	page_context = {

		'title': title,
		'onMediaPage': on_media_page,
		'galleryGategories': gallery_categories,
		'ourGallery': our_gallery,
	}

	our_gallery_context = global_context.copy()
	our_gallery_context.update(page_context)

	return render(request, 'main_app/our_gallery.html', our_gallery_context)



# article

def article_view(request, news_slug):

	on_media_page = 'current'
	title = 'La Renaissance | Article'

	check_project = News.objects.filter(slug=news_slug).count()
	if check_project == 0:
		messages.error(request, "Désolé, nous n'avons pas trouvé l'article!")
		return HttpResponseRedirect(reverse('mainAppNamespace:MediaName', kwargs={'media': news_slug}))
		
	requested_article = News.objects.all().filter(slug=news_slug)
	lattest_news_list = News.objects.all().filter(active=True).order_by('-id')[:5]

	requested_article_instance = News.objects.get(slug=news_slug)
	requested_article_comments = NewsComment.objects.all().filter(news=requested_article_instance)

	global_context = get_global_data(request)

	page_context = {

		'title': title,
		'onMediaPage': on_media_page,
		'requestedArticle': requested_article,
		'lattestNewsList': lattest_news_list,
		'requestedArticleComments': requested_article_comments,
	}

	article_context = global_context.copy()
	article_context.update(page_context)

	return render(request, 'main_app/article.html', article_context)




# comment news

@login_required(login_url='/login-redirect?redirect_message=Veuillez vous connecter pour commenter!')
def comment_news_view(request, news_slug):

	comment = request.POST.get('comment', None)

	check_news = News.objects.filter(slug=news_slug).count()
	if check_news == 0:
		messages.error(request, "Désolé, nous n'avons pas trouvé le média que vous voullez commenter!")
		return HttpResponseRedirect(reverse('mainAppNamespace:HomeName'))

	get_requested_news_data = News.objects.all().filter(slug=news_slug)
	for requested_news_data in get_requested_news_data:
		number_of_requested_news_comments = requested_news_data.number_of_comments

	new_number_of_requested_news_comments = number_of_requested_news_comments+1

	if request.method == 'POST':
		news_instance = News.objects.get(slug=news_slug)

		logged_user_instance = User.objects.get(id=request.user.id)

		get_logged_user_data = UserAccount.objects.all().filter(user=logged_user_instance)
		for logged_user_data in get_logged_user_data:
			logged_user_account_instance = UserAccount.objects.get(slug=logged_user_data.slug)

		NewsComment.objects.create(news=news_instance, commented_by=logged_user_account_instance, comment=comment)

		News.objects.filter(slug=news_slug).update(number_of_comments=new_number_of_requested_news_comments)

		messages.success(request, "Commentaire posté avec succès!")
		return HttpResponseRedirect(reverse('mainAppNamespace:ArticleName', kwargs={'news_slug': news_slug}))
	else:
		return HttpResponseRedirect(reverse('mainAppNamespace:ArticleName', kwargs={'news_slug': news_slug}))
	



# contact

def contact_view(request):

	on_contact_page = 'current'
	title = 'La Renaissance |  Contact'

	if request.method == 'POST':
		full_name = request.POST.get('full_name', None)
		subject = request.POST.get('subject', None)
		email = request.POST.get('email', None)
		tel = request.POST.get('phone', None)
		message = request.POST.get('message', None)

		Message.objects.create(full_name=full_name, email=email, tel=tel, subject=subject, message=message)

		get_company_details = CompanyDetails.objects.all()
		for company_data in get_company_details:
			company_email = company_data.email
			company_name = company_data.company_name

		sent_message = message+'\n\n'+full_name+'\nEmail: '+email+'\nTéléphone: '+tel

		to_company_email = [company_email]
		send_mail(subject, sent_message, settings.EMAIL_HOST_USER, to_company_email, fail_silently=True)

		to_user_email = [email]
		send_mail('Message envoyé à '+company_name, 'Sujet: '+subject+'\n\n'+sent_message, settings.EMAIL_HOST_USER, to_user_email, fail_silently=True)

		messages.success(request, "Message evoyé!")
		return HttpResponseRedirect(reverse('mainAppNamespace:HomeName'))

	global_context = get_global_data(request)

	page_context = {

		'title': title,
		'onContactPage': on_contact_page,
	}

	contact_context = global_context.copy()
	contact_context.update(page_context)

	return render(request, 'main_app/contact.html', contact_context)




# send contact message

def send_contact_message_view(request):

	if request.method == 'POST':
		full_name = request.POST.get('full_name', None)
		subject = request.POST.get('subject', None)
		email = request.POST.get('email', None)
		tel = request.POST.get('phone', None)
		message = request.POST.get('message', None)

		Message.objects.create(full_name=full_name, email=email, tel=tel, subject=subject, message=message)

		get_company_details = CompanyDetails.objects.all()
		for company_data in get_company_details:
			company_email = company_data.email
			company_name = company_data.company_name

		sent_message = message+'\n\n'+full_name+'\nEmail: '+email+'\nTéléphone: '+tel

		to_company_email = [company_email]
		send_mail(subject, sent_message, settings.EMAIL_HOST_USER, to_company_email, fail_silently=True)

		to_user_email = [email]
		send_mail('Message envoyé à '+company_name, 'Sujet: '+subject+'\n\n'+sent_message, settings.EMAIL_HOST_USER, to_user_email, fail_silently=True)

		messages.success(request, "Message evoyé!")
		return HttpResponseRedirect(reverse('mainAppNamespace:HomeName'))
	else:
		return HttpResponseRedirect(reverse('mainAppNamespace:HomeName'))




# request for appointment

def request_for_appointment_view(request):

	on_contact_page = 'current'
	title = 'La Renaissance |  Prendre rendez-vous'

	subject = request.GET.get('object', None)
	if subject == None:
		subject = ''
	
	global_context = get_global_data(request)

	page_context = {

		'title': title,
		'subject': subject,
		'onContactPage': on_contact_page,
	}

	request_for_appointment_context = global_context.copy()
	request_for_appointment_context.update(page_context)

	return render(request, 'main_app/request_for_appointment.html', request_for_appointment_context)




# send appointment request

def send_appointment_request_view(request):

	if request.method == 'POST':
		full_name = request.POST.get('full_name', None)
		subject = request.POST.get('subject', None)
		email = request.POST.get('email', None)
		tel = request.POST.get('phone', None)
		message = request.POST.get('message', None)

		Message.objects.create(full_name=full_name, email=email, tel=tel, subject=subject, message=message, is_rendez_vous=True)

		get_company_details = CompanyDetails.objects.all()
		for company_data in get_company_details:
			company_email = company_data.email
			company_name = company_data.company_name

		sent_message = message+'\n\n'+full_name+'\nEmail: '+email+'\nTéléphone: '+tel

		to_company_email = [company_email]
		send_mail(subject, sent_message, settings.EMAIL_HOST_USER, to_company_email, fail_silently=True)

		to_user_email = [email]
		send_mail('Demande de rendez-vous envoyé à '+company_name, 'Sujet: '+subject+'\n\n'+sent_message, settings.EMAIL_HOST_USER, to_user_email, fail_silently=True)

		messages.success(request, "Demande de rendez-vous evoyé!")
		return HttpResponseRedirect(reverse('mainAppNamespace:HomeName'))





# covid19

def covid19_view(request):

	title = 'La Renaissance | Covid-19'

	covid19_informations_list = Covid19.objects.all().filter(active=True, on_presentation=False)
	covid19_presentation_information = Covid19.objects.all().filter(active=True, on_presentation=True).order_by('-id')[:1]

	global_context = get_global_data(request)

	page_context = {

		'title': title,
		'covid19InformationsList': covid19_informations_list,
		'covid19PresentationInformation': covid19_presentation_information,
	}

	covid19_context = global_context.copy()
	covid19_context.update(page_context)

	return render(request, 'main_app/covid19.html', covid19_context)




# covid19 government information

def covid19_government_information_view(request):

	title = 'La Renaissance | covid-19 Informations Gouvernementales'

	get_covid19_government_informations_list = Covid19GovernmentInformation.objects.all().filter(active=True)

	paginator = Paginator(get_covid19_government_informations_list, 6)
	page = request.GET.get('page')
	try:
		covid19_government_informations_list = paginator.page(page)
	except PageNotAnInteger:
		covid19_government_informations_list = paginator.page(1)
	except EmptyPage:
		covid19_government_informations_list = paginator.page(paginator.num_pages)

	global_context = get_global_data(request)

	page_context = {

		'title': title,
		'covid19GovernmentInformationsList': covid19_government_informations_list,
		}

	covid19_government_information_context = global_context.copy()
	covid19_government_information_context.update(page_context)

	return render(request, 'main_app/covid19_government_information.html', covid19_government_information_context)



# covid19 government information details

def covid19_government_information_details_view(request, covid19_government_information_slug):

	on_media_page = 'current'
	title = 'La Renaissance | Covid-19 Information Gouvernementale'

	check_project = Covid19GovernmentInformation.objects.filter(slug=covid19_government_information_slug).count()
	if check_project == 0:
		messages.error(request, "Désolé, nous n'avons pas trouvé l'information!")
		return HttpResponseRedirect(reverse('mainAppNamespace:Covid19GovernmentInformationName'))
		
	requested_covid19_government_information = Covid19GovernmentInformation.objects.all().filter(slug=covid19_government_information_slug)

	global_context = get_global_data(request)

	page_context = {

		'title': title,
		'onMediaPage': on_media_page,
		'requestedCovid19GovernmentInformation': requested_covid19_government_information,
	}

	covid19_government_information_details_context = global_context.copy()
	covid19_government_information_details_context.update(page_context)

	return render(request, 'main_app/covid19_government_information_details.html', covid19_government_information_details_context)




# login redirect message

def login_redirect_view(request):

	redirect_message = request.GET.get('redirect_message')

	messages.error(request, redirect_message)
	return HttpResponseRedirect(reverse('mainAppNamespace:AuthentificationName'))





# authentification

def authentification_view(request):

	if request.user.is_authenticated:
		messages.info(request, 'Vous êtes connecté(e)!')
		return HttpResponseRedirect(reverse('mainAppNamespace:HomeName'))

	title = 'La Renaissance | Authentification'

	global_context = get_global_data(request)

	page_context = {

		'title': title,
	}

	authentification_context = global_context.copy()
	authentification_context.update(page_context)

	return render(request, 'main_app/authentification.html', authentification_context)





# login

def login_view(request):

	if request.method == 'POST':

		username = request.POST.get('username')
		password = request.POST.get('password')

		username = username.lower()

		try:
			user = User.objects.get(username=username)
		except:
			messages.error(request, 'Désolé, nous n\'avons pas trouvé votre nom d\'utilisateur. Veuillez vérifier votre nom d\'utilisateur et essayez!')
			return HttpResponseRedirect(reverse('mainAppNamespace:AuthentificationName'))

		user = authenticate(request, username=username, password=password)

		if user is None:
			messages.error(request, 'Erreur de connexion! Veuillez vérifier votre mot de passe et réessayer!')
		else:
			login(request, user)

			user_instance = User.objects.get(username=username)

			get_logged_user_data = UserAccount.objects.all().filter(user=user_instance)
			for logged_user_data in get_logged_user_data:
				request.session['logged_user_last_name'] = logged_user_data.first_name

		messages.success(request, 'Connexion réussie!')
		return HttpResponseRedirect(reverse('mainAppNamespace:HomeName'))
	else:
		return HttpResponseRedirect(reverse('mainAppNamespace:AuthentificationName'))





# create an account

def register_view(request):

	if request.method == 'POST':

		first_name = request.POST.get('first_name')
		last_name = request.POST.get('last_name')
		email = request.POST.get('email')
		tel = request.POST.get('tel')
		password = request.POST.get('password')
		password_confirmation = request.POST.get('password_confirmation')

		email = email.lower()

		check_user = User.objects.all().filter(username=email).count()
		if check_user != 0:
			messages.info(request, 'Vous êtes déjà inscrit. Veuillez vous connecter!')
			return HttpResponseRedirect(reverse('mainAppNamespace:AuthentificationName'))

		if password != password_confirmation:
			messages.info(request, 'Désolé, les deux mots de passe ne sont pas les même. Veuillez vérifier votre mot de passe et réessayer.!')
			return HttpResponseRedirect(reverse('mainAppNamespace:AuthentificationName'))

		User.objects.create_user(username=email, password=password)

		new_user_instance = User.objects.get(username=email)

		UserAccount.objects.create(user=new_user_instance, first_name=first_name, last_name=last_name, email=email, tel1=tel)
		
		messages.success(request, 'Vous êtes inscrit avec succès!')	
		return HttpResponseRedirect(reverse('mainAppNamespace:AuthentificationName'))
	else:
		return HttpResponseRedirect(reverse('mainAppNamespace:AuthentificationName'))



# logout

def logout_view(request):

	logout(request)

	messages.success(request, "Vous vous êtes déconnecté avec succès!")
	return HttpResponseRedirect(reverse('mainAppNamespace:HomeName'))




# privacy policy

def privacy_policy_view(request):

	title = 'La Renaissance | Confidentialité'

	global_context = get_global_data(request)

	page_context = {

		'title': title,
	}

	privacy_policy_context = global_context.copy()
	privacy_policy_context.update(page_context)

	return render(request, 'main_app/privacy_policy.html', privacy_policy_context)



# our partners

def our_partners_view(request):

	title = 'La Renaissance | Covid-19'

	partner_area = request.GET.get('partner_area', None)

	if partner_area == 'pharmacy':
		page_title = 'Nos Pharmacies Partenaires'
		get_our_partners_list = OurPartners.objects.all().filter(active=True, is_pharmacy=True)
	else:
		page_title = 'Nos Partenaires'
		get_our_partners_list = OurPartners.objects.all().filter(active=True)		

	paginator = Paginator(get_our_partners_list, 9)
	page = request.GET.get('page')
	try:
		our_partners_list = paginator.page(page)
	except PageNotAnInteger:
		our_partners_list = paginator.page(1)
	except EmptyPage:
		our_partners_list = paginator.page(paginator.num_pages)

	global_context = get_global_data(request)

	page_context = {

		'title': title,
		'pageTitle': page_title,
		'ourPartnersList': our_partners_list,
	}

	our_partners_context = global_context.copy()
	our_partners_context.update(page_context)

	return render(request, 'main_app/our_partners.html', our_partners_context)

