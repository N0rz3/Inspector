import argparse, os # modules
from tqdm import tqdm

import utils # my module

from modules import lookup, free_scraping, reputation # my module
from lib import amazon, instagram



class Inspect:

    def main():
        
        os.system("cls && title Inspect0r v1" if os.name == "nt" else 'clear')
        print(utils.Banner)

        # command for launch the tool
        parser = argparse.ArgumentParser() 
        parser.add_argument('phonenumber', help='<phone>')

        args = parser.parse_args()
        numbers = args.phonenumber

        phone_format = numbers.replace("+33", "") # Change the `+33` by the country code that need 
        free_format = numbers.replace("+", "").strip()
        for i in tqdm(range(int(9e6))):
            pass

        lookup.Look(phone=numbers)

        print(f"\n{utils.Green}> {utils.White}Ignorant Modules\n{utils.Green}---------------------------------------------------{utils.White}\n")
        amazon.main(phone=phone_format)
        instagram.main(phone=phone_format)
        print(f"\n[{utils.Red}-{utils.White}] = No account, [{utils.Green}+{utils.White}] = Linked account, [{utils.Black}x{utils.White}] = Ratelimit")

        print(f"\n\n{utils.Green}> {utils.White}Free-lookup.net\n{utils.Green}---------------------------------------------------{utils.White}\n")
        free_scraping.Main(phone=free_format)
        reputation.Main(phone=phone_format)


# Launch the tool
if __name__ == "__main__":
    Inspect.main()
