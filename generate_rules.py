from efficient_apriori import apriori
import enum
from loading_data import df,dic,transactions,discription
from generate_item_sets import compute_item_set1,trans_count
import time
sub_sets=[]
rules=[]

def get_rules_eff(min_sup,min_confid):
  t1=time.time()
  itemset,rules=apriori(transactions, min_support=min_sup, min_confidence=min_confid)
  t2=time.time()
  print("Time Cost = ",'%.3f'%(t2-t1),"seconds")
  print("number of rules = ",len(rules),"\n\n")
  
  for r in rules:
    print("(",end="")    
    for c,l in enumerate(r.lhs):
      classs=dic[l]
      sub_class=classs[1]
      if df.columns[classs[0]] in discription:
      	sub_class=discription[df.columns[classs[0]]][sub_class]

      print(df.columns[classs[0]],"=",sub_class,end="")
      if(c == len(r.lhs)-1):
        break
      print(" , ",end="")
    print(")"," -> ","(",end=" ")

    for c,l in enumerate(r.rhs):
      classs=dic[l]
      sub_class=classs[1]
      if df.columns[classs[0]] in discription:
        sub_class=discription[df.columns[classs[0]]][sub_class]

      print(df.columns[classs[0]],"=",sub_class,end="")
      if(c == len(r.rhs)-1):
        break
      print(" , ",end="")
    
    print(") Confidence=",'%.3f'%r.confidence,"  Lift=",'%.3f'%r.lift,"\n\n")
    

class rule():
  def __init__(self,lhs,rhs,confid,sup_lhs,sup_rhs,sup_lhsandrhs):
    self.lhs=lhs
    self.rhs=rhs
    self.confid=confid
    self.sup_lhs=sup_lhs
    self.sup_rhs=sup_rhs
    self.sup_lhsandrhs=sup_lhsandrhs
  
  def visualize(self): 
    print("(",end="")       
    for c,l in enumerate(self.lhs):
      classs=dic[l][0]
      sub_class=dic[l][1]
      if(df.columns[classs] in discription):
        sub_class=discription[df.columns[classs]][sub_class]
      print(df.columns[classs],"=",sub_class,end="")
      if(c == len(self.lhs)-1):
          break
      print(" & ",end="")
  
    print(")"," -> ","(",end=" ")
    
    for c,l in enumerate(self.rhs):
      classs=dic[l][0]
      sub_class=dic[l][1]
      if(df.columns[classs] in discription):
        sub_class=discription[df.columns[classs]][sub_class]
      print(df.columns[classs],"=",sub_class,end="")
      if(c == len(self.rhs)-1):
        break
      print(" & ",end="")
    print(") [ Confidence=",'%.3f'%self.confid," , Lift=",'%.3f'%(self.sup_lhsandrhs/(self.sup_lhs*self.sup_rhs))," , Leverage=",'%.3f'%(self.sup_lhsandrhs-(self.sup_lhs*self.sup_rhs)),"] \n\n")


def support2(trans1):
  return len(trans_count[len(trans1)-1][trans1])/len(transactions)

def find_all_subsets(rule,ans,ind):
  if(ind == len(rule)):
    if(len(ans) != 1) and (len(ans) != len(rule)+1) :
      sub_sets.append(ans[1:])
    return 
  ans1=ans.copy()
  ans1.append(rule[ind])

  find_all_subsets(rule,ans1,ind+1)
  find_all_subsets(rule,ans,ind+1)
  
def get_rules(item_set,min_conf):
  for sub_set in sub_sets:
    lhs=sub_set
    rhs=list(set(item_set)-set(sub_set))    
    r=lhs+rhs
    r.sort()
    sup_lhs=support2(tuple(lhs))
    sup_rule=support2(tuple(r))
    if(sup_rule/sup_lhs >= min_conf):
      sup_rhs=support2(tuple(rhs))
      r=rule(lhs,rhs,sup_rule/sup_lhs,sup_lhs,sup_rhs,sup_rule)
      rules.append(r)

def compute_rules(min_sup,min_conf):
  t1=time.time()
  it =compute_item_set1(min_sup)
  global rules
  rules=[]
  for i  in range(1,len(it)):
      for j in range(len(it[i])):
        global sub_sets
        sub_sets=[]      
        find_all_subsets(it[i][j].copy(),[0],0)
        get_rules(it[i][j],min_conf)
  t2=time.time()
  print("Time Cost =",'%.2f'%(t2-t1),"seconds")
  print("num_of_rules",len(rules))
  for r in rules:
  	r.visualize()
  

