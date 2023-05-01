from bs4 import BeautifulSoup
import requests

import utils

class Main:

    def __init__(self, phone):

        """
        Multi-step function :

        -> Retrieve the html code of the page
        -> Take the <ul> tag which has the class: "list-inline" and take the <li> tags
        -> Filter <span> tags that are in <li> and removed
        """

        try:
            self.phone_number = phone

            response = requests.get(utils.free_lookup(phone), headers=utils.headers)
            html = response.text

            html_body = BeautifulSoup(html, "html.parser")
            li_list = html_body.find("ul", class_="list-inline").find_all("li")


            possible_formats = [] # list

            for li in li_list:

                for span in li.find_all("span"):
                    span.clear() # clear all <span> in balises <li>

                formats = li.text.strip()
                possible_formats.append(formats) # added all formats

            print(f"{utils.Green}[{utils.Yellow}~{utils.Green}] {utils.White}Possible phone number formats :\n")
            for formats in possible_formats:
                print(f"[{utils.Green}+{utils.White}] " + formats)

        except:
            return None