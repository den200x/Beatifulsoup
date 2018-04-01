import requests
import re
from bs4 import BeautifulSoup
import pandas

rr = requests.get("https://www.pythonhow.com/real-estate/rock-springs-wy/LCWYROCKSPRINGS/")
cc = rr.content

soupp = BeautifulSoup(cc,"html.parser")

all = soupp.find_all("div",{"class":"propertyRow"})

#v = all[0].find("h4",{"class":"propPrice"}).text.replace("\n","").replace(" ","")
#url = """http://www.pythonhow.com/real-estate/rock-springs-wy/LCWYROCKSPRINGS/t=0&s=\"""" 

page_num=soupp.find_all("a",{"class":"Page"})[-1].text
x = int(page_num)
#print(x)
li =[]
for page in range(0,x*10,10):
    
        
    r=requests.get("http://www.pythonhow.com/real-estate/rock-springs-wy/LCWYROCKSPRINGS/t=0&s="+str(page)+".html")
    c=r.content
    soup=BeautifulSoup(c,"html.parser")
    all=soup.find_all("div",{"class":"propertyRow"})
    for item in all:
        d={}
        d["Address"]=item.find_all("span",{"class","propAddressCollapse"})[0].text
        d["Locality"]=item.find_all("span",{"class","propAddressCollapse"})[1].text
        d["Price"]=item.find("h4",{"class":"propPrice"}).text.replace("\n","").replace(" ","")
        #print('\n\n#######' + item.find("h4",{"class":"propPrice"}).text.replace("\n","").replace(" ",""))
        #print(item.find_all("span",{"class","propAddressCollapse"})[0].text)
        #print(item.find_all("span",{"class","propAddressCollapse"})[1].text + "\n")
        try:
            d["Beds"]=item.find("span",{"class","infoBed"}).find("b").text #alternatively add .find("b")
        except:
            d["Beds"]=None
        try:
            d["Area"]=item.find("span",{"class","infoSqFt"}).find("b").text
        except:
            d["Area"]=None
        try:
            d["FullBath"]=item.find("span",{"class","infoValueFullBath"}).find("b").text
        except:
            d["FullBath"]=None
        for col_group in item.find_all("div",{"class":"columnGroup"}):
            #print(col_group)
            for feat_group, feat_name in zip(col_group.find_all("span",{"class":"featureGroup"}),col_group.find_all("span",{"class":"featureName"})):
                #print(feat_group.text, feat_name.text)
                if"Lot Size" in feat_group.text:
                    d["Lot Size"]=feat_name.text
        li.append(d)
    
        
    ##if int(page_nr) >=1:

        #page_nr = int(page_nr) -1 

df = pandas.DataFrame(li)
df.to_csv("ScrapedData.csv")
print(df)