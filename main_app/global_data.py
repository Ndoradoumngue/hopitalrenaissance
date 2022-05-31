from .models import CompanyDetails, OurService, NewsCategory, News

def get_global_data(request):

	current_url = request.META.get('HTTP_HOST')+''+request.META.get('PATH_INFO') 
	
	company_details = CompanyDetails.objects.all()
	our_services_list = OurService.objects.all()
	news_categories_list = NewsCategory.objects.all().order_by('ranking')
	our_news_list = News.objects.all().filter(active=True).order_by('-id')[:3]

	for company_data in company_details:
		page_keywords = company_data.keywords
		page_description = company_data.short_description

	data_dict = {
		'pageKeywords': page_keywords,
		'currentURL': current_url,
		'pageDescription': page_description,
		'companyDetails': company_details,
		'newsCategoriesList': news_categories_list,
		'ourNewsList': our_news_list,
		'ourServicesList': our_services_list,
	}

	return data_dict

