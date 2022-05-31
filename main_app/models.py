# coding=utf-8

import random
from ckeditor.fields import RichTextField
from django.db import models
from django.db.models.signals import pre_save
from django.utils.text import slugify
from django.contrib.auth.models import User
from .validators import validate_file_extension


# Country

class Country(models.Model):
    country_name = models.CharField(max_length=50)
    country_code = models.CharField(max_length=50)
    slug = models.SlugField(max_length=5000, null=True, blank=True, unique=True)
    added_on_date_time = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return self.country_name

def create_country_slug(instance, new_slug=None):
    slug = slugify(instance.country_name)
    if new_slug is not None:
        slug = new_slug
    qs = Country.objects.filter(slug=slug).order_by('id')
    exists = qs.exists()
    if exists:
        new_slug = '%s-%s' % (slug, qs.first().id)
        return create_country_slug(instance, new_slug=new_slug)
    return slug

def presave_country(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = create_country_slug(instance)

pre_save.connect(presave_country, sender=Country)


# Town

class Town(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    town_name = models.CharField(max_length=50)
    town_code = models.CharField(max_length=50)
    slug = models.SlugField(max_length=5000, null=True, blank=True, unique=True)
    added_on_date_time = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return self.town_name

def create_town_slug(instance, new_slug=None):
    slug = slugify(instance.town_name)
    if new_slug is not None:
        slug = new_slug
    qs = Town.objects.filter(slug=slug).order_by('id')
    exists = qs.exists()
    if exists:
        new_slug = '%s-%s' % (slug, qs.first().id)
        return create_town_slug(instance, new_slug=new_slug)
    return slug

def presave_town(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = create_town_slug(instance)

pre_save.connect(presave_town, sender=Town)


# user account

class UserAccount(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    id_number = models.CharField(max_length=50, null=True, blank=True)
    first_name = models.CharField(max_length=50, null=True, blank=True)
    middle_name = models.CharField(max_length=50, null=True, blank=True)
    last_name = models.CharField(max_length=50, null=True, blank=True)
    dob = models.DateField(blank=True, null=True)    
    profile_image = models.FileField(validators=[validate_file_extension], null=True, blank=True)
    email = models.CharField(max_length=30, null=True, blank=True)
    tel1 = models.CharField(max_length=20, null=True, blank=True)
    tel2 = models.CharField(max_length=20, null=True, blank=True)
    country = models.ForeignKey(Country, on_delete=models.CASCADE, null=True, blank=True)
    town = models.ForeignKey(Town, on_delete=models.CASCADE, null=True, blank=True)
    address = models.CharField(max_length=150, null=True, blank=True)
    brief_bio = models.CharField(max_length=500, null=True, blank=True)
    profession = models.CharField(max_length=50, null=True, blank=True)
    facebook_profile_link = models.URLField(null=True, blank=True)
    linkedin_profile_link = models.URLField(null=True, blank=True)
    twitter_profile_link = models.URLField(null=True, blank=True)
    youtube_profile_link = models.URLField(null=True, blank=True)
    active = models.BooleanField(default=True)
    show = models.BooleanField(default=True)
    is_doctor = models.BooleanField(default=False)
    registered_for_newsletter = models.BooleanField(default=False)
    slug = models.SlugField(max_length=5000, null=True, blank=True, unique=True)
    deleted = models.BooleanField(default=False)
    deleted_on_date_time = models.DateTimeField(blank=True, null=True)
    added_on_date_time = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return self.first_name

def create_user_account_slug(instance, new_slug=None):
    slug = slugify(instance.first_name)
    if new_slug is not None:
        slug = new_slug
    qs = UserAccount.objects.filter(slug=slug).order_by('id')
    exists = qs.exists()
    if exists:
        new_slug = '%s-%s' % (slug, qs.first().id)
        return create_user_account_slug(instance, new_slug=new_slug)
    return slug

def presave_user_account(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = create_user_account_slug(instance)

pre_save.connect(presave_user_account, sender=UserAccount)


# Position

class Position(models.Model):
    position = models.CharField(max_length=50)
    active = models.BooleanField(default=False)
    slug = models.SlugField(max_length=5000, null=True, blank=True, unique=True)
    added_on_date_time = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return self.position

def create_position_slug(instance, new_slug=None):
    slug = slugify(instance.position)
    if new_slug is not None:
        slug = new_slug
    qs = Position.objects.filter(slug=slug).order_by('id')
    exists = qs.exists()
    if exists:
        new_slug = '%s-%s' % (slug, qs.first().id)
        return create_position_slug(instance, new_slug=new_slug)
    return slug

def presave_position(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = create_position_slug(instance)

pre_save.connect(presave_position, sender=Position)


# Staff member

class StaffMember(models.Model):
    employee_id = models.CharField(max_length=50)
    user = models.ForeignKey(UserAccount, on_delete=models.CASCADE)
    position = models.ForeignKey(Position, on_delete=models.CASCADE)
    active = models.BooleanField(default=False)
    slug = models.SlugField(max_length=5000, null=True, blank=True, unique=True)
    added_on_date_time = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return self.employee_id

def create_staff_member_slug(instance, new_slug=None):
    slug = slugify(instance.employee_id)
    if new_slug is not None:
        slug = new_slug
    qs = StaffMember.objects.filter(slug=slug).order_by('id')
    exists = qs.exists()
    if exists:
        new_slug = '%s-%s' % (slug, qs.first().id)
        return create_staff_member_slug(instance, new_slug=new_slug)
    return slug

def presave_staff_member(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = create_staff_member_slug(instance)

pre_save.connect(presave_staff_member, sender=StaffMember)


# company details

class CompanyDetails(models.Model):
    company_name = models.CharField(max_length=50)
    slogan = models.CharField(max_length=100)
    company_description = RichTextField()
    short_description = models.CharField(max_length=500)
    keywords = models.CharField(max_length=500)
    company_logo = models.FileField(validators=[validate_file_extension])
    about_image = models.FileField(validators=[validate_file_extension])
    presentation_image = models.FileField(validators=[validate_file_extension])
    historique = RichTextField()
    historique_image = models.FileField(validators=[validate_file_extension])
    admission_preparation = RichTextField()
    daily_life = RichTextField()
    rights_and_duties = RichTextField()
    privacy_policy = RichTextField()
    email = models.EmailField(max_length=50)
    tel1 = models.CharField(max_length=20)
    tel_reception = models.CharField(max_length=20, null=True, blank=True)
    tel_lab = models.CharField(max_length=20, null=True, blank=True)
    mission = models.CharField(max_length=500, null=True, blank=True)
    vision = models.CharField(max_length=250, null=True, blank=True)
    values = models.CharField(max_length=250, null=True, blank=True)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    town = models.ForeignKey(Town, on_delete=models.CASCADE)
    address = models.CharField(max_length=150, null=True, blank=True)
    director = models.ForeignKey(UserAccount, on_delete=models.CASCADE)
    number_of_doctors = models.IntegerField()
    number_of_beds = models.IntegerField()
    number_of_internal_patients = models.IntegerField()
    number_of_paramedics = models.IntegerField()
    facebook_profile_link = models.URLField(null=True, blank=True)
    linkedin_profile_link = models.URLField(null=True, blank=True)
    twitter_profile_link = models.URLField(null=True, blank=True)
    youtube_profile_link = models.URLField(null=True, blank=True)
    slug = models.SlugField(max_length=5000, null=True, blank=True, unique=True)
    added_on_date_time = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return self.company_name

def create_company_details_slug(instance, new_slug=None):
    slug = slugify(instance.company_name)
    if new_slug is not None:
        slug = new_slug
    qs = CompanyDetails.objects.filter(slug=slug).order_by('id')
    exists = qs.exists()
    if exists:
        new_slug = '%s-%s' % (slug, qs.first().id)
        return create_company_details_slug(instance, new_slug=new_slug)
    return slug

def presave_company_details(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = create_company_details_slug(instance)

pre_save.connect(presave_company_details, sender=CompanyDetails)


# directions

class Direction(models.Model):
    name = models.CharField(max_length=50)
    fontawesome_icon = models.CharField(max_length=50)
    image = models.FileField(validators=[validate_file_extension])
    description = RichTextField()
    director = models.ForeignKey(UserAccount, on_delete=models.CASCADE, related_name="director", null=True, blank=True)
    deputy_director = models.ForeignKey(UserAccount, on_delete=models.CASCADE, related_name="deputy_director", null=True, blank=True)
    added_by = models.ForeignKey(UserAccount, on_delete=models.CASCADE, related_name="direction_added_by", null=True, blank=True)
    active = models.BooleanField(default=True)
    slug = models.SlugField(max_length=5000, null=True, blank=True, unique=True)
    added_on_date_time = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return self.name

def create_direction_slug(instance, new_slug=None):
    slug = slugify(instance.name)
    if new_slug is not None:
        slug = new_slug
    qs = Direction.objects.filter(slug=slug).order_by('id')
    exists = qs.exists()
    if exists:
        new_slug = '%s-%s' % (slug, qs.first().id)
        return create_direction_slug(instance, new_slug=new_slug)
    return slug

def presave_direction(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = create_direction_slug(instance)

pre_save.connect(presave_direction, sender=Direction)


# days of the week

class DayOfTheWeek(models.Model):
    day = models.CharField(max_length=50)
    slug = models.SlugField(max_length=5000, null=True, blank=True, unique=True)
    added_on_date_time = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return self.day

def create_day_of_the_week_slug(instance, new_slug=None):
    slug = slugify(instance.day)
    if new_slug is not None:
        slug = new_slug
    qs = DayOfTheWeek.objects.filter(slug=slug).order_by('id')
    exists = qs.exists()
    if exists:
        new_slug = '%s-%s' % (slug, qs.first().id)
        return create_day_of_the_week_slug(instance, new_slug=new_slug)
    return slug

def presave_day_of_the_week(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = create_day_of_the_week_slug(instance)

pre_save.connect(presave_day_of_the_week, sender=DayOfTheWeek)


# working hour

class WorkingHour(models.Model):
    hour = models.CharField(max_length=50)
    slug = models.SlugField(max_length=5000, null=True, blank=True, unique=True)
    added_on_date_time = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return self.hour

def create_working_hour_slug(instance, new_slug=None):
    slug = slugify(instance.hour)
    if new_slug is not None:
        slug = new_slug
    qs = WorkingHour.objects.filter(slug=slug).order_by('id')
    exists = qs.exists()
    if exists:
        new_slug = '%s-%s' % (slug, qs.first().id)
        return create_working_hour_slug(instance, new_slug=new_slug)
    return slug

def presave_working_hour(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = create_working_hour_slug(instance)

pre_save.connect(presave_working_hour, sender=WorkingHour)


# timetable

class Timetable(models.Model):
    day = models.ForeignKey(DayOfTheWeek, on_delete=models.CASCADE)
    hour = models.ForeignKey(WorkingHour, on_delete=models.CASCADE)
    task = models.CharField(max_length=150, null=True, blank=True)
    doctors = models.CharField(max_length=150, null=True, blank=True)
    ranking = models.IntegerField()
    is_break_time = models.BooleanField(default=False)
    responsable = models.ForeignKey(UserAccount, on_delete=models.CASCADE)
    slug = models.SlugField(max_length=5000, null=True, blank=True, unique=True)
    added_on_date_time = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return self.slug

def create_timetable_slug(instance, new_slug=None):
    
    day_name = instance.day.day
    hour_name = instance.hour.hour

    formed_slug = day_name+'-'+hour_name

    slug = slugify(formed_slug)
    if new_slug is not None:
        slug = new_slug
    qs = Timetable.objects.filter(slug=slug).order_by('id')
    exists = qs.exists()
    if exists:
        new_slug = '%s-%s' % (slug, qs.first().id)
        return create_timetable_slug(instance, new_slug=new_slug)
    return slug

def presave_timetable(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = create_timetable_slug(instance)

pre_save.connect(presave_timetable, sender=Timetable)


# our partners

class OurPartners(models.Model):
    company_name = models.CharField(max_length=50)
    company_logo = models.FileField(validators=[validate_file_extension])
    email = models.EmailField(max_length=50, null=True, blank=True)
    tel1 = models.CharField(max_length=20, null=True, blank=True)
    tel2 = models.CharField(max_length=20, null=True, blank=True)
    address = models.CharField(max_length=150, null=True, blank=True)
    country = models.ForeignKey(Country, on_delete=models.CASCADE, null=True, blank=True)
    town = models.ForeignKey(Town, on_delete=models.CASCADE, null=True, blank=True)
    facebook_profile_link = models.URLField(null=True, blank=True)
    linkedin_profile_link = models.URLField(null=True, blank=True)
    twitter_profile_link = models.URLField(null=True, blank=True)
    profile_website_link = models.URLField(null=True, blank=True)
    representative = models.ForeignKey(UserAccount, on_delete=models.CASCADE, related_name="company_representative", null=True, blank=True)
    added_by = models.ForeignKey(UserAccount, on_delete=models.CASCADE, related_name="company_added_by", null=True, blank=True)
    is_pharmacy = models.BooleanField(default=False)
    active = models.BooleanField(default=True)
    slug = models.SlugField(max_length=5000, null=True, blank=True, unique=True)
    added_on_date_time = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return self.company_name

def create_our_partners_slug(instance, new_slug=None):
    slug = slugify(instance.company_name)
    if new_slug is not None:
        slug = new_slug
    qs = OurPartners.objects.filter(slug=slug).order_by('id')
    exists = qs.exists()
    if exists:
        new_slug = '%s-%s' % (slug, qs.first().id)
        return create_our_partners_slug(instance, new_slug=new_slug)
    return slug

def presave_our_partners(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = create_our_partners_slug(instance)

pre_save.connect(presave_our_partners, sender=OurPartners)


# Slider

class Slider(models.Model):
    title = models.CharField(max_length=57)
    sub_title = models.CharField(max_length=100)
    rank = models.IntegerField()
    image = models.FileField(validators=[validate_file_extension])
    active = models.BooleanField(default=True)
    slug = models.SlugField(max_length=5000, null=True, blank=True, unique=True)
    added_on_date_time = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return self.title

def create_slider_slug(instance, new_slug=None):
    slug = slugify(instance.title)
    if new_slug is not None:
        slug = new_slug
    qs = Slider.objects.filter(slug=slug).order_by('id')
    exists = qs.exists()
    if exists:
        new_slug = '%s-%s' % (slug, qs.first().id)
        return create_slider_slug(instance, new_slug=new_slug)
    return slug

def presave_slider(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = create_slider_slug(instance)

pre_save.connect(presave_slider, sender=Slider)


# Testimony

class Testimony(models.Model):
	testifier = models.ForeignKey(UserAccount, on_delete=models.CASCADE)
	review = models.CharField(max_length=250)
	active = models.BooleanField(default=True)
	first_in_the_list = models.BooleanField(default=False)
	slug = models.SlugField(max_length=5000, null=True, blank=True, unique=True)
	added_on_date_time = models.DateTimeField(auto_now=False, auto_now_add=True)

	def __str__(self):
		return self.slug

	generated_code_from = "abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
	code_length = 30
	generated_slug = ""

	for i in range(code_length):
		next_index = random.randrange(len(generated_code_from))
		generated_slug = generated_slug + generated_code_from[next_index]

def create_testimony_slug(instance, new_slug=None):
	slug = slugify(instance.generated_slug)
	if new_slug is not None:
		slug = new_slug
	qs = Testimony.objects.filter(slug=slug).order_by('id')
	exists = qs.exists()
	if exists:
		new_slug = '%s-%s' % (slug, qs.first().id)
		return create_testimony_slug(instance, new_slug=new_slug)
	return slug

def presave_testimony(sender, instance, *args, **kwargs):
	if not instance.slug:
		instance.slug = create_testimony_slug(instance)

pre_save.connect(presave_testimony, sender=Testimony)


# News category

class NewsCategory(models.Model):
    category = models.CharField(max_length=50)
    ranking = models.IntegerField()
    active = models.BooleanField(default=True)
    slug = models.SlugField(max_length=5000, null=True, blank=True, unique=True)
    posted_on_date_time = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return self.category

def create_news_category_slug(instance, new_slug=None):
    slug = slugify(instance.category)
    if new_slug is not None:
        slug = new_slug
    qs = NewsCategory.objects.filter(slug=slug).order_by('id')
    exists = qs.exists()
    if exists:
        new_slug = '%s-%s' % (slug, qs.first().id)
        return create_news_category_slug(instance, new_slug=new_slug)
    return slug

def presave_news_category(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = create_news_category_slug(instance)

pre_save.connect(presave_news_category, sender=NewsCategory)


# News

class News(models.Model):
    category = models.ForeignKey(NewsCategory, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    short_description = models.CharField(max_length=250)
    news = RichTextField()
    image = models.FileField()
    posted_by = models.ForeignKey(UserAccount, on_delete=models.CASCADE)
    number_of_comments = models.IntegerField(default=0)
    active = models.BooleanField(default=True)
    slug = models.SlugField(max_length=5000, null=True, blank=True, unique=True)
    posted_on_date_time = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return self.title

def create_news_slug(instance, new_slug=None):
	slug = slugify(instance.title)
	if new_slug is not None:
		slug = new_slug
	qs = News.objects.filter(slug=slug).order_by('id')
	exists = qs.exists()
	if exists:
		new_slug = '%s-%s' % (slug, qs.first().id)
		return create_news_slug(instance, new_slug=new_slug)
	return slug

def presave_news(sender, instance, *args, **kwargs):
	if not instance.slug:
		instance.slug = create_news_slug(instance)

pre_save.connect(presave_news, sender=News)


# News Comments

class NewsComment(models.Model):
	news = models.ForeignKey(News, on_delete=models.CASCADE, null=True, blank=True)
	commented_by = models.ForeignKey(UserAccount, on_delete=models.CASCADE, null=True, blank=True)
	comment = models.CharField(max_length=250)
	slug = models.SlugField(max_length=5000, null=True, blank=True, unique=True)
	added_on_date_time = models.DateTimeField(auto_now=False, auto_now_add=True)

	def __str__(self):
		return self.slug

	generated_code_from = "abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
	code_length = 30
	generated_slug = ""

	for i in range(code_length):
		next_index = random.randrange(len(generated_code_from))
		generated_slug = generated_slug + generated_code_from[next_index]

def create_news_comment_slug(instance, new_slug=None):
	slug = slugify(instance.generated_slug)
	if new_slug is not None:
		slug = new_slug
	qs = NewsComment.objects.filter(slug=slug).order_by('id')
	exists = qs.exists()
	if exists:
		new_slug = '%s-%s' % (slug, qs.first().id)
		return create_news_comment_slug(instance, new_slug=new_slug)
	return slug

def presave_news_comment(sender, instance, *args, **kwargs):
	if not instance.slug:
		instance.slug = create_news_comment_slug(instance)

pre_save.connect(presave_news_comment, sender=NewsComment)


# Gallery Category

class GalleryCategory(models.Model):
	category = models.CharField(max_length=50)
	active = models.BooleanField(default=True)
	slug = models.SlugField(max_length=5000, null=True, blank=True, unique=True)
	added_on_date_time = models.DateTimeField(auto_now=False, auto_now_add=True)

	def __str__(self):
		return self.category

def create_gallery_category_slug(instance, new_slug=None):
	slug = slugify(instance.category)
	if new_slug is not None:
		slug = new_slug
	qs = GalleryCategory.objects.filter(slug=slug).order_by('id')
	exists = qs.exists()
	if exists:
		new_slug = '%s-%s' % (slug, qs.first().id)
		return create_gallery_category_slug(instance, new_slug=new_slug)
	return slug

def presave_gallery_category(sender, instance, *args, **kwargs):
	if not instance.slug:
		instance.slug = create_gallery_category_slug(instance)

pre_save.connect(presave_gallery_category, sender=GalleryCategory)


# Gallery

class Gallery(models.Model):
	category = models.ForeignKey(GalleryCategory, on_delete=models.CASCADE)
	title = models.CharField(max_length=50)
	image = models.FileField()
	active = models.BooleanField(default=True)
	slug = models.SlugField(max_length=5000, null=True, blank=True, unique=True)
	added_on_date_time = models.DateTimeField(auto_now=False, auto_now_add=True)

	def __str__(self):
		return self.title

def create_gallery_slug(instance, new_slug=None):
	slug = slugify(instance.title)
	if new_slug is not None:
		slug = new_slug
	qs = Gallery.objects.filter(slug=slug).order_by('id')
	exists = qs.exists()
	if exists:
		new_slug = '%s-%s' % (slug, qs.first().id)
		return create_gallery_slug(instance, new_slug=new_slug)
	return slug

def presave_gallery(sender, instance, *args, **kwargs):
	if not instance.slug:
		instance.slug = create_gallery_slug(instance)

pre_save.connect(presave_gallery, sender=Gallery)


# Our Services

class OurService(models.Model):
    title = models.CharField(max_length=50)
    image = models.FileField()
    short_description = models.CharField(max_length=100)
    description = RichTextField()
    active = models.BooleanField(default=True)
    slug = models.SlugField(max_length=5000, null=True, blank=True, unique=True)
    added_on_date_time = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return self.title

def create_our_service_slug(instance, new_slug=None):
	slug = slugify(instance.title)
	if new_slug is not None:
		slug = new_slug
	qs = OurService.objects.filter(slug=slug).order_by('id')
	exists = qs.exists()
	if exists:
		new_slug = '%s-%s' % (slug, qs.first().id)
		return create_our_service_slug(instance, new_slug=new_slug)
	return slug

def presave_our_service(sender, instance, *args, **kwargs):
	if not instance.slug:
		instance.slug = create_our_service_slug(instance)

pre_save.connect(presave_our_service, sender=OurService)


# Events

class Event(models.Model):
	formateur = models.ForeignKey(UserAccount, on_delete=models.CASCADE)
	title = models.CharField(max_length=75)
	from_datetime = models.DateTimeField()
	to_datetime = models.DateTimeField()
	venue = models.CharField(max_length=150)
	brief_description = models.CharField(max_length=150)
	description = RichTextField()
	image = models.FileField()
	seats_limit = models.IntegerField()
	image_thumb = models.FileField()
	upcoming = models.BooleanField(default=True)
	reached_percecntage_goal = models.IntegerField(default=0)
	slug = models.SlugField(max_length=5000, null=True, blank=True, unique=True)
	added_on_date_time = models.DateTimeField(auto_now=False, auto_now_add=True)

	def __str__(self):
		return self.title

def create_event_slug(instance, new_slug=None):
	slug = slugify(instance.title)
	if new_slug is not None:
		slug = new_slug
	qs = Event.objects.filter(slug=slug).order_by('id')
	exists = qs.exists()
	if exists:
		new_slug = '%s-%s' % (slug, qs.first().id)
		return create_event_slug(instance, new_slug=new_slug)
	return slug

def presave_event(sender, instance, *args, **kwargs):
	if not instance.slug:
		instance.slug = create_event_slug(instance)

pre_save.connect(presave_event, sender=Event)


# Event Participants

class EventParticipant(models.Model):
	event = models.ForeignKey(Event, on_delete=models.CASCADE, null=True, blank=True)
	participant = models.ForeignKey(UserAccount, on_delete=models.CASCADE, null=True, blank=True)
	message = models.CharField(max_length=250)
	slug = models.SlugField(max_length=5000, null=True, blank=True, unique=True)
	registered_on_date_time = models.DateTimeField(auto_now=False, auto_now_add=True)

	def __str__(self):
		return self.slug

	generated_code_from = "abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
	code_length = 30
	generated_slug = ""

	for i in range(code_length):
		next_index = random.randrange(len(generated_code_from))
		generated_slug = generated_slug + generated_code_from[next_index]

def create_event_participant_slug(instance, new_slug=None):
	slug = slugify(instance.generated_slug)
	if new_slug is not None:
		slug = new_slug
	qs = EventParticipant.objects.filter(slug=slug).order_by('id')
	exists = qs.exists()
	if exists:
		new_slug = '%s-%s' % (slug, qs.first().id)
		return create_event_participant_slug(instance, new_slug=new_slug)
	return slug

def presave_event_participant(sender, instance, *args, **kwargs):
	if not instance.slug:
		instance.slug = create_event_participant_slug(instance)

pre_save.connect(presave_event_participant, sender=EventParticipant)


# Event Comments

class EventComment(models.Model):
	event = models.ForeignKey(Event, on_delete=models.CASCADE, null=True, blank=True)
	commented_by = models.ForeignKey(UserAccount, on_delete=models.CASCADE, null=True, blank=True)
	comment = models.CharField(max_length=250)
	slug = models.SlugField(max_length=5000, null=True, blank=True, unique=True)
	added_on_date_time = models.DateTimeField(auto_now=False, auto_now_add=True)

	def __str__(self):
		return self.slug

	generated_code_from = "abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
	code_length = 30
	generated_slug = ""

	for i in range(code_length):
		next_index = random.randrange(len(generated_code_from))
		generated_slug = generated_slug + generated_code_from[next_index]

def create_event_comment_slug(instance, new_slug=None):
	slug = slugify(instance.generated_slug)
	if new_slug is not None:
		slug = new_slug
	qs = EventComment.objects.filter(slug=slug).order_by('id')
	exists = qs.exists()
	if exists:
		new_slug = '%s-%s' % (slug, qs.first().id)
		return create_event_comment_slug(instance, new_slug=new_slug)
	return slug

def presave_event_comment(sender, instance, *args, **kwargs):
	if not instance.slug:
		instance.slug = create_event_comment_slug(instance)

pre_save.connect(presave_event_comment, sender=EventComment)


# Our Project

class OurProject(models.Model):
    title = models.CharField(max_length=150)
    image = models.FileField(validators=[validate_file_extension])
    description = RichTextField()
    active = models.BooleanField(default=True)
    added_by = models.ForeignKey(UserAccount, on_delete=models.CASCADE, null=True, blank=True)
    slug = models.SlugField(max_length=5000, null=True, blank=True, unique=True)
    added_on_date_time = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return self.title

def create_our_project_slug(instance, new_slug=None):
    slug = slugify(instance.title)
    if new_slug is not None:
        slug = new_slug
    qs = OurProject.objects.filter(slug=slug).order_by('id')
    exists = qs.exists()
    if exists:
        new_slug = '%s-%s' % (slug, qs.first().id)
        return create_our_project_slug(instance, new_slug=new_slug)
    return slug

def presave_our_project(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = create_our_project_slug(instance)

pre_save.connect(presave_our_project, sender=OurProject)


# Covid19

class Covid19(models.Model):
    title = models.CharField(max_length=100)
    description = RichTextField()
    file = models.FileField(null=True, blank=True)
    is_image = models.BooleanField(default=False)
    on_presentation = models.BooleanField(default=False)
    active = models.BooleanField(default=True)
    slug = models.SlugField(max_length=5000, null=True, blank=True, unique=True)
    sent_on_on_date_time = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return self.title

def create_covid19_slug(instance, new_slug=None):
	slug = slugify(instance.title)
	if new_slug is not None:
		slug = new_slug
	qs = Covid19.objects.filter(slug=slug).order_by('id')
	exists = qs.exists()
	if exists:
		new_slug = '%s-%s' % (slug, qs.first().id)
		return create_covid19_slug(instance, new_slug=new_slug)
	return slug

def presave_covid19(sender, instance, *args, **kwargs):
	if not instance.slug:
		instance.slug = create_covid19_slug(instance)

pre_save.connect(presave_covid19, sender=Covid19)


# Covid19 Government Information

class Covid19GovernmentInformation(models.Model):
    title = models.CharField(max_length=100)
    short_description = models.CharField(max_length=500)
    description = RichTextField()
    image = models.FileField(validators=[validate_file_extension])
    active = models.BooleanField(default=True)
    slug = models.SlugField(max_length=5000, null=True, blank=True, unique=True)
    sent_on_on_date_time = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return self.title

def create_covid19_government_information_slug(instance, new_slug=None):
    slug = slugify(instance.title)
    if new_slug is not None:
        slug = new_slug
    qs = Covid19GovernmentInformation.objects.filter(slug=slug).order_by('id')
    exists = qs.exists()
    if exists:
        new_slug = '%s-%s' % (slug, qs.first().id)
        return create_covid19_government_information_slug(instance, new_slug=new_slug)
    return slug

def presave_covid19_government_information(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = create_covid19_government_information_slug(instance)

pre_save.connect(presave_covid19_government_information, sender=Covid19GovernmentInformation)



# Messages

class Message(models.Model):
    full_name = models.CharField(max_length=100)
    # from_user_last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=50, null=True, blank=True)
    tel = models.CharField(max_length=50, null=True, blank=True)
    subject = models.CharField(max_length=50, null=True, blank=True)
    is_rendez_vous = models.BooleanField(default=False)
    message = RichTextField()
    attended = models.BooleanField(default=False)
    slug = models.SlugField(max_length=5000, null=True, blank=True, unique=True)
    sent_on_on_date_time = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return self.full_name

def create_message_slug(instance, new_slug=None):
    slug = slugify(instance.full_name)
    if new_slug is not None:
        slug = new_slug
    qs = Message.objects.filter(slug=slug).order_by('id')
    exists = qs.exists()
    if exists:
        new_slug = '%s-%s' % (slug, qs.first().id)
        return create_message_slug(instance, new_slug=new_slug)
    return slug

def presave_message(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = create_message_slug(instance)

pre_save.connect(presave_message, sender=Message)

