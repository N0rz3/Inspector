"""
Here you will find everything used to make the tool work properly like : 
- All colors
- Logo in ascii art
- Website used
- Headers
"""




# List all colors used
"""
Colors palette used -> https://www.webucator.com/article/python-color-constants-module/
Color rgb example (205,102,0) => Functional rgb color in python scripts example (\033[38;2;205;102;0m)
"""


Red = "\033[38;2;255;48;48m"
White = '\033[38;2;255;255;255m'
Green = "\033[38;2;193;255;193m"
Black = "\033[38;2;0;0;0m"
Yellow = "\033[38;2;255;255;0m"


# Banner
"""
Logo used in ascii art
"""
Banner = f"""
                       (@@@@@@@@@@@@@@@@@@@@@)
                   (@@@@@@@@@@@@@@@@@@@@@@@@@@@@@)                
               (@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@)
           (@@@@@@@@@@@@@@@@@@@@%%%%%@@@@@@@@@@@@@@@@@@@@)
        (@@@@@@@@@@@@@@@@@@@@@%%%%%%%%%@@@@@@@@@@@@@@@@@@@@@)
     (@@@@@@@@@@@@@@@@@@@@@@@%%%%/-\%%%%%@@@@@@@@@@@@@@@@@@@@@@)    By Norze (@N0rz3)
     (@@@@@@@@@@@@@@@@@@@@@@@%%%%\-/%%%%%@@@@@@@@@@@@@@@@@@@@@@)      Inspect{Red}0{White}r v1.1
        (@@@@@@@@@@@@@@@@@@@@@%%%%%%%%%@@@@@@@@@@@@@@@@@@@@@)
           (@@@@@@@@@@@@@@@@@@@@%%%%%@@@@@@@@@@@@@@@@@@@@)       
               (@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@)          
                   (@@@@@@@@@@@@@@@@@@@@@@@@@@@@@)
                       (@@@@@@@@@@@@@@@@@@@@@)
                       
                       
""".replace("(", Black + "(" + White).replace(")", Black + ")" + White).replace("@", White + "@").replace("%", Red + "%" + White).replace("/", Black + "/" + White).replace("\\", Black + "\\" + White).replace("-", Black + "-" + White)               


# website for the different variations of phone number
def free_lookup(phone) -> None:
    url = "https://free-lookup.net/{}".format(phone)

    return url

def tellows(phone) -> None:
    url = "https://www.tellows.fr/num/{}".format(phone)

    return url


# headers for requests
headers = {
    "User-Agent": "Mozilla/4.0 (compatible; MSIE 5.0; SunOS 5.9 sun4u; X11)"
}
