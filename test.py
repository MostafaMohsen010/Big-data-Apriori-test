from efficient_apriori import apriori


def test_apriori():

    transactions = [('eggs', 'bacon', 'soup'),
                    ('eggs', 'bacon', 'apple'),
                    ('soup', 'bacon', 'banana')]

    itemsets, rules = apriori(transactions, min_support=0.1, min_confidence=1)

    #TODO: ADD our algorithim and compare results