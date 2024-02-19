import phonenumbers
from phonenumbers import timezone,geocoder,carrier
from phonenumbers import phonemetadata,shortnumberinfo,util
number = input("ENTER YOUR NUMBER WITH +__:")
phone = phonenumbers.parse(number)
time = timezone.time_zones_for_number(phone)
car = carrier.name_for_number(phone,"en")
reg = geocoder.description_for_number(phone,"en")
a = phonemetadata.PhoneNumberDesc(phone,"en")
b = shortnumberinfo.expected_cost_for_region(phone,"en")
c = shortnumberinfo.is_sms_service_for_region(phone,"en")
d = util.mutating_method(phone)
print(time)
print(phone)
print(car)
print(reg)
