from internet_speed_twitter_bot import InternetSpeedTwitterBot
# import requests
#
# url = "https://login.kt.com/wamui/AthWebPopup.do?urlcd=http%3A%2F%2Fspeed.kt.com%2Fspeed%2Fspeedtest%2Fintroduce.asp"
# response = requests.get(url)
# html_content = response.text
#
# print(html_content)

internet_speed_twitter_bot = InternetSpeedTwitterBot()

internet_speed_twitter_bot.get_internet_speed()
internet_speed_twitter_bot.tweet_at_provider()




