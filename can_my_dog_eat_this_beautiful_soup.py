import requests
from bs4 import BeautifulSoup
import pandas as pd
import re

page=requests.get("https://www.healthline.com/nutrition/human-foods-for-dogs")

soup=BeautifulSoup(page.content,"html.parser")
tag=soup.find_all(class_="css-0")
noumber=[2,3,5,6,8,10,12,13,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59]

food=[tag[i].a.get_text() for i in noumber]
desc=[tag[i].find(class_="content_body").get_text() for i in noumber]

df=pd.DataFrame({"RawFood":food,"RawDesc":desc})
df["Food"]=df["RawFood"].apply(lambda x:x.split(". ")[1].split(": ")[0])
df["RawCat"]=df["RawFood"].apply(lambda x:x.split(". ")[1].split(": ")[-1])
df["Description"]= [re.sub(r"\s\(.+\)","",str(x)) for x in df['RawDesc']]
df["Category"]=df["RawCat"].apply(lambda x:"Yes" if x=="Can Eat" else ("Yes, but" if x=="Limit" else "No"))
df.drop(["RawFood","RawDesc","RawCat"],axis=1,inplace=True)