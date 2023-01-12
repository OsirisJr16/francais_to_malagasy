import requests  
import unicodedata 
from bs4 import BeautifulSoup  

def get_traduction_to_malagasy(mot) :
    trads=[]
    url="https://fr.mondemalgache.org/bins/teny2/" + mot.lower()

    soup  = BeautifulSoup(requests.get(url = url).text , 'html.parser') 


    for trad in soup.find_all('a') :
        if "/bins/teny2/" in str(trad.get('href')) :
            trads.append(unicodedata.normalize("NFKD", trad.text))
    traductions = []
    for i in trads : 
        if i.isalpha() : 
            traductions.append(i)
    if traductions:
        return ' '.join(traductions )
    else:
        return 'Aucun mots semblabes à'+' '+mot 

