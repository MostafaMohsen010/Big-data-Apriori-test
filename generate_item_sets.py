from loading_data import df,dic,transactions
from bisect import bisect_left 
import time

trans_count=[]    
def BinarySearch(a, x): 
  i = bisect_left(a, x) 
  if i != len(a) and a[i] == x: 
    return i 
  else:
    return -1
def support1(trans1,trans2):
  out=[]
  for t1 in trans1:
    if( BinarySearch(trans2,t1) != -1 ):
      out.append(t1)
  return out

def compute_item_set1(min_sup):
  item_set=[]
  item_set1=[]
  unique=[]
  dic={}
  for i in range(12):
    for element in df[df.columns[i]].unique():     
      element_trans=[]
      for k in range(len(transactions)):
        
        if(transactions[k][i] == element):
          element_trans.append(k)
      
      sup=len(element_trans)/len(transactions)
      if sup >= min_sup:
        item_set1.append([element])
        dic[(element,)]=element_trans
  trans_count.append(dic)
  item_set.append(item_set1)
  i=-1
  while(len(item_set1) != 0):
    dic={}
    i+=1
    item_set1=[]     
    for ind1,item1 in enumerate(item_set[i]):
      for ind2 in range(ind1+1,len(item_set[i])):
        rule1=item1.copy()
        rule2=item_set[i][ind2].copy()
        if(rule1[0:-1] != rule2[0:-1]):
          break

        num_of_tr=support1(trans_count[i][tuple(rule1)],trans_count[0][(rule2[-1],)])    
        
        if(len(num_of_tr)/len(transactions) >= min_sup):
          rule1.append(rule2[-1])
          dic[tuple(rule1)]=num_of_tr
          item_set1.append(rule1)
    
    trans_count.append(dic)
    item_set.append(item_set1)
  return item_set
