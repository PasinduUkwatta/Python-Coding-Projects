# coding:utf-8
import os
import json

with open(os.path.join('C:/Users/Acer/Desktop/New folder', 'wing_commander_abhinandan_feb14_march_31.json'), 'r',
          encoding='utf-8') as f1:
    ll = [json.loads(line.strip()) for line in f1.readlines()]
    total = len(ll) // 2000
    for i in range(total):
        json.dump(ll[i * 100:(i + 1) * 100], open(
            "C:/Users/Acer/Desktop/New folder/wing_commander_abhinandan_feb14_march_31_split" + str(i) + ".json", 'w',
            encoding='utf8'), ensure_ascii=False, indent=True)
