import random 
import datetime

def bdaymessagespy():

  bday_messages = ['Hope you have a very Happy Birthday! 🎈',
  'Its your special day – get out there and celebrate! 🎉',
  'You were born and the world got better – everybody wins! 🥳',
  'Have lots of fun on your special day! 🎂',
  'Another year of you going around the sun! 🌞'] 

  random_message = random.choice(bday_messages)

today = datetime.date.today()
next_birthday = datetime.date(2026, 3, 11)

days_away = next_birthday - today

if today == next_birthday:
  print(bdaymessagespy())
else:
  print('My next birthday is ', days_away ,' days away!')

# this took 4 years to complete

