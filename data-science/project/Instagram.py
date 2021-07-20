from datetime import datetime
import instaloader
import numpy as np



km = np.loadtxt('files/carros-km.txt', delimiter=',')




print(km)



login = instaloader.Instaloader()
login.login('marco.bacelo@gmail.com', 'sazuke2018')

posts = instaloader.Profile.from_username(login.context, "marcobacelo").get_posts()

SINCE = datetime(2020,6,7)
UNTIL = datetime(2021,6,11)

for post in posts:
    if(post.date >= SINCE) and (post.date <= UNTIL):
        print(post.date)
        login.download_post(post, "insta-posts-downloads")
