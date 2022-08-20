import requests
import json
from rasa_sdk import Action


class CallHuman(Action):
  def name(self):
    return 'action_call_human'

  def run(self, dispatcher, tracker, domain):
    dispatcher.utter_message(text='Publicando mensagem no MQTT...')
    return []

class MOZ(Action):
  def name(self):
    return 'action_MOZ'

  def run(self, dispatcher, tracker, domain):
    should_call_moz = tracker.get_slot('moz_questions')
    for slot in tracker.slots:
      print(slot, ":", tracker.get_slot(slot))
    print('*' * 50)

    if should_call_moz:
      dispatcher.utter_message(text='Publicando mensagem no MQTT...')
      dispatcher.utter_message(text='Ativando MÁGICO DE OZ...')
    else:
      dispatcher.utter_message(text='MÁGICO DE OZ não será chamado...')

    return []