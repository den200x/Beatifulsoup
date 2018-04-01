import requests
from bs4 import BeautifulSoup
import pandas
import re
from IPython.display import HTML

r = requests.get("http://www.dm5.com/manhua-new/")
c = r.content

soup = BeautifulSoup(c,"html.parser")

Upd = soup.find_all("div",{"class":"mh-item-detali"}) #type(Upd) == <class 'bs4.element.ResultSet'>

updated = []

for items in Upd:
    d={}
    #updated.append(items)
    
    d["title_name"] = items.find("h2",{"class":"title"}).text
    d["chap_name"] = items.find("p",{"class","chapter"}).text
    d["t_update"] = items.find("p",{"class":"zl"}).text.replace(" ","")
    #d["link"] = '<a href="'+"http://www.dm5.com" + re.findall(r'"(.*?)"',str(items.find("a",href=True,text=True)))[0]+'">link</a>'
    d["link"] = "http://www.dm5.com" + re.findall(r'"(.*?)"',str(items.find("a",href=True,text=True)))[0]
    #updated.append(zip(title_name,chap_name,t_update))
    updated.append(d)


df = pandas.DataFrame(updated)
df = df[["title_name","chap_name","t_update","link"]]

#df.columns = df[3].apply(lambda:x '<a href="{}">{}</a>'.format(x))

#df.style.format(make_clickable)
#for link in df["link"]:
#    link = '<a href="{0}">link</a>'.format(link)
#df.to_html("updatedManga.html")
print(df)
HTML(df.to_html("updated2Manga.html"))

#df = pandas.DataFrame(li)
#df.to_csv("ScrapedData.csv")
#print(all)
#print(type(Upd))
#print(type(updated))
#print(updated)

#print(updated)
#print(chap_name)
#print(t_update)