from datetime import datetime, timedelta, time
from django.db.models import Count, Sum, Q, F
from main_app.models import (UserAccount, Country, Town, Position, StaffMember)


def list_users(active, position_slug, is_patient, country_slug, town_slug, registered_from_date, registered_to_date, custom_search):
    
    
    ids_of_staff = []
    ids_of_users_by_position = []


    # default users

    default_users_ids = UserAccount.objects.values_list('id', flat=True)


    # get users by activity

    if active is None or active == '' or active == 'undefined' or active == 'null':
        ids_of_users_by_activity = default_users_ids
        activity_title = ''
    else:
        if active == 'true':
            activity_title = ' actif(ve)s'
            ids_of_users_by_activity = UserAccount.objects.filter(active=True).values_list('id', flat=True)
        elif active == 'false':
            activity_title = ' deactif(ve)s'
            ids_of_users_by_activity = UserAccount.objects.filter(active=False).values_list('id', flat=True)
        else:
            activity_title = ''
            ids_of_users_by_activity = default_users_ids



    # get users by profession

    if position_slug is None or position_slug == '' or position_slug == 'undefined' or position_slug == 'null':
        ids_of_users_by_position = default_users_ids
        profession_title = ''
    else:
        check_profession = Position.objects.filter(slug=position_slug).count()
        if check_profession == 0:
            profession_title = ''
            ids_of_users_by_position = default_users_ids[:0]
        else:
            profession_instance = Position.objects.get(slug=position_slug)

            get_staff_in_position = StaffMember.objects.all().filter(position=profession_instance)
            for staff_in_position_data in get_staff_in_position:
                ids_of_users_by_position.append(staff_in_position_data.user.id)

            get_profession_details = Position.objects.all().filter(slug=position_slug)
            for profession_data in get_profession_details:
                profession_title = profession_data.position



    # get users by type

    if is_patient is None or is_patient == '' or is_patient == 'undefined' or is_patient == 'null':
        ids_of_users_by_type = default_users_ids
        type_title = ' utilisateurs'
    else:
        get_staff = StaffMember.objects.all().filter(active=True)
        for staff_data in get_staff_in_position:
            ids_of_staff.append(staff_in_position_data.user.id)

        if is_patient == 'true':
            type_title = ' patients'
            ids_of_users_by_type = UserAccount.objects.exclude(id__in=ids_of_staff).values_list('id', flat=True)
        else:
            type_title = ' membre du staff'
            ids_of_users_by_type = ids_of_staff



    # get partners by country

    if country_slug is None or country_slug == '' or country_slug == 'undefined' or country_slug == 'null':
        ids_of_users_by_country = default_users_ids
        country_title = ''
    else:
        check_country = Country.objects.filter(slug=country_slug).count()
        if check_country == 0:
            country_title = ''
            ids_of_users_by_country = default_users_ids[:0]
        else:
            country_details = Country.objects.all().filter(slug=country_slug)
            for country_data in country_details:
                country_name = country_data.country_name

            country_title = '. Pays: '+country_name

            country_instance = Country.objects.get(slug=country_slug)

            ids_of_users_by_country = UserAccount.objects.filter(country=country_instance).values_list('id', flat=True)



    # get partners by town

    if town_slug is None or town_slug == '' or town_slug == 'undefined' or town_slug == 'null':
        town_title = ''
        ids_of_users_by_town = default_users_ids
    else:
        check_town = Town.objects.filter(slug=town_slug).count()
        if check_town == 0:
            town_title = ''
            ids_of_users_by_town = default_users_ids[:0]
        else:
            town_details = Town.objects.all().filter(slug=town_slug)
            for town_data in town_details:
                town_name = town_data.town_name

            town_title = '. Ville: '+town_name

            town_instance = Town.objects.get(slug=town_slug)

            ids_of_users_by_town = UserAccount.objects.filter(town=town_instance).values_list('id', flat=True)



    # get users registered from a date

    if registered_from_date is None or registered_from_date == '' or registered_from_date == 'undefined-undefined-undefined':
        ids_of_users_registered_from_a_date = default_users_ids
        registered_from_date_title = ''
    else:
        registered_from_date_title = ' enregistrés du '+str(registered_from_date)
        ids_of_users_registered_from_a_date = UserAccount.objects.filter(added_on_date_time__gte=registered_from_date).values_list('id', flat=True)



    # get users registered to a date

    if registered_to_date is None or registered_to_date == '' or registered_to_date == 'undefined-undefined-undefined':
        ids_of_users_registered_to_a_date = default_users_ids
        registered_to_date_title = ''
    else:
        if registered_from_date_title == '':
            registered_to_date_title = ' enregistrés avant le '+str(registered_to_date)
        else:
            registered_to_date_title = ' au '+str(registered_to_date)

        ids_of_users_registered_to_a_date = UserAccount.objects.filter(added_on_date_time__lte=registered_to_date).values_list('id', flat=True)



    # get users with search query

    if custom_search is None or custom_search == '' or custom_search == 'undefined' or custom_search == 'null':
        custom_search_title = ''
        ids_of_users_with_search_query = default_users_ids
    else:
        custom_search_title = '. Terme de recherche: [\''+custom_search+'\']'
        ids_of_users_with_search_query = UserAccount.objects.filter(Q(profession__icontains=custom_search) | Q(first_name__icontains=custom_search) | Q(last_name__icontains=custom_search) | Q(brief_bio__icontains=custom_search) | Q(id_number__icontains=custom_search) | Q(email__icontains=custom_search) | Q(tel1__icontains=custom_search)).values_list('id', flat=True)
    


    list_of_users_ids_to_return = list(set(ids_of_users_by_activity) & set(ids_of_users_by_position) & set(ids_of_users_by_type) & set(ids_of_users_by_country) & set(ids_of_users_by_town) & set(ids_of_users_registered_from_a_date) & set(ids_of_users_registered_to_a_date) & set(ids_of_users_with_search_query))

    returned_users_title = 'Liste des '+type_title+' '+profession_title+' '+activity_title+' '+registered_from_date_title+' '+registered_to_date_title+' '+town_title+' '+country_title+' '+custom_search_title
    
    return list_of_users_ids_to_return, returned_users_title

