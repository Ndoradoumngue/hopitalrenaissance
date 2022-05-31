import hashlib
import random
import string
import time
import requests
import base64
from datetime import datetime, time, timedelta
from twilio.rest import Client, TwilioRestClient
# get server timezone
from requests.auth import HTTPBasicAuth
from .models import CompanyDetails


# generate random string

def generate_random_string():
    characters = string.ascii_letters + string.digits + string.punctuation
    random_string = ''.join(random.choice(characters) for i in range(8))

    return random_string



# get local timezone

def get_local_timezone():
    if time.daylight:
        offset_hour = time.altzone / 3600
    else:
        offset_hour = time.timezone / 3600

    return offset_hour


# get server timezone

def add_remove_days_to_date(start_date, days_to_add):
    needed_date = start_date + timedelta(days=int(days_to_add))

    return needed_date


# get server timezone

def test_int(integer):
    try:
        int(integer)
        result = '1'
    except Exception as e:
        result = '0'

    return result

   
# check safaricom number

def check_safaricom_phone_number(number):
    safaricom_prefixes = []

    safaricom_prefixes.append('0701')
    safaricom_prefixes.append('0702')
    safaricom_prefixes.append('0703')
    safaricom_prefixes.append('0704')
    safaricom_prefixes.append('0705')
    safaricom_prefixes.append('0706')
    safaricom_prefixes.append('0707')
    safaricom_prefixes.append('0708')
    safaricom_prefixes.append('0709')
    safaricom_prefixes.append('0710')
    safaricom_prefixes.append('0711')
    safaricom_prefixes.append('0712')
    safaricom_prefixes.append('0713')
    safaricom_prefixes.append('0714')
    safaricom_prefixes.append('0715')
    safaricom_prefixes.append('0716')
    safaricom_prefixes.append('0717')
    safaricom_prefixes.append('0718')
    safaricom_prefixes.append('0719')
    safaricom_prefixes.append('0720')
    safaricom_prefixes.append('0721')
    safaricom_prefixes.append('0722')
    safaricom_prefixes.append('0723')
    safaricom_prefixes.append('0724')
    safaricom_prefixes.append('0725')
    safaricom_prefixes.append('0726')
    safaricom_prefixes.append('0727')
    safaricom_prefixes.append('0728')
    safaricom_prefixes.append('0729')

    safaricom_prefixes.append('701')
    safaricom_prefixes.append('702')
    safaricom_prefixes.append('703')
    safaricom_prefixes.append('704')
    safaricom_prefixes.append('705')
    safaricom_prefixes.append('706')
    safaricom_prefixes.append('707')
    safaricom_prefixes.append('708')
    safaricom_prefixes.append('709')
    safaricom_prefixes.append('710')
    safaricom_prefixes.append('711')
    safaricom_prefixes.append('712')
    safaricom_prefixes.append('713')
    safaricom_prefixes.append('714')
    safaricom_prefixes.append('715')
    safaricom_prefixes.append('716')
    safaricom_prefixes.append('717')
    safaricom_prefixes.append('718')
    safaricom_prefixes.append('719')
    safaricom_prefixes.append('720')
    safaricom_prefixes.append('721')
    safaricom_prefixes.append('722')
    safaricom_prefixes.append('723')
    safaricom_prefixes.append('724')
    safaricom_prefixes.append('725')
    safaricom_prefixes.append('726')
    safaricom_prefixes.append('727')
    safaricom_prefixes.append('728')
    safaricom_prefixes.append('729')


    safaricom_prefixes.append('+254701')
    safaricom_prefixes.append('+254702')
    safaricom_prefixes.append('+254703')
    safaricom_prefixes.append('+254704')
    safaricom_prefixes.append('+254705')
    safaricom_prefixes.append('+254706')
    safaricom_prefixes.append('+254707')
    safaricom_prefixes.append('+254708')
    safaricom_prefixes.append('+254709')
    safaricom_prefixes.append('+254710')
    safaricom_prefixes.append('+254711')
    safaricom_prefixes.append('+254712')
    safaricom_prefixes.append('+254713')
    safaricom_prefixes.append('+254714')
    safaricom_prefixes.append('+254715')
    safaricom_prefixes.append('+254716')
    safaricom_prefixes.append('+254717')
    safaricom_prefixes.append('+254718')
    safaricom_prefixes.append('+254719')
    safaricom_prefixes.append('+254720')
    safaricom_prefixes.append('+254721')
    safaricom_prefixes.append('+254722')
    safaricom_prefixes.append('+254723')
    safaricom_prefixes.append('+254724')
    safaricom_prefixes.append('+254725')
    safaricom_prefixes.append('+254726')
    safaricom_prefixes.append('+254727')
    safaricom_prefixes.append('+254728')
    safaricom_prefixes.append('+254729')

    safaricom_prefixes.append('254701')
    safaricom_prefixes.append('254702')
    safaricom_prefixes.append('254703')
    safaricom_prefixes.append('254704')
    safaricom_prefixes.append('254705')
    safaricom_prefixes.append('254706')
    safaricom_prefixes.append('254707')
    safaricom_prefixes.append('254708')
    safaricom_prefixes.append('254709')
    safaricom_prefixes.append('254710')
    safaricom_prefixes.append('254711')
    safaricom_prefixes.append('254712')
    safaricom_prefixes.append('254713')
    safaricom_prefixes.append('254714')
    safaricom_prefixes.append('254715')
    safaricom_prefixes.append('254716')
    safaricom_prefixes.append('254717')
    safaricom_prefixes.append('254718')
    safaricom_prefixes.append('254719')
    safaricom_prefixes.append('254720')
    safaricom_prefixes.append('254721')
    safaricom_prefixes.append('254722')
    safaricom_prefixes.append('254723')
    safaricom_prefixes.append('254724')
    safaricom_prefixes.append('254725')
    safaricom_prefixes.append('254726')
    safaricom_prefixes.append('254727')
    safaricom_prefixes.append('254728')
    safaricom_prefixes.append('254729')

    supplied_number_prefix = str(number)[:4]

    if supplied_number_prefix in safaricom_prefixes:
        if len(number) == 10:
            is_safaricom_number = '1'
        else:
            is_safaricom_number = '0'
    else:
        is_safaricom_number = '0'

    return is_safaricom_number

