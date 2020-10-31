import json
import jsonschema
from jsonschema.validator import Draft7Validator



 #Load Shema files , remebering that Json schemas are also  Json files!
with open('../../Schemas/PlayersScoreCard.json') as Schema:
    PlayerScoreCardSchema = json.load(Schema)
  
IsValid = jsonschema.validator(PlayerScoreCardSchema)
  
print(IsValid)