import re

regex_mail = re.compile(r'[A-Za-z0-9]+@[A-Za-z]+[.]{1}[a-z]+')
regex_phone = re.compile(r'([0-9]{2} ){4}[0-9]{2}')
regex_postcode = re.compile(r'[0-9]{5}')
#regex_date = re.compile()

def valid_mail(mail:str) -> bool:
    return re.fullmatch(regex_mail, mail)

def valid_phone(phone:str) -> bool:
    return re.fullmatch(regex_phone, phone)

def valid_postcode(postcode:str) -> bool:
    return re.fullmatch(regex_postcode, postcode)

print(valid_phone('07 20 20 20 20'))
print(valid_mail('asdDGGqsdfq@qfdgqdfg.ccc'))
