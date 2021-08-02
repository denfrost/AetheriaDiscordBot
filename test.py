import json

with open('cogs/events.json','r') as file:
  data = json.loads(file.read())

while True:
  io = input ('Current Time: ')
  for event in data['events']:
    if event['time'] == io:
      name = event['name']
      print(f'Executing event {name}.')
    elif event['time'] != io:
      name = event['name']
      print(f'Event {name}\'s provided time does not match current time.')
