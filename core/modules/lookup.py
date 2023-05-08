import re
import phonenumbers
from phonenumbers import carrier, timezone, geocoder

import utils

class Look:
    def __init__(self, phone):

            try:
                self.phone_number = phone

                # checking with phonenumbers
                numbers = phonenumbers.parse(phone)
                valid = phonenumbers.is_valid_number(numbers)
                timezones = timezone.time_zones_for_number(numbers)
                carriers = carrier.name_for_number(numbers, None)
                country = geocoder.description_for_number(numbers, 'fr')
                international = phonenumbers.format_number(numbers, phonenumbers.PhoneNumberFormat.INTERNATIONAL)
                national = phonenumbers.format_number(numbers, phonenumbers.PhoneNumberFormat.NATIONAL)
                prefix = phonenumbers.format_number(numbers, phonenumbers.PhoneNumberFormat.INTERNATIONAL).split(" ")[0]
                country_code = phonenumbers.region_code_for_country_code(int(prefix))

                # checing surcharged or not
                taxed = phone.replace("+33", "")
                if re.match(r"^8\d{8}$", taxed) or re.match(r"^0 8\d{8}$", taxed):
                    taxed = f"[{utils.Yellow}?{utils.White}] Phone number certainly surcharged"

                elif re.match(r"^9\d{8}$", taxed) or re.match(r"^0 9\d{8}$", taxed):
                    taxed = f"[{utils.Red}!{utils.White}] Phone number surcharged"     

                else:
                    taxed = f"[{utils.Green}*{utils.White}] Phone number not surcharged"


                # checking mobile or line
                mobile = phonenumbers.number_type(numbers)

                if mobile == phonenumbers.PhoneNumberType.MOBILE:
                    types = f"[{utils.Green}*{utils.White}] Type {utils.Green}->{utils.White} Mobile"

                else:
                    types = f"[{utils.Green}*{utils.White}] Type {utils.Green}->{utils.White} Line fixed "

                print(f"""
{utils.Green}> {utils.White}LookUp{utils.Green}
---------------------------------------------------{utils.White}

[{utils.Green}*{utils.White}] Valid {utils.Green}->{utils.White} {valid}
{types}
{taxed}

[{utils.Green}+{utils.White}] International phone number {utils.Green}->{utils.White} {international}
[{utils.Green}+{utils.White}] National phone number {utils.Green}->{utils.White} {national}   
[{utils.Green}+{utils.White}] Country prefix {utils.Green}->{utils.White} {prefix}
[{utils.Green}+{utils.White}] Country code {utils.Green}->{utils.White} {country_code}
[{utils.Green}+{utils.White}] Country {utils.Green}->{utils.White} {country}
[{utils.Green}+{utils.White}] TimeZone {utils.Green}->{utils.White} {timezones}
[{utils.Green}+{utils.White}] Carrier {utils.Green}->{utils.White} {carriers} 
                """)

            except:
                return None
