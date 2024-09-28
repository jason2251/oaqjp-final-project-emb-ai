from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector  # Import the Watson-based emotion_detector function
app = Flask("Emotion Detection")

@app.route("/emotionDetector")
def sent_analyzer():
    # Retrieve the text to analyze from the request arguments
    text_to_analyze = request.args.get('textToAnalyze')

    # Call the emotion_detector function and store the response
    response = emotion_detector(text_to_analyze)

    # Extract emotion scores and dominant emotion
    emotion_scores = {
        'anger': response['anger'],
        'disgust': response['disgust'],
        'fear': response['fear'],
        'joy': response['joy'],
        'sadness': response['sadness']
    }
    dominant_emotion = response['dominant_emotion']

    # Return a formatted string with all emotions and their scores, and the dominant emotion
    return (
        f"For the given statement, the system response is 'anger': {emotion_scores['anger']:.9f}, "
        f"'disgust': {emotion_scores['disgust']:.9f}, 'fear': {emotion_scores['fear']:.9f}, "
        f"'joy': {emotion_scores['joy']:.7f} and 'sadness': {emotion_scores['sadness']:.9f}. "
        f"The dominant emotion is **{dominant_emotion}**."  
    )

@app.route("/")
def render_index_page():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
