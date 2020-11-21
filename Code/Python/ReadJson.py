import json

#with open('./Code/JSON/Data/ExampleSc.json') as Schema:
with open('/Users/paulcarter/Documents/GITHUB/Melbage/Melbagesite/melbagesite.github.io/Code/JSON/Data/PlayersScoreCardTmplate.json') as Schema:
    PlayerScoreCard = json.load(Schema)

#print(PlayerScoreCard)
#print(PlayerScoreCard['Properties'])
#print(PlayerScoreCard['Event'])
#print(PlayerScoreCard['ScoreCard']['Holes'])
TSI =0
for enum,Hole in enumerate(PlayerScoreCard['ScoreCard']['Holes']):
    if enum ==0 : #this should be the totals
        print(Hole)
        print(type(Hole))
        Hole['Ferrits'] = 18
        print(Hole)
    TSI= TSI+Hole['StokeIndex']
#print(TSI)

print(PlayerScoreCard['ScoreCard']['Holes'][0]['StokeIndex'])
PlayerScoreCard['ScoreCard']['Holes'][0]['StokeIndex'] = TSI
print(PlayerScoreCard['ScoreCard']['Holes'][0]['StokeIndex'])
print(PlayerScoreCard)