# get twilio account details

def get_twilio_account_details():
    
    # Account SID from twilio.com/console
    account_sid = "AC6d64f4138d40052e23cd17f2a0bebeac"

    # Auth Token from twilio.com/console
    auth_token  = "609c69d53d3b536785c8e6f02115909b"

    # Twilio phone number
    twilio_number = '+14348851286'

    return account_sid, auth_token, twilio_number

# verify and format kenyan number

def verify_kenyan_phone_number(phone_number):

    if len(phone_number) == 10:
        if phone_number[:2] == '07':
            number_corrected = True
            number_to_use = '+254'+phone_number[1:]
        else:
            number_corrected = False
            number_to_use = 'Number is not a mobile number'
    elif len(phone_number) == 9:
        if phone_number[:1] == '7':
            number_corrected = True
            number_to_use = '+254'+phone_number
        else:
            number_corrected = False
            number_to_use = 'Number is not a mobile number'
    elif len(phone_number) == 12:
        if phone_number[:3] == '254':
            number_corrected = True
            number_to_use = '+'+phone_number
        else:
            number_corrected = False
            number_to_use = 'Number is not a mobile number'
    elif len(phone_number) == 13:
        if phone_number[:4] == '+254':
            number_corrected = True
            number_to_use = phone_number
        else:
            number_corrected = False
            number_to_use = 'Number is not a mobile number'
    elif len(phone_number) == 14:
        if phone_number[:5] == '00254':
            number_corrected = True
            number_to_use = '+'+phone_number[2:]
        else:
            number_corrected = False
            number_to_use = 'Number is not a mobile number'
    elif len(phone_number) == 15:
        if phone_number[:6] == '000254':
            number_corrected = True
            number_to_use = '+'+phone_number[3:]
        else:
            number_corrected = False
            number_to_use = 'Number is not a mobile number'
    else:
        number_corrected = False
        number_to_use = 'Number is not a mobile number'

    return number_corrected, number_to_use

# send sms twilio

def send_twilio_sms(tel_number, sms):

    # test phone number

    phone_number_correct, number_to_use = verify_kenyan_phone_number(tel_number)
    if phone_number_correct == True:
        account_sid, auth_token, twilio_number = get_twilio_account_details()

        client = Client(account_sid, auth_token)
        message = client.messages.create(to=number_to_use, from_=twilio_number, body=sms)

        sms_sent = True
        message_sid = message.sid
    else:
        sms_sent = False
        message_sid = 'None'

    return sms_sent, message_sid

# get duration

def get_duration_in_hours(starting_date, end_date):
    starting_date_formatted = datetime.strptime(str(starting_date)[:19], '%Y-%m-%d %H:%M:%S')
    end_date_formatted = datetime.strptime(str(end_date)[:19], '%Y-%m-%d %H:%M:%S')

    if end_date_formatted < starting_date_formatted:
        result_code = "0"
        duration_in_hours = 0
        message = "starting date must be greater than end date"
    else:
        dates_substraction = end_date_formatted - starting_date_formatted

        dates_substraction_string = str(dates_substraction)

        if "-" in dates_substraction_string:
            result_code = "0"
            duration_in_hours = 0
            message = "starting date must be greater than end date"
        else:
            if "days," in dates_substraction_string:
                the_number_of_days = float(dates_substraction_string.split("days")[0])
                the_hours_part = dates_substraction_string[-8:]
            else:
                if "day," in dates_substraction_string:
                    the_number_of_days = float(dates_substraction_string.split("day")[0])
                    the_hours_part = dates_substraction_string[-8:]
                else:
                    the_number_of_days = 0
                    if ':' in dates_substraction_string[:2]:
                        the_hours_part = '0' + dates_substraction_string
                    else:
                        the_hours_part = dates_substraction_string

            the_number_of_hours = float(the_hours_part[:2])
            the_number_of_minutes = float(the_hours_part[3:5])

            if the_number_of_minutes > 0:
                minute_converted_to_hour = 1
            else:
                minute_converted_to_hour = 0

            duration_in_hours = the_number_of_days * 24 + the_number_of_hours + minute_converted_to_hour
            result_code = "1"
            message = "Success"

    return result_code, str(duration_in_hours), message


