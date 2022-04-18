from selenium import webdriver
from time import sleep
from bs4 import BeautifulSoup
import datetime
import json
import re
import urllib.request

driver = webdriver.Chrome()

password = "Peelskills123!"
username = "mehta.r.jatin@gmail.com"

driver.get('https://stackoverflow.com/users/signup')
driver.find_element_by_xpath('//*[@id="openid-buttons"]/button[1]').click()
sleep(3)
driver.find_element_by_xpath('//input[@type="email"]').send_keys(username)
driver.find_element_by_xpath('//*[@id="identifierNext"]').click()
sleep(3)
driver.find_element_by_xpath('//input[@type="password"]').send_keys(password)
driver.find_element_by_xpath('//*[@id="passwordNext"]').click()
sleep(3)
driver.get('https://youtube.com/feed/history')

driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

sleep(10)

contents = driver.page_source
soup = BeautifulSoup(contents, 'html.parser')
watch_histories = soup.find(id='contents')

watch_histories = watch_histories.find_all('ytd-item-section-renderer')


def to_seconds(timestr):
    seconds = 0
    for part in timestr.split(':'):
        seconds = seconds*60 + int(part)
    return seconds


i = 0
data = {}
data['videos'] = []

for watch_history in watch_histories:

    header = watch_history.find(id="title").string

    videos = watch_history.find_all('ytd-video-renderer')

    date = datetime.date.today() - datetime.timedelta(days=i)

    print(date, '\n\n')

    total_time = 0

    for video in videos:
        video_info = video.find(id="video-title")
        video_link = video_info['href']

        if video_link.find('&t=') == -1:

            temp_var = video.find("ytd-thumbnail-overlay-time-status-renderer")
            temp_var = temp_var.find("span").string.replace(" ", "").strip()

            time_watched = to_seconds(temp_var)
            video_id = video_link[9:]

        else:
            index = video_link.find('&t=')
            time_watched = int(video_link[index+3:-1])
            video_id = video_link[9:index]

        total_time = total_time + time_watched
        title = video_info.find('yt-formatted-string').string

        api_key = "AIzaSyB0MLOrsRa-7c-UsZ5-HKZINxec262TyIk"

        url = f"https://www.googleapis.com/youtube/v3/videos?part=snippet&id={video_id}&key={api_key}"

        json_url = urllib.request.urlopen(url)
        YT_data = json.loads(json_url.read())

        category = int(YT_data["items"][0]["snippet"]["categoryId"])

        data['videos'].append({
            'duration': time_watched,
            'category': category,
            'date': date.strftime('%m/%d/%Y')
        })

        if i > 1:
            print(title, '\t', time_watched, '\t')

    print('Total Time Watched', datetime.timedelta(seconds=total_time))

    i = i + 1

driver.close()