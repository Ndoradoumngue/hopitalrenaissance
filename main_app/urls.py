from django.conf.urls import url
from django.conf.urls.static import static
from django.conf import settings
from django.urls import path
from main_app.views import *

app_name='main_app'

urlpatterns = [

    path('', home_view, name='HomeName'),
    path('newsletter-registration', newsletter_registration_view, name='NewsletterRegistrationName'),
    path('a-propos', about_us_view, name='AboutUsName'),
    path('historique', historique_view, name='HistoriqueName'),
    path('directions', directions_view, name='DirectionsName'),
    path('direction/<slug:direction_slug>', direction_view, name='DirectionName'),
    path('projets', projects_view, name='ProjectsName'),
    path('projet/<slug:projet_slug>', project_view, name='ProjectName'),
    path('service/<slug:service_slug>', service_view, name='ServiceName'),
    path('plage-horaires', timetable_view, name='TimetableName'),
    path('nos-medecins', our_team_view, name='OurTeamName'),
    path('medecin/<slug:member_slug>', member_view, name='MemberName'),
    path('preparer-son-sejour', prepare_admission_view, name='PrepareAdmissionName'),
    path('vie-quotidienne', daily_life_view, name='DailyLifeName'),
    path('droits-et-devoirs', rights_and_duties_view, name='RightsAndDutiesName'),
    path('media/<slug:category_slug>', media_view, name='MediaName'),
    path('gallerie', our_gallery_view, name='OurGalleryName'),
    path('article/<slug:news_slug>', article_view, name='ArticleName'),
    path('commenter-article/<slug:news_slug>', comment_news_view, name='CommentNewsName'),
    path('contact', contact_view, name='ContactName'),
    path('send-contact-message', send_contact_message_view, name='SendContactMessageName'),
    path('prendre-rendez-vous', request_for_appointment_view, name='RequestForAppointmentName'),
    path('send-appointment-request', send_appointment_request_view, name='SendAppointmentRequestName'),
    path('covid-19', covid19_view, name='Covid19Name'),
    path('covid-19-informations-gouvernementales', covid19_government_information_view, name='Covid19GovernmentInformationName'),
    path('covid-19-informations-gouvernementale/<slug:covid19_government_information_slug>', covid19_government_information_details_view, name='Covid19GovernmentInformationDetailsName'),
    path('login-redirect', login_redirect_view, name='LoginRedirectName'),
    path('authentification', authentification_view, name='AuthentificationName'),
    path('login', login_view, name='LoginName'),
    path('register', register_view, name='RegisterName'),
    path('deconnexion', logout_view, name='LogoutName'),
    path('politiques-de-confidentialite', privacy_policy_view, name='PrivacyPolicyName'),
    path('nos-partenaires', our_partners_view, name='OurPartnersName'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    # urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
