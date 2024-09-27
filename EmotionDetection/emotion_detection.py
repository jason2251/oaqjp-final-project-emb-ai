import requests  # Import the requests library to handle HTTP requests
import json

def emotion_detector(text_to_analyze):  # Define a function named emotion_detector that takes a string input (text_to_analyze)
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = { "raw_document": { "text": text_to_analyze } }
    
    # Send a POST request to the API with the text and headers
    response = requests.post(url, json=myobj, headers=header)
    
    # Parsing the JSON response from the API
    formatted_response = json.loads(response.text)
    
    # Extracting emotion and score from the response
    emotion_data = formatted_response['emotionPredictions'][0]['emotion']
    
    # Finding the dominant emotion
    dominant_emotion = max(emotion_data, key=emotion_data.get)
    
    # Returning a dictionary containing sentiment analysis results
    return {
        'anger': emotion_data['anger'],
        'disgust': emotion_data['disgust'],
        'fear': emotion_data['fear'],
        'joy': emotion_data['joy'],
        'sadness': emotion_data['sadness'],
        'dominant_emotion': dominant_emotion
    }