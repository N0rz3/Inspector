from bs4 import BeautifulSoup
import requests


import utils


class Main:

    def __init__(self, phone):

        """
        Multi-step function :

        -> scrape the html code of the site
        -> look for the 1st <div> tag that has the class: "col-lg-9"
        -> retrieve the <h1> tag
        -> put in text and display in strip()
        """

        try:
            self.phone_numbers = phone
  
            response = requests.get(utils.tellows(phone=phone), headers=utils.headers)

            html = BeautifulSoup(response.text, "html.parser")
            html_cs = html.find("div", {"class": "col-lg-9"}).findAll("h1")


            try:
                infos = html_cs[0].text.strip()
                info = f"[{utils.Green}+{utils.White}] Phone number reputed for {utils.Green}->{utils.White} {infos}"

            except:
                info = f"[{utils.Red}-{utils.White}] Phone number not reputation"

            print(f"""
\n{utils.Green}> {utils.White}Reputation{utils.Green}
---------------------------------------------------{utils.White}

{info}
            """)

        except:
            return None