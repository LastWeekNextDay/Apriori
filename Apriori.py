from mlxtend.frequent_patterns import apriori
from mlxtend.frequent_patterns import association_rules
import pandas as pd


class Apriori:
    def __init__(self):
        self.data = None
        self.frequent_itemsets = None
        self.association_rules = None

    def load(self, data):
        self.data = data

    def process(self, frq_min_support=0.6, mtr="confidence", rule_min_threshold=0.7):
        # Convert the transaction data to a one-hot encoded DataFrame
        oht = pd.DataFrame(pd.Series(self.data).str.join('|').str.get_dummies('|'))

        # Find frequent itemsets with a minimum support of 0.5 (adjust as needed)
        self.frequent_itemsets = apriori(oht, min_support=frq_min_support, use_colnames=True)

        # Find association rules
        self.association_rules = association_rules(self.frequent_itemsets, metric=mtr, min_threshold=rule_min_threshold)
