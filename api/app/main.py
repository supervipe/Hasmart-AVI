import traceback

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import requests
import helpers
import settings

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class Message(BaseModel):
    sender: str
    text: str


@app.get("/")
async def read_root():
    return {"message": "OK"}


@app.post("/messages")
async def read_item(message: Message):
  try:
    r = requests.post(settings.RASA_WEBHOOK_URL, json={'sender': message.sender, 'message': message.text})
    res = r.json()
    for response in res:
      response['audio_name'] = helpers.text_to_md5(response.text)
  except Exception as e:
    res = {'message': 'ops'}
    print('[ERROR] ' + traceback.format_exc())
  finally:
    return res
