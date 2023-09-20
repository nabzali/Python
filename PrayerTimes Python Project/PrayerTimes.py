import requests
import datetime
import boto3

today = datetime.date.today()
isJummah = today.strftime("%A") == "Friday"
isJummah = False

url = "http://18.168.179.166/Prayers_alkalaam_ig2/data.php"
try:
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
    else:
        print(f"Request failed with status code {response.status_code}")
except requests.exceptions.RequestException as e:
    print(f"Request error {e}")

todaysTimes = data["today"]
dictionary = {}

# def printPrayerTimes(prayers):
#     print(f'Sunrise is at: {dictionary["Sunrise"]}')
#     for key, value in dictionary.items():
#         if not key == "Sunrise":
#             print(f'{key}: {value[0]} ({value[1]})')
    

prayers = ["Fajr", "Zohr" if not isJummah else "Jummah", "Asr", "Magrib", "Isha"]

for prayer in prayers:
    if prayer == "Jummah":
        dictionary["Jummah"] = [todaysTimes["Jumah_1"], todaysTimes["Jumah_2"]]
        continue
    dictionary[prayer] = [todaysTimes[f"{prayer}_Begins"], todaysTimes[f"{prayer}_Jamaat"]]
dictionary["Sunrise"] = todaysTimes["Sunrise"]

print(dictionary)

sns_client = boto3.client('sns')

# Replace 'your_topic_arn' with the ARN of the SNS topic you created
topic_arn = 'arn:aws:sns:eu-west-2:426338758247:PrayerTimes'

# Your message
message = f'\nSunrise starts at {dictionary["Sunrise"]}\n'

for key, value in dictionary.items():
    if not key == "Sunrise":
        message += f"{key}: {value[0]} ({value[1]})\n"
message = message[:-1]

response = sns_client.publish(
    TopicArn=topic_arn,
    Message=message
)

print("Message sent:", response)
