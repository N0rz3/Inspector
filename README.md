# **Inspector 👁️ - OSINT tool**
![inspector](https://user-images.githubusercontent.com/123885505/235235978-76f43388-fba9-4443-bb30-1649aaa3ed95.png)
![Python minimum version](https://img.shields.io/badge/Python-3.10%2B-brightgreen)

# Find information via a 📞 __French__ phone number  !

## **⚙️ Requirements / Launch**

- [Python 3](https://www.python.org/downloads/)
```sh
>> git clone https://github.com/N0rz3/Inspector.git
>> cd Inspector
>> pip install -r requirements.txt

>> cd core\
>> python inspector.py -h
```

- Details : 
```

                       (@@@@@@@@@@@@@@@@@@@@@)
                   (@@@@@@@@@@@@@@@@@@@@@@@@@@@@@)
               (@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@)
           (@@@@@@@@@@@@@@@@@@@@%%%%%@@@@@@@@@@@@@@@@@@@@)        
        (@@@@@@@@@@@@@@@@@@@@@%%%%%%%%%@@@@@@@@@@@@@@@@@@@@@)     
     (@@@@@@@@@@@@@@@@@@@@@@@%%%%/-\%%%%%@@@@@@@@@@@@@@@@@@@@@@)    By Norze (@N0rz3)
     (@@@@@@@@@@@@@@@@@@@@@@@%%%%\-/%%%%%@@@@@@@@@@@@@@@@@@@@@@)      Inspect0r v1.1 
        (@@@@@@@@@@@@@@@@@@@@@%%%%%%%%%@@@@@@@@@@@@@@@@@@@@@)
           (@@@@@@@@@@@@@@@@@@@@%%%%%@@@@@@@@@@@@@@@@@@@@)       
               (@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@)           
                   (@@@@@@@@@@@@@@@@@@@@@@@@@@@@@)
                       (@@@@@@@@@@@@@@@@@@@@@)


usage: inspector.py [-h] <phonenumber>


positional arguments:
  phonenumber  <phone>

options:
  -h, --help   show this help message and exit
```

### **📚 Example input :**
```
python inspector.py +33666666666
```

### **📚 Example output :**
```


                       (@@@@@@@@@@@@@@@@@@@@@)
                   (@@@@@@@@@@@@@@@@@@@@@@@@@@@@@)
               (@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@)
           (@@@@@@@@@@@@@@@@@@@@%%%%%@@@@@@@@@@@@@@@@@@@@)
        (@@@@@@@@@@@@@@@@@@@@@%%%%%%%%%@@@@@@@@@@@@@@@@@@@@@)
     (@@@@@@@@@@@@@@@@@@@@@@@%%%%/-\%%%%%@@@@@@@@@@@@@@@@@@@@@@)    By Norze (@N0rz3)
     (@@@@@@@@@@@@@@@@@@@@@@@%%%%\-/%%%%%@@@@@@@@@@@@@@@@@@@@@@)      Inspect0r v1.1
        (@@@@@@@@@@@@@@@@@@@@@%%%%%%%%%@@@@@@@@@@@@@@@@@@@@@)
           (@@@@@@@@@@@@@@@@@@@@%%%%%@@@@@@@@@@@@@@@@@@@@)
               (@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@)
                   (@@@@@@@@@@@@@@@@@@@@@@@@@@@@@)
                       (@@@@@@@@@@@@@@@@@@@@@)



> LookUp
---------------------------------------------------

[*] Valid -> True
[*] Type -> Mobile
[*] Phone number not surcharged

[+] International phone number -> +33 6 66 66 66 66
[+] National phone number -> 06 66 66 66 66        
[+] Country prefix -> +33
[+] Country code -> FR
[+] Country -> France
[+] TimeZone -> ('Europe/Paris',)
[+] Carrier -> Bouygues


> Ignorant Modules
---------------------------------------------------

[-] Amazon
[x] Instagram

[-] = No account, [+] = Linked account, [x] = Ratelimit


> Free-lookup.net
---------------------------------------------------    

[~] Possible phone number formats :

[+] 06 66 66 66 66
[+] +33 6 66 66 66 66
[+] +33666666666
[+] 0666666666
[+] tel:+33-6-66-66-66-66


> Reputation
---------------------------------------------------

[+] Phone number reputed for -> carrefour express 0666666666 / +33666666666
```


## **🧾 Summary**

Mains features :
 - Valid or no
 - Mobile or line
 - Phone number surchaged
 - Differents formats
 - Country information
 - Carrier
 - Related accounts
 - Reputation 


## **🗂️ Ignorant  Modules**

|   Name   |  Domain | Method | 
|---    |:-: | :-:
|    amazon  |   amazon.com   | login|
|   instagram|   instagram.com           | register|





## ✔️/❌ Rules
### __Disclaimer__

This tool was built solely for educational purposes, and I am not responsible for its use.

Using this tool in a paid service is strictly prohibited. Please use it only for personal investigation purposes or open-source projects.

**⚠️ DO NOT USE FOR MALICIOUS PURPOSES ⚠️**


## **📝 License**

[GNU General Public License v3](https://www.gnu.org/licenses/gpl-3.0.fr.html)

Do you like what I offer as content ? Subscribe to my GitHub account for more tools and programs ! 😉

## **💳 Credits**

- 👨‍💻 Source code : me 🤗
- 🖼️ Logo        : me 🤗
- 🖼️ Logo in ascii : Z0r4x

if you want to find information on a number other than French please change ` country_code="33"` instead of 33 change with the beginning of the number for example: `+20...` well you put `20` instead of 33 in the lib folder in `amazon.py` and `instagram.py`

and also change the `country = geocoder.description_for_number(numbers, 'fr')` in the module folder and `lookup.py` by `country = geocoder.description_for_number(numbers, 'country code of the phone number')`
