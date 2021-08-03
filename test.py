import json

def split(word):
    return [char for char in word]

with open('cogs/events.json','r') as file:
  data = json.loads(file.read())

while True:
  inp = input ('Current Time: ')
  temp = split(inp)
  day = temp[0] + temp[1]
  hour = temp[3] + temp[4]
  minute = temp[6] + temp[7]
  for event in data['events']:
    if event['time'] == inp:
      name = event['name']
      print(f'Executing event {name}.')
    elif event['time'] != inp:
      name = event['name']
      print(f'Event {name}\'s provided time does not match current time.')
