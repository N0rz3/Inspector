import trio
import httpx

"""
Ignorant -> https://github.com/megadose/ignorant
Github Owner Ignorant -> https://github.com/megadose/

License Ignorant -> https://www.gnu.org/licenses/gpl-3.0.fr.html
"""

from ignorant.modules.shopping.amazon import amazon


import utils


def main(phone):
    
    try:
        list = []

        async def Amazon():
            country_code="33" # To change according to the country of the number
            client = httpx.AsyncClient()
            out = []

            await amazon(phone, country_code, client, out)

            list.append(out)
            await client.aclose()


        trio.run(Amazon)

        acces_list = []

        for i in list:
            try:

                if i[0]['rateLimit'] == True:
                    acces_list.clear()

                    print(f"[{utils.Black}x{utils.White}] Amazon")

                if i[0]['rateLimit'] == False:

                    if i[0]['exists'] == True:
                        acces_list.append(i[0]['name'])

                        print(f"[{utils.Green}+{utils.White}] Amazon")

                    if i[0]['exists'] == False:
                        acces_list.clear()

                        print(f"[{utils.Red}-{utils.White}] Amazon")
            except:
                pass

    except:
        return None
