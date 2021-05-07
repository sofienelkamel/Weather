import os, sys
os.system("clear")

# if you don't install requests and bs4 the Tool will not work

try:
    import requests
    from bs4 import BeautifulSoup
except ImportError:
    print(" please install requests and bs4")
    # pip install requests
    # pip install bs4
    sys.exit(1)
city = input(" Enter your city: ")
search = f"Weather in {city}"
url = f"https://www.google.com/search?&q={search}"
req = requests.get(url)
sor = BeautifulSoup(req.text, "html.parser")
con = sor.find("div", class_='BNeawe').text
print(' ',con)