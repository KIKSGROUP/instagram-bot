import random
from instagrapi import Client
from instagrapi.exceptions import ClientLoginRequired



username = "kiks_group"
password = "pythongroupwork"

try:
    client = Client()
    client.login(username, password)
    print("Logged in successfully!")
except ClientLoginRequired:
    print("Login failed. Please check your username and password.")
except Exception as e:
    print("An error occurred:", e)

client = Client()
client.login(username , password)
media_ids = [
    "B1234567890",    
]  

usernames = [
    "kiks_group"
]

comments = ["Awesome", "Great", "Gorgeous"]

client = Client()

for i, media_id in enumerate(media_ids):

    comment = random.choice(comments)
    
    client.media.comment(media_id, comment)
    
    print(f"Commented '{comment}' under post number {i+1} for user {usernames[i]}")
