# Sentiment Analysis - Eden AI API
## Description
This repositery provides code to implement Eden AI Sentiment Analysis API. Eden AI Sentiment Analysis API allows to call Sentiment Analysis APIs from multpile sentiment analysis providers. It permits to get results from these providers, compare the results, siwtch between providers or combine them.

## What is AI-Compare ?
[Eden AI](https://www.edanai.co/) is a SaaS providing APIs connected to big (AWS, GCP, etc.) and small AI providers for vision, text, audio, OCR, prediction and translation AI engines. Our solution allows users to compare the performance of these providers APIs according to their data and use them directly via our API thus offering great flexibility and making it very easy to change supplier. In particular, we offer better performance with the "Genius" feature that cleverly combines results from multiple providers.

Eden AI offers community offer (free) when you [create your account for free](https://app.edenai.run/user/login). You can then use [APIs](https://api.edenai.run/v1/redoc/), use the [interface](https://app.edenai.run/bricks/default), manage your account, access to cost management.

You can find APIs documentation here : https://api.edenai.run/v1/redoc/

## Usage
### Initialization
Enter your access token and select your API endpoint. You can get your token on your account manager [here](https://www.ai-compare.com/accounts/login/?next=/my_apis/my_account).
```python
import requests
headers = {  'Authorization': 'Bearer your API Key'}
url = 'https://dev-api.edenai.run/v1/pretrained/text/sentiment_analysis'
```
### Select parameters 
Set your text, the language, the attempted result, and providers APIs you want to run :
```python
payload = {'providers': '[\'ibm\', \'microsoft\', \'aws\', \'google_cloud\']','text':'I am angry today', 'sentiments_to_find': 'neutral','language': 'en-US'}
```
### Get results
```python
response = requests.request("POST", url, headers=headers, data = payload, files = files)
print(response.text.encode('utf8'))
```

## Response example
<details>
<summary>

```json
{
  "result": [{"solution_name": "Google cloud","execution_time": "1.839108","result": {"text": "The score of a document's sentiment indicates the overall emotion of a document. The magnitude of a document's sentiment indicates how much emotional content is present within the document, and this value is often proportional to the length of the document.","sentiments": ["Positive"],"sentiment_rate": [0.2]},"api_response": {"documentSentiment": {"magnitude": 0.4,"score": 0.2},
```

</summary>

```


{
  "result": [
    {
      "solution_name": "Google cloud",
      "execution_time": "1.839108",
      "result": {
        "text": "The score of a document's sentiment indicates the overall emotion of a document. The magnitude of a document's sentiment indicates how much emotional content is present within the document, and this value is often proportional to the length of the document.",
        "sentiments": [
          "Positive"
        ],
        "sentiment_rate": [
          0.2
        ]
      },
      "api_response": {
        "documentSentiment": {
          "magnitude": 0.4,
          "score": 0.2
        },
        "language": "fr-FR",
        "sentences": [
          {
            "text": {
              "content": "The score of a document's sentiment indicates the overall emotion of a document.",
              "beginOffset": 0
            },
            "sentiment": {
              "magnitude": 0.1,
              "score": 0.1
            }
          },
          {
            "text": {
              "content": "The magnitude of a document's sentiment indicates how much emotional content is present within the document, and this value is often proportional to the length of the document.",
              "beginOffset": 81
            },
            "sentiment": {
              "magnitude": 0.3,
              "score": 0.3
            }
          }
        ]
      },
      "found_sentiments": 0
    },
    {
      "solution_name": "Ibm",
      "execution_time": "1.539684",
      "result": {
        "text": "The score of a document's sentiment indicates the overall emotion of a document. The magnitude of a document's sentiment indicates how much emotional content is present within the document, and this value is often proportional to the length of the document.",
        "sentiments": [
          "negative"
        ],
        "sentiment_rate": [
          0.358381
        ]
      },
      "api_response": {
        "usage": {
          "text_units": 1,
          "text_characters": 257,
          "features": 1
        },
        "sentiment": {
          "document": {
            "score": -0.358381,
            "label": "negative"
          }
        },
        "language": "en"
      },
      "found_sentiments": 0
    },
    {
      "solution_name": "Microsoft Azure",
      "execution_time": "0.750626",
      "result": {
        "text": "The score of a document's sentiment indicates the overall emotion of a document. The magnitude of a document's sentiment indicates how much emotional content is present within the document, and this value is often proportional to the length of the document.",
        "sentiments": [
          "positive"
        ],
        "sentiment_rate": [
          0.7244399189949036
        ]
      },
      "api_response": {
        "documents": [
          {
            "id": "1",
            "score": 0.7244399189949036
          }
        ],
        "errors": []
      },
      "found_sentiments": 0
    },
    {
      "solution_name": "Amazon Web Services",
      "execution_time": "0.414591",
      "result": {
        "text": "The score of a document's sentiment indicates the overall emotion of a document. The magnitude of a document's sentiment indicates how much emotional content is present within the document, and this value is often proportional to the length of the document.",
        "sentiments": [
          "Positive",
          "Negative",
          "Neutral",
          "Mixed"
        ],
        "sentiment_rate": [
          0.6242444515228271,
          0.009806307032704353,
          0.3659137487411499,
          0.000035498022043611854
        ]
      },
      "api_response": {
        "Sentiment": "POSITIVE",
        "SentimentScore": {
          "Positive": 0.6242444515228271,
          "Negative": 0.009806307032704353,
          "Neutral": 0.3659137487411499,
          "Mixed": 0.000035498022043611854
        },
        "ResponseMetadata": {
          "RequestId": "1803e418-a6d0-45af-8ed9-8f3d0ec9dd37",
          "HTTPStatusCode": 200,
          "HTTPHeaders": {
            "x-amzn-requestid": "1803e418-a6d0-45af-8ed9-8f3d0ec9dd37",
            "content-type": "application/x-amz-json-1.1",
            "content-length": "164",
            "date": "Tue, 10 Mar 2020 08:45:03 GMT"
          },
          "RetryAttempts": 0
        }
      },
      "found_sentiments": 1
    }
  ]
}


```

</details>

## Blog articles
We provides on our website some [blog articles on AI engines](https://www.edenai.co/blog)

## Contact
If you have any question or request, you can contact us at contact@edenai.com

## Terms of use
You can access to our terms [here](https://www.edenai.co/terms) on our website.

#
![Screenshot](https://github.com/ai-compare/Speech_to_text-API/blob/ba9d4f1668d8758141f24240d1287640b4211c63/Logo%20complet%20Eden%20AI%20-%20format%20PNG.png)

