# import random
# from instagrapi import Client
# from instagrapi.exceptions import ClientLoginRequired

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
# client = Client()
# client.login(username , password)


# hashtag= {"animals" , "mythology"}
# comments = ["Awesome", "Great", "Gorgeous"]
# medias= client.hashtag_medias_recent(hashtag, 20)

# client = Client()
# for i, media_id in enumerate(medias):
#     if i % 5 == 0:
#         comment = random.choice(comments)
#         client.media.comment(media_id, comment)
#         print(f"Commented '{comment}' under post number {i+1} for user {i + 1}")

import random
from instagrapi import Client
from instagrapi.exceptions import ClientLoginRequired, LoginRequired

# Define your Instagram credentials
username = "kiks_group"
password = "pythongroupwork"

# Login function
def login_instagram(username, password):
    try:
        client = Client()
        client.login(username, password)
        print("Logged in successfully!")
        return client
    except (ClientLoginRequired, LoginRequired):
        print("Login failed. Please check your username and password.")
    except Exception as e:
        print("An error occurred:", e)
    return None

# Main function to perform actions
def main():
    # Login to Instagram
    client = login_instagram(username, password)
    if client:
        try:
            # Define hashtags and comments
            hashtags = ["animals", "mythology"]
            comments = ["Awesome", "Great", "Gorgeous"]

            # Fetch recent media for each hashtag
            for hashtag in hashtags:
                medias = client.hashtag_medias_recent(hashtag, 20)
                for i, media in enumerate(medias):
                    if i % 5 == 0:
                        # Comment on the post
                        comment = random.choice(comments)
                        client.media_comment(media.pk, comment)  # Use client.media_comment instead of client.post_comment
                        print(f"Commented '{comment}' under post number {i+1} for user {media.user.username}")
        except Exception as e:
            print("An error occurred:", e)

if __name__ == "__main__":
    main()
