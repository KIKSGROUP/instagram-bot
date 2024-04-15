# Instagram can ban you if you act like a bot!
# Ideas - follow/unfollow, like, comment users based on hashtags

# import random
# from instagrapi import Client
# from instagrapi.exceptions import ClientLoginRequired, ClientNotFoundError

# username = "kiks_group"
# password = "pythongroupwork"

# try:
#     client = Client()
#     client.login(username, password)
#     print("Logged in successfully!")
# except ClientLoginRequired:
#     print("Login failed. Please check your username and password.")
# except Exception as e:
#     print("An error occurred:", e)

# hashtag = "animals" 

# comments = ["Awesome", "Great", "Gorgeous"]

# medias= client.hashtag_medias_recent(hashtag , 20)




# for i, media in enumerate(medias):
#     client.media_like(media.id)
#     if i % 5 == 0:
#         try:
#             client.user_follow(media.user.pk)
#             print(f"Followed user {media.user.username}")
#             comment = random.choice(comments)
#             client.media.comment(media.pk, comment)  # Corrected method call to comment on media
#             print(f"Commented '{comment}' under post number {i + 1} for user {media.user.username}")
#         except Exception as e:
#             print(f"An error occurred while interacting with user {media.user.username}: {e}")

import random
import time
from instagrapi import Client
from instagrapi.exceptions import ClientLoginRequired, ClientNotFoundError

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

hashtag = "animals"

comments = ["Awesome", "Great", "Gorgeous"]

try:
    medias = client.hashtag_medias_recent(hashtag, 20)

    for i, media in enumerate(medias):
        client.media_like(media.id)

        # Follow user and leave a comment every 5th media
        if i % 5 == 0:
            try:
                # Follow the user
                client.user_follow(media.user.pk)
                print(f"Followed user {media.user.username}")

                # Pause for a random duration before commenting
                time.sleep(random.randint(10, 30))

                # Select a random comment and post it
                comment = random.choice(comments)
                client.media_comment(media.pk, comment)
                print(f"Commented '{comment}' under post number {i + 1} for user {media.user.username}")

                # Pause again before proceeding to the next iteration
                time.sleep(random.randint(20, 40))
            except Exception as e:
                print(f"An error occurred while interacting with user {media.user.username}: {e}")

        # Pause between interactions to appear more natural
        time.sleep(random.randint(10, 20))

except ClientNotFoundError:
    print("Error: Hashtag not found.")
except Exception as e:
    print("An error occurred while fetching medias:", e)




