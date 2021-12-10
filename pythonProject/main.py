import pandas as pd
import json

##f = open('worldcup.json')

jsonWc = json.loads('worldcup.json')

print(jsonWc)
#worldcup = pd.read_json(jsonWc)#pd.json_normalize('worldcup.json')

# normalized_wc = pd.json_normalize(worldcup, record_path=['rounds'], meta= [])

normalized_wc = pd.json_normalize(jsonWc)

#worldcup = pd.read_json('worldcup.json')

#normalizado = pd.json_normalize(worldcup)
print(normalized_wc)


#Flatten students
#pd.json_normalize(data, record_path=['students'])
