import phonenumbers
mobileno=input("Enter ur number with country code")
mobileno=phonenumbers.parse(mobileno)
print(timezone.time_zones_for_number(mobileno))
print(carrier.name_for_number(mobileno,"en"))
print(geocoder.description_for_number(mobileno,"en"))                              
