from django.contrib import admin
from .models import (Country, Town, UserAccount, Position, StaffMember, CompanyDetails, OurPartners, Slider, 
	Testimony, NewsCategory, News, NewsComment, GalleryCategory, Gallery, OurService, Event, EventParticipant, 
	EventComment, Message, OurProject, Direction, DayOfTheWeek, WorkingHour, Timetable, Covid19, 
	Covid19GovernmentInformation)

admin.site.register(Country)

admin.site.register(Town)

admin.site.register(UserAccount)

admin.site.register(Position)

admin.site.register(StaffMember)

admin.site.register(CompanyDetails)

admin.site.register(OurPartners)

admin.site.register(Slider)

admin.site.register(Testimony)

admin.site.register(NewsCategory)

admin.site.register(News)

admin.site.register(NewsComment)

admin.site.register(GalleryCategory)

admin.site.register(Gallery)

admin.site.register(OurService)

admin.site.register(Event)

admin.site.register(EventParticipant)

admin.site.register(EventComment)

admin.site.register(Message)

admin.site.register(OurProject)

admin.site.register(Direction)

admin.site.register(DayOfTheWeek)

admin.site.register(WorkingHour)

admin.site.register(Timetable)

admin.site.register(Covid19)

admin.site.register(Covid19GovernmentInformation)
