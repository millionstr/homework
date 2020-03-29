import json
"""class Taksi:
    def __init__(name, estimate):
        self.name = name
        self.estimate = estimate
"""

if __name__ == "__main__":
    #-----------------          основна прога          -------------------
    with open("prices.json", "r") as file:
        katalog = file.read()    
    baza = json.loads(katalog)
    print(baza['prices'])