from efficient_apriori import apriori
import pandas as pd

def test_apriori(min_sup=0.1, min_conf=1):

    df = pd.read_csv("dataset.csv")
    
    transactions = [tuple(row) for row in df.values.tolist()]

    itemsets, rules = apriori(transactions, min_support=min_sup, min_confidence=min_conf)

    print(rules)

    #TODO: ADD our algorithim and compare results

if __name__ == "__main__":
    test_apriori()