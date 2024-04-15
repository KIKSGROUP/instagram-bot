#instagram can ban you if you act like a bot!
#ideas - follow/unfollow, like, comment users based on hashtags

from instagrapi import Client
from instagrapi.exceptions import ClientLoginRequired
import random



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

hashtag = "mythology"
comments = ["Awesome", "Great", "Gorgeous"]

medias= client.hashtag_medias_recent(hashtag , 20)

for i, media in enumerate(medias):
    if i % 5 == 0:
        client.user_follow(media.user.pk)
        print(f"followed user {media.user.username}")
        comment = random.choice(comments)
        client.media_comment(media.pk, comment)
        print(f"Commented '{comment}' under post number {i + 1} for user {media.user.username}")

