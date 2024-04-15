# from instagrapi import Client
# import random
# from instagrapi.exceptions import LoginRequired
# import logging
# from time import sleep

# USER_NAME = "Kiks_group"
# PASSWORD = "pythongroupwork"
# cl = Client()
# cl.login(USER_NAME , PASSWORD)



# logger = logging.getLogger()

# def login_user():
#     """
#     Attempts to login to Instagram using either the provided session information
#     or the provided username and password.
#     """

#     cl = Client()
#     session = cl.load_settings("session.json")

#     login_via_session = False
#     login_via_pw = False

#     if session:
#         try:
#             cl.set_settings(session)
#             cl.login(USER_NAME, PASSWORD)

#             # check if session is valid
#             try:
#                 cl.get_timeline_feed()
#                 print("Logged In!!")
#                 return cl
#             except LoginRequired:
#                 print(
#                     "Session is invalid, need to login via username and password")

#                 old_session = cl.get_settings()

#                 # use the same device uuids across logins
#                 cl.set_settings({})
#                 cl.set_uuids(old_session["uuids"])

#                 cl.login(USER_NAME, PASSWORD)
#             login_via_session = True
#         except Exception as e:
#             print(
#                 "Couldn't login user using session information: %s" % e)

#     if not login_via_session:
#         try:
#             print(
#                 "Attempting to login via username and password. username: %s" % USER_NAME)
#             if cl.login(USER_NAME, PASSWORD):
#                 login_via_pw = True
#         except Exception as e:
#             print(
#                 "Couldn't login user using username and password: %s" % e)

#     if not login_via_pw and not login_via_session:
#         raise Exception("Couldn't login user with either password or session")

# def pick_hash_tags(client):

#     hashtag = {"animals", "mythology"}

#     medias = client.hashtag_medias_recent("animals", 20)

#     for i, media in enumerate(medias):
#         if i % 5 == 0:
#             client.user_follow(media.user.pk)
#             print(f"We just followed {media.user.username}")
#             sleep(5)

            # print(f"followed user {media.user.username}")
            # comment = random.choice(comments)
            # client.media.comment(comment)
            # print(f"Commented '{comment}' under post number {
            #       i + 1} for user {media.user.username}")

#     print("Done!!")


# session = login_user()
# pick_hash_tags(session)



import logging
import random
from time import sleep
from instagrapi import Client
from instagrapi.exceptions import LoginRequired, FeedbackRequired, ClientLoginRequired


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


USERNAME = "Kiks_group"
PASSWORD = "pythongroupwork"

def login_user():
    cl = Client()
    try:
        cl.login(USERNAME, PASSWORD)
        logger.info("Logged in successfully.")
        return cl
    except (LoginRequired, ClientLoginRequired) as e:
        logger.error(f"Login required: {e}")
    except Exception as e:
        logger.error(f"Failed to login: {e}")


def follow_accounts(client, hashtags, max_follows=20):
    try:
        for hashtag in hashtags:
            medias = client.hashtag_medias_recent(hashtag, max_follows)
            for i, media in enumerate(medias):
                if i % 5 == 0:
                    try:
                        client.user_follow(media.user.pk)
                        logger.info(f"Followed user: {media.user.username}")
                        sleep(random.randint(10, 30))
                        if i % 100 == 0:
                            sleep(random.randint(600, 900)) 
                    except FeedbackRequired as e:
                        logger.error(f"Feedback required: {e}")
                        sleep(random.randint(600, 900))  # Wait before retrying
            logger.info(f"Finished following accounts for #{hashtag}.")
    except FeedbackRequired as e:
        logger.error(f"Feedback required: {e}")
        sleep(random.randint(600, 900))  # Wait before retrying
    except Exception as e:
        logger.error(f"Error following accounts: {e}")



def main():
    try:
        client = login_user()
        if client:
            hashtags = ["animals", "mythology"] 
            follow_accounts(client, hashtags)
    except Exception as e:
        logger.error(f"An error occurred: {e}")

if __name__ == "__main__":
    main()


