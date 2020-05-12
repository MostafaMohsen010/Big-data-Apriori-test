
import pandas as pd
from efficient_apriori import apriori
import enum
from itertools import combinations

data_set_path="/Users/mak/Desktop/My_GitHup/Big-data-Apriori-test/dataset.csv"
df = pd.read_csv(data_set_path,header=None)

df_numpy=df.to_numpy()
unique=[]
offset=[]
dic={}
offset.append(0)
classes_num=0
for i in range(12):
	unique.append(max(df[i].unique())+1)
	classes_num+=unique[-1]

for v in unique:
	offset.append(v+offset[-1])

counter=0

for c,u in enumerate(unique):	
	for i in range(u):
		dic[counter]=(c,i)
		counter+=1
    
for i in range(df.shape[1]):
		
	for j in range(df.shape[0]):
		df_numpy[j,i]+=offset[i]
df.columns = ["Number of car policies","Number of fire policies","Customer_Status","Number of houses","Avrage size household","Avrage age","Customer main type","Roman catholic","Protestant","Other religion","No religion","Married"]
transactions = [tuple(row) for row in df.values.tolist()]
discription={"Customer_Status":[
  "High Income,expensive child",
	"Very Important Provincials",
  "High status seniors",
	"Affluent senior apartments",
  "Mixed seniors",
  "Career and childcare",
  "Dinki's (double income no kids)",
  "Middle class families",
  "Modern, complete families",
  "Stable family",
  "Family starters",
  "Affluent young families",
  "Young all american family",
  "Junior cosmopolitan",
  "Senior cosmopolitans",
  "Students in apartments",
  "Fresh masters in the city",
  "Single youth",
  "Suburban youth",
  "Etnically diverse",
  "Young urban have-nots",
  "Mixed apartment dwellers",
  "Young and rising",
  "Young, low educated" ,
  "Young seniors in the city",
  "Own home elderly",
  "Seniors in apartments",
  "Residential elderly",
  "Porchless seniors: no front yard",
  "Religious elderly singles",
  "Low income catholics",
  "Mixed seniors",
  "Lower class large families",
  "Large family, employed child",
  "Village families",
  "Couples with teens 'Married with children'",
  "Mixed small town dwellers",
  "Traditional families",
	"Large religous families",
  "	Large family farms",
  "Mixed rurals",
],
"Avg age":[
  "(20-30 years)",
  "(30-40 years)",
  "(40-50 years)",
  "(50-60 years)",
  "(60-70 years)",
  "(70-80 years)",
  ],
  "Customer main type":[

  "Successful hedonists",

  "Driven Growers",

  "Average Family",

  "Career Loners",

  "Living well",

  "Cruising Seniors",

  "Retired and Religeous",

  "Family with grown ups",

  "Conservative families",

 "Farmers",
  ],
  "Roman catholic":[
   "0%",
  "1 - 10%",
  "11 - 23%",
  "24 - 36%",
  "37 - 49%",
  "50 - 62%",
  "63 - 75%",
  "76 - 88%",
  "89 - 99%",
  "100%",   
  ]

}

	