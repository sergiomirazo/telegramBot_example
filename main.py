import requests

# Access token to the Telegram API 
token = "YOUR_TOKEN"

# Chat ID thats the message will be sent
chat_id = "YOUR_ID"

# Text message
texto = "Hello world, this is a message"

# The url of the Api telegram
url = f"https://api.telegram.org/bot{token}/sendMessage"

# Parameters for the callback
params = {
    "chat_id": chat_id,
    "text": texto
}

# Callback to the api
response = requests.post(url, params=params)

# Verification  for the result
if response.status_code == 200:
    print("Message sent successfuly")
else:
    print("Error sending message")
