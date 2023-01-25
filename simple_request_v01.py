import requests
import datetime

url = input("Please enter the URL: ")
response = requests.get(url)

# Create the filename with today's date
today = datetime.date.today()
filename_txt = 'simple_request_' + today.strftime("%Y-%m-%d") + '.txt'

# Output result into a text file
with open(filename_txt, 'w') as f:
    f.write(response.text)
