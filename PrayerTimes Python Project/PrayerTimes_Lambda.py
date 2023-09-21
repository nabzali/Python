import requests
import datetime
import boto3

def lambda_handler(event, context):
    
    today = datetime.date.today()
    isJummah = today.strftime("%A") == "Friday"
    #isJummah = True
    
    url = "http://18.168.179.166/Prayers_alkalaam_ig2/data.php"
    sns_client = boto3.client('sns')
    topic_arn = "arn:aws:sns:eu-west-2:426338758247:EmailTest"
    #"arn:aws:sns:eu-west-2:426338758247:PTTesting"
    #'arn:aws:sns:eu-west-2:426338758247:PrayerTimes'
    
    prayers = ["Fajr", "Zohr" if not isJummah else "Jummah", "Asr", "Magrib", "Isha"]
    todaysTimes = None
    
    def getData():
        try:
            response = requests.get(url)
            if response.status_code == 200:
                data = response.json()
                global todaysTimes 
                todaysTimes = data["today"]
            else:
                print(f"Request failed with status code {response.status_code}")
        except requests.exceptions.RequestException as e:
            print(f"Request error {e}")
    
        finally:
            return response.status_code
    
    def createPrayerDictionary():
        dictionary = {}
        for prayer in prayers:
            if prayer == "Jummah":
                dictionary["Jummah"] = [todaysTimes["Jumah_1"], todaysTimes["Jumah_2"]]
                continue
            dictionary[prayer] = [todaysTimes[f"{prayer}_Begins"], todaysTimes[f"{prayer}_Jamaat"]]
        dictionary["Sunrise"] = todaysTimes["Sunrise"]
        return dictionary
    
    def buildMessage():
        message = f'\n{today.strftime("%A %dth %B %Y")}:\n'
        message += f'Sunrise starts at: {dictionary["Sunrise"]}\n'
        for key, value in dictionary.items():
            if not key == "Sunrise":
                message += f"{key}: {value[0]} ({value[1]})\n"
    
        return message.replace("Zohr", "Zuhr").replace("Magrib", "Maghrib")[:-1]
    
    apiCall = getData()
    if apiCall not in range(200, 300):
        return {
            'statusCode': apiCall
        }
    
    dictionary = createPrayerDictionary()
    print(dictionary)
    
    response = sns_client.publish(
        TopicArn=topic_arn,
        Message=buildMessage()
    )
    
    print("Message sent:", response)

    return {
        'statusCode': 200
    }
