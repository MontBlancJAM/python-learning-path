#!/usr/bin/env python3

#matchups using nested for loops

players = ["Alice", "Bob", "Charlie"]

for person in players:
    for player in players:
        if person != player:
            print(f'{person} vs {player}')

'''Alice vs Bob
Alice vs Charlie
Bob vs Alice
Bob vs Charlie
Charlie vs Alice
Charlie vs Bob'''