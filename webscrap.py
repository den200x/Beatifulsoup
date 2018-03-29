import requests
from bs4 import BeautifulSoup

r = requests.get("https://www.pythonhow.com/real-estate/rock-springs-wy/LCWYROCKSPRINGS/")
c = r.content

soup = BeautifulSoup(c,"html.parser")

all = soup.find_all("div",{"class":"propertyRow"})

v = all[0].find("h4",{"class":"propPrice"}).text#.replace("\n","").replace(" ","")

for item in all:
    d={}
    d["Address"]=item.find_all("span",{"class","propAddressCollapse"})[0].text
    d["Locality"]=item.find_all("span",{"class","propAddressCollapse"})[1].text
    d["Price"]=item.find("h4",{"class":"propPrice"}).text.replace("\n","").replace(" ","")
    #print('\n\n#######' + item.find("h4",{"class":"propPrice"}).text.replace("\n","").replace(" ",""))
    #print(item.find_all("span",{"class","propAddressCollapse"})[0].text)
    #print(item.find_all("span",{"class","propAddressCollapse"})[1].text + "\n")
    try:
        print(item.find("span",{"class","infoBed"}).text) #alternatively add .find("b")
    except:
        pass
        #print(None)
    try:
        print(item.find("span",{"class","infoSqFt"}).text)
    except:
        pass
        #print(None)
    try:
        print(item.find("span",{"class","infoValueFullBath"}).text)
    except:
        pass
        print('\n')
    for col_group in item.find_all("div",{"class":"columnGroup"}):
        #print(col_group)
        for feat_group, feat_name in zip(col_group.find_all("span",{"class":"featureGroup"}),col_group.find_all("span",{"class":"featureName"})):
            #print(feat_group.text, feat_name.text)
            if"Lot Size" in feat_group.text:
                print(feat_name.text)
#print(v)