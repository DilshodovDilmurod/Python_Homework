1. Age Calculator: Ask the user to enter their birthdate. Calculate and print their age in years, months, and days.

from datetime import datetime, timedelta
birthdate = input('Tugilgan kuningizni kiriting(year/month/day):')
birthdate = datetime.strptime(birthdate,'%Y/%m/%d')

today = datetime.today()

# farqni hisoblash
years = today.year - birthdate.year
months = today.month - birthdate.month
days = today.day - birthdate.day

#tekshirish 
if days<0:
    months -=1
    last_month = (today.replace(day=1) - timedelta(days=1)).day
    days+=last_month
if months < 0:
    years -=1
    months +=12
print(f"siz {years} yil, {months} oy, {days} kun yashagansiz")
2 Days Until Next Birthday: Similar to the first exercise, but this time, calculate and print the number of days remaining until the user's next birthday.

from datetime import datetime, timedelta
birthdate = input('Tugilgan kuningizni kiriting(year/month/day):')
birthdate = datetime.strptime(birthdate,'%Y/%m/%d')

today = datetime.today()
# keyingi tugilgan kunini aniqlash
if today.month> birthdate.month:
    birthdate = birthdate.replace(year=today.year+1)
else: 
    birthdate = birthdate.replace(year=today.year)

# farqni hisoblash
years = birthdate.year - today.year
months = birthdate.month - today.month 
days = birthdate.day - today.day 

#tekshirish 
if days<0:
    months -=1
    last_month = (today.replace(day=1) - timedelta(days=1)).day
    days+=last_month
if months < 0:
    years -=1
    months +=12
print(f"sizning tugilgan kuningizga  {years} yil, {months} oy, {days} kun qolgan")
3 Meeting Scheduler: Ask the user to enter the current date and time, as well as the duration of a meeting in hours and minutes. Calculate and print the date and time when the meeting will end.
from datetime import datetime, timedelta
meeting_date = input('Uchrashuv sanasi toliq yozish va necha soat savom qiladi:(year/month/day/hour/minute')
meeting_duration = input('Uchrashuv davomiyligini kiriting:(hour/minute)')

meeting_date = datetime.strptime(meeting_date, '%Y/%m/%d/%H/%M')
hour, minute = map(int, meeting_duration.split('/'))

duration = timedelta(hours=hour, minutes=minute)

end_date = meeting_date + duration

print('Uchrashuv boshlash sanasi:', meeting_date)
print('uchrashuv tugash vaqti:', end_date)


4 Timezone Converter: Create a program that allows the user to enter a date and time along with their current timezone, and then convert and print the date and time in another timezone of their choice.
from datetime import datetime
import pytz

date_str = input('Sana va vaqtni kiriting:(masalan 2023-12-10 23:120) ')
from_zone = input('Hozirgi timezone (Asia/Tashkent)')
to_zone = input('Qaysi timezone ga otmoqchisiz (Europe/London)')

local_time = datetime.strptime(date_str, '%Y-%m-%d %H:%M')

local_tz = pytz.timezone(from_zone)
target_tz = pytz.timezone(to_zone)

localized_time = local_tz.localize(local_time)

convert_time = localized_time.astimezone(target_tz)

print(f'siz kiritgan ({from_zone}): {localized_time}')
print(f'siz tanlagan ({to_zone}) :{convert_time}')
5 Countdown Timer: Implement a countdown timer. Ask the user to input a future date and time, and then continuously print the time remaining until that point in regular intervals (e.g., every second).
from datetime import datetime
import time
date_str = input('Sana va vaqtni kiriting:(masalan 2023-12-10 23:120) ')
f_date  = datetime.strptime(date_str, '%Y-%m-%d %H:%M')
today= datetime.now()
while today < f_date:
    today= datetime.now()
    
    time_remaining = f_date - today
    print("Time remaining", time_remaining, end="\r")
    time.sleep(1)


6 Email Validator: Write a program that validates email addresses. Ask the user to input an email address, and check if it follows a valid email format.
import re
check_email = input("Email kiriting...")
pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
if re.match(pattern, check_email):
    print("True")
else:
    print("error")
7 Phone Number Formatter: Create a program that takes a phone number as input and formats it according to a standard format. For example, convert "1234567890" to "(123) 456-7890".
import re

phone = input( 'Telefon raqamini kiriting:')
digit_s = re.sub(r'\D', '', phone)
if len(digit_s) == 10:
    formatted = f'({digit_s[:3]}) {digit_s[3:6]}-{digit_s[6:10]}'
    print(f'formatlangan raqam: {formatted}')

8 Password Strength Checker: Implement a password strength checker. Ask the user to input a password and check if it meets certain criteria (e.g., minimum length, contains at least one uppercase letter, one lowercase letter, and one digit).
import re
password = input('Parollingizni kiriting:')
len_check = len(password)>=8
upper_case = re.search(r'[A-Z]', password)
lower_case = re.search(r'[a-z]', password)
digit_case = re.search(r'\d', password)
special_check = re.search(r'[@#$%!_%&*?]', password)
if all([len_check, upper_case, lower_case, digit_case, special_check]):
    print('Kuchli parol')
else:
    if not len_check:
        print('Kamida 8 belgi bolishi kerak')
    if not upper_case:
        print('kamida bitta katta harf kerak')
    if not lower_case:
        print('kamida bitta kichik harf bolishi kerak')
    if not digit_case:
        print('kamida bitta number kerak')
    if not special_check:
        print('kamida bitta bellilarda bolishi kerak')
9 Word Finder: Develop a program that finds all occurrences of a specific word in a given text. Ask the user to input a word, and then search for and print all occurrences of that word in a sample text.
text = 'bugungi kun  juda ajoyib kun bolayapti, kun davomida xush kayfiyat tilayman, ishlaringizga omad end yaxshi kunlardan bolsin'
word = input('soz kiriting:')
x = re.findall(word, text)
print(x)
