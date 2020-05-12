#from loading_data import df,dic,transactions
from generate_rules import get_rules_eff,compute_rules
from generate_item_sets import compute_item_set1
import argparse

parser = argparse.ArgumentParser()

parser.add_argument('--algorithm', type=int,default=0)#0 for efficient_apriori, 1 for our algorithm
parser.add_argument('--min_support', type=float,default=.1)
parser.add_argument('--min_confiedence',type=float,default=1)
args=parser.parse_args()

if(args.algorithm == 0):
	get_rules_eff(args.min_support,args.min_confiedence)
else:
	compute_rules(args.min_support,args.min_confiedence)

