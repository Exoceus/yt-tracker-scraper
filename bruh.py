from selenium import webdriver
from time import sleep
from bs4 import BeautifulSoup
import datetime
import json
import re
import urllib.request

with open('sample.json', 'r') as openfile:
    data = json.load(openfile)

entertainment_time = 0
productive_time = 0

for video in data['videos']:
    if video['category'] >= 20 and video['category'] <= 24:
        entertainment_time = entertainment_time + video['duration']
    elif video['category'] >= 30 and video['category'] <= 34:
        entertainment_time = entertainment_time + video['duration']
    elif video['category'] >= 36 and video['category'] <= 44:
        entertainment_time = entertainment_time + video['duration']
    else:
        productive_time = productive_time + video['duration']

print(datetime.timedelta(seconds=entertainment_time))
print(datetime.timedelta(seconds=productive_time))

'''
AIzaSyB0MLOrsRa-7c-UsZ5-HKZINxec262TyIk

https://www.googleapis.com/youtube/v3/videos?part=snippet&id={video_id}&key=AIzaSyB0MLOrsRa-7c-UsZ5-HKZINxec262TyIk


2 - Autos & Vehicles
1 -  Film & Animation
10 - Music
15 - Pets & Animals
17 - Sports
18 - Short Movies
19 - Travel & Events
20 - Gaming
21 - Videoblogging
22 - People & Blogs
23 - Comedy
24 - Entertainment
25 - News & Politics
26 - Howto & Style
27 - Education
28 - Science & Technology
29 - Nonprofits & Activism
30 - Movies
31 - Anime/Animation
32 - Action/Adventure
33 - Classics
34 - Comedy
35 - Documentary
36 - Drama
37 - Family
38 - Foreign
39 - Horror
40 - Sci-Fi/Fantasy
41 - Thriller
42 - Shorts
43 - Shows
44 - Trailers
'''
