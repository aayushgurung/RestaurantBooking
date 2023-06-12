import json

with open('C:/TEST FINAL YEAR/image.json', 'r', encoding='utf-8') as f:
    data = json.load(f)
    
print(len(data))