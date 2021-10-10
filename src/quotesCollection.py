import json
import random


class QuotesCollection:
    location = "quotes.json"

    def __init__(self):
        self.jsonData = json.load(open(self.location, "r"))

    def getQuote(self):  # Gives random quotes
        quotes_ = self.jsonData['quotes']
        quoteNo = random.randint(0, (len(quotes_) - 1))
        return quotes_[quoteNo]['quote']
