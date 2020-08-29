import requests
from bs4 import BeautifulSoup
import sys, argparse
import bcolors

def banner():
  print("""

                ░██████╗░█████╗░██████╗░██╗██████╗░████████╗░░░░░░░█████╗░██████╗░░█████╗░░██╗░░░░░░░██╗██╗░░░░░███████╗██████╗░
                ██╔════╝██╔══██╗██╔══██╗██║██╔══██╗╚══██╔══╝░░░░░░██╔══██╗██╔══██╗██╔══██╗░██║░░██╗░░██║██║░░░░░██╔════╝██╔══██╗
                ╚█████╗░██║░░╚═╝██████╔╝██║██████╔╝░░░██║░░░█████╗██║░░╚═╝██████╔╝███████║░╚██╗████╗██╔╝██║░░░░░█████╗░░██████╔╝
                ░╚═══██╗██║░░██╗██╔══██╗██║██╔═══╝░░░░██║░░░╚════╝██║░░██╗██╔══██╗██╔══██║░░████╔═████║░██║░░░░░██╔══╝░░██╔══██╗
                ██████╔╝╚█████╔╝██║░░██║██║██║░░░░░░░░██║░░░░░░░░░╚█████╔╝██║░░██║██║░░██║░░╚██╔╝░╚██╔╝░███████╗███████╗██║░░██║
                ╚═════╝░░╚════╝░╚═╝░░╚═╝╚═╝╚═╝░░░░░░░░╚═╝░░░░░░░░░░╚════╝░╚═╝░░╚═╝╚═╝░░╚═╝░░░╚═╝░░░╚═╝░░╚══════╝╚══════╝╚═╝░░╚═╝
                                                                                                                    Code By: NG
            """
        )

#u = "https://medium.com/@gupta.bless"


if(len(sys.argv) > 1):
  banner()
  if(sys.argv[1] != 'u'):
    try:
      input_url = sys.argv[2]
      finput_url = 'https://www.' + input_url
      parser = argparse.ArgumentParser()
      parser.add_argument("-u", required=True)
      args = parser.parse_args()

      print(bcolors.BITALIC + "Checking for Java script Link")
      input_request = requests.get(finput_url)
      print(input_request)
      input_soup = BeautifulSoup(input_request.text, 'html.parser')
      for input_search in input_soup.find_all('script'):
        input_text = input_search.get('src', input_search.get('src'))
        if (input_text != None):
           if 'js' in input_text:
            try:
             if 'http' in input_text:
                input_statuscode = requests.get(input_text).status_code
                print(bcolors.OKMSG + input_text, input_statuscode)
             elif '.com' in input_text:
                 input_replaced =  input_text.replace('//' ,' ')
                 input_striped = "https://" + input_replaced.strip()
                 input_statuscode = requests.get(input_striped).status_code
                 print(bcolors.OKMSG + input_striped , input_statuscode)
             else:
               full_input_url = finput_url +  input_text
               input_statuscode = requests.get(full_input_url).status_code
               print(bcolors.OKMSG + full_input_url , input_statuscode)
            except:
                print(bcolors.ERRMSG + 'Status code for that url not possible')
    except:
      print(bcolors.OKMSG + 'Please enter python js.py -u <valid URL without https://  or https://> ')
  elif (sys.argv[1] == '-h'):
    print(bcolors.BOLD + 'usage: js.py [-h] -u URL' '\n' 'OPTIONS:' '\n' '-h,--help    '
                         'show this help message and exit' '\n''-u URL,   --url URL for which URL you want to check js')
  elif (sys.argv[1] != '-u'):
      print(bcolors.OKMSG + 'Please enter -u < valid URL without http:// or https:// >')
else:
    banner()
    print(bcolors.ERR + 'Please select at-least 1 option from -u or -h, with a valid URL')

