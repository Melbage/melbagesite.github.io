import json

#with open('./Code/JSON/Data/ExampleSc.json') as Schema:
with open('./Code/JSON/Data/ExampleSCv2.json') as Schema:
    PlayerScoreCard = json.load(Schema)

#print(PlayerScoreCard)
#print(PlayerScoreCard['Properties'])
#print(PlayerScoreCard['Event'])
#print(PlayerScoreCard['ScoreCard']['Holes'])

for enum,Hole in enumerate(PlayerScoreCard['ScoreCard']['Holes']):
    if enum ==0 : #this should be the totals
        print(Hole)
        Hole['Ferrits'] = '18'
        print(Hole)