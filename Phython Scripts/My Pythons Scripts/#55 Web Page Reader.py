import requests


url = "https://www.tgcom24.mediaset.it/cronaca/lotteria-italia-premi-biglietti-numeri-vincenti_75482858-202402k.shtml"

r = requests.get(url)
if r.status_code == 200:
    print(r.text)
else:
    print('Error')