def convert_hours_to_second(hour):
    return hour * 60


# hash password

def hash_password_function(raw_password):
    encoded_password = raw_password.encode('utf-8')
    h = hashlib.md5()
    h.update(encoded_password)
    hashed_password = h.hexdigest()

    return hashed_password
    

# function to return current datetime in safaricom mpesa timestamp

def get_safaricom_timestamp():
    current_datetime = datetime.now()
    datetime_without_dash = str(current_datetime).replace("-", "")
    datetime_without_space = datetime_without_dash.replace(" ", "")
    datetime_without_colon = datetime_without_space.replace(":", "")

    mpesa_date_stamp = datetime_without_colon[:14]

    return (mpesa_date_stamp)

# function to encode data in base64

def encode_in_base64(data_to_encode):
    bytes_encoded_data = base64.b64encode(data_to_encode.encode())

    from_b_data = str(bytes_encoded_data).split('b\'', 1)[1:]
    encoded_data = from_b_data[0].split('\'', 1)[:1]

    return (encoded_data[0])

# mpesa access token

def get_mpesa_access_token():

    today = datetime.now().date()

    current_datetime = datetime.now()

    get_current_mpesa_token = CompanyDetails.objects.all()
    for current_mpesa_token_data in get_current_mpesa_token:
        current_mpesa_access_token = current_mpesa_token_data.current_mpesa_access_token
        current_mpesa_access_token_generated_on_datetime = current_mpesa_token_data.current_mpesa_access_token_generated_on_datetime

    if current_mpesa_access_token == '' or current_mpesa_access_token == None:
        generate_another_mpesa_access_token = True
    else:
        period_of_last_generated_mpesa_access_token = current_datetime.replace(tzinfo=None)-current_mpesa_access_token_generated_on_datetime.replace(tzinfo=None)
        period_of_last_generated_mpesa_access_token_string = str(period_of_last_generated_mpesa_access_token)

        if 'days' in period_of_last_generated_mpesa_access_token_string or 'day' in period_of_last_generated_mpesa_access_token_string:
            generate_another_mpesa_access_token = True
        else:
            extracted_hour = period_of_last_generated_mpesa_access_token_string.split(':', 1)[:1]
            if int(extracted_hour[0]) > 0:
                generate_another_mpesa_access_token = True
            else:
                generate_another_mpesa_access_token = False


    if generate_another_mpesa_access_token == True:
        consumer_key = "duhDY8aQ1qFn0P3jrdkaSUGqMf5EK0zS"
        consumer_secret = "duiTT3Wp7k1OBKgS"
        api_URL = "https://api.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials"
        
        r = requests.get(api_URL, auth=HTTPBasicAuth(consumer_key, consumer_secret))

        # Test.objects.create(test=r)

        from_token_data = r.text.split('"access_token": "', 1)[1:]

        access_token_data = from_token_data[0].split('",', 1)[:1]

        access_token_data = access_token_data[0]

        CompanyDetails.objects.update(current_mpesa_access_token=access_token_data, current_mpesa_access_token_generated_on_datetime=today)
    else:
        access_token_data = current_mpesa_access_token

    return (access_token_data)

# perform user mpesa transfer

def perform_client_mpesa_transfer(mpesa_access_token, amount, user_mpesa_tel):

    paybill_number = "834700"
    access_token = mpesa_access_token
    lipa_na_mpesa_online_pass_key = "bfb279f9aa9bdbcf158e97dd71a467cd2e0c893059b10f78e6b72ada1ed2c919"    

    timestamp = get_safaricom_timestamp()

    string_to_encode = paybill_number+""+lipa_na_mpesa_online_pass_key+""+timestamp

    mpesa_password = encode_in_base64(string_to_encode)

    api_url="https://api.safaricom.co.ke/mpesa/stkpush/v1/processrequest"
    headers={"Authorization":"Bearer %s"%access_token}
    request={
        "BusinessShortCode": paybill_number,
        "Password": mpesa_password,
        "Timestamp": timestamp,
        "TransactionType": "CustomerPayBillOnline",
        "Amount": int(amount),
        "PartyA": user_mpesa_tel,
        "PartyB": paybill_number,
        "PhoneNumber": user_mpesa_tel,
        "CallBackURL": "https://technologiepenempesatest.herokuapp.com/rest_online_paybill_transaction_confirmation/",
        "AccountReference": 'NormalPayment',
        "TransactionDesc": 'Sacco payment'
    }

    response = requests.post(api_url,json=request,headers=headers)

    return (response.text)
    