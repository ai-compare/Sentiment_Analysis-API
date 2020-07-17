import requests

# You can find the documentation here : https://documenter.getpostman.com/view/10011301/SzmiVFqh?version=latest#071c4411-5aac-47b6-bf66-fb4eb374db35

#Enter your API Token
headers = {'x-access-token': 'Enter your API Key'} #You can get your free API token here https://www.ai-compare.com/accounts/login/?next=/my_apis

# Select API
url = 'https://www.ai-compare.com/api/v1/text/create/compare/sentiment_analysis'

# Select providers, and text to analyze
payload = {'providers': '[\'google_cloud\', \'cognitives_service\', \'aws\']','text':'I am angry today', 'sentiments_to_find': 'neutral','language': 'en-US'}

# Request to AI COMPARE
response = requests.request("POST", url, headers=headers, data = payload, files = files)

# Print result
print(response.text.encode('utf8'))
