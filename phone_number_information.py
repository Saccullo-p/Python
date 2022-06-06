import phonenumbers
from phonenumbers import carrier, geocoder, timezone

mobileNum = input('Inserire un numero di telefono con il prefisso del paese: ')
mobileNum = phonenumbers.parse(mobileNum)

print(timezone.time_zones_for_number(mobileNum))

print(carrier.name_for_number(mobileNum, 'en'))

print(geocoder.description_for_number(mobileNum, 'en'))

print('Numero di telefono valido:', phonenumbers.is_valid_number(mobileNum))