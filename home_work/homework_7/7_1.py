#!/usr/bin/python3

chess_players = {"Carlsen, Magnus": 1865,
                 "Firouzja, Alireza": 2804,
                 "Ding, Liren": 2799,
                 "Caruana, Fabiano": 1792,
                 "Nepomniachtchi, Ian": 2773}
new_chess_players = {k: v.split()[0].replace(',', ' ') + v.split()[1][0] + '.' for v, k in chess_players.items() if int(k) > 2000}
for k, v in new_chess_players.items():
    print(k, v)
