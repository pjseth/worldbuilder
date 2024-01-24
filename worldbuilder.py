from openai import OpenAI
client = OpenAI()

print('Enter character name:')
character_name = input()

print('Enter superpower:')
superpower = input()

print('Enter race:')
race = input()

print('Enter age:')
age = input()

completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are a professional writer who is meant to complete the next three sentences from the user's given sentence"},
    {"role": "user", "content": f"My character's name is {character_name}. They have the superpower of {superpower}. They are {race} and {age} years old."}
  ]
)

print(completion.choices[0].message)
