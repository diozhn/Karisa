import requests
import json

def buscar_dados(url):
  request = requests.get(url)
  todos = json.loads(request.content)
  ##print(todos)
  return todos
