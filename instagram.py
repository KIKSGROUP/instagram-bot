from instagrapi import Client

client = Client()
client.login(username, password)

hashtag = "programming"

medias - client.hashtag_medias_recent(hashtag, 20)
for i, media in enumerate(medias):
    print(f"Liked post number {i+1} of hashtag {hashtag}")
    