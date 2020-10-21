# Sentiment Analysis - AI-Compare API
## Description
This repositery provides code to implement [AI-Compare Sentiment Analysis API](https://www.ai-compare.com/text_apis/sentiment_analysis/). [AI-Compare Sentiment Analysis API](https://www.ai-compare.com/text_apis/sentiment_analysis/) allows to call Sentiment Analysis APIs from Google Cloud Platform Natural Language, AWS Comprehend, Microsoft Azure Cognitives Service Language, and IBM Watson Natural Language Understanding. It permits to get results from these providers and compare the results.

## What is AI-Compare ?
[AI-Compare](https://www.ai-compare.com/) is a SaaS providing APIs connected to big (AWS, GCP, etc.) and small AI providers: [object detection](https://www.ai-compare.com/vision_apis/object_detection), [OCR](https://www.ai-compare.com/vision_apis/ocr), [NLP](https://www.ai-compare.com/text_apis/sentiment_analysis/), [speech-to-text](https://www.ai-compare.com/audio_apis/speech_recognition), custom vision, etc. Our solution allows users to compare the performance of these providers APIs according to their data and use them directly via our API thus offering great flexibility and making it very easy to change supplier. In particular, we offer better performance with the "Genius" feature that cleverly combines results from multiple providers.

AI-Compare offers 2$ free credits when you [create your account for free](https://www.ai-compare.com/accounts/login/?next=/my_apis). You can then use [APIs](https://www.ai-compare.com/v1/redoc/), use the [interface](https://www.ai-compare.com/my_apis), manage your account and have access to all the APIs.

You can find APIs documentation here : https://www.ai-compare.com/v1/redoc/

## Usage
### Initialization
Enter your access token and select your API endpoint. You can get your token on your account manager [here](https://www.ai-compare.com/accounts/login/?next=/my_apis/my_account).
```python
import requests
headers = {  'Authorization': 'Bearer your API Key'}
url = 'https://www.ai-compare.com/v1/pretrained/text/sentiment_analysis'
```
### Select parameters 
Set your text, the language, the attempted result, and providers APIs you want to run :
```python
payload = {'providers': '[\'ibm\', \'cognitives_service\', \'aws\', \'google_cloud\']','text':'I am angry today', 'sentiments_to_find': 'neutral','language': 'en-US'}
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

## FAQ
Here you can access to AI-Compare [FAQ](https://www.ai-compare.com/faq/).

## Use cases
We provides on our website some [use cases examples for NLP APIs](https://www.ai-compare.com/use_cases_nlp/)

## Contact
If you have any question or request, you can contact us at contact@ai-compare.com

## Terms of use
You can access to our terms [here](https://www.ai-compare.com/terms/) on our website.

#
![Screenshot](Ai-compare_new.png)

