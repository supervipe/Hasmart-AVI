import settings
import requests


print(settings.RASA_WEBHOOK_URL)

try:
  r = requests.post(settings.RASA_WEBHOOK_URL, json={'sender': 'joao', 'message': 'Bom dia'})
  print(r.json())
except:
  print({'message': 'ops'})
