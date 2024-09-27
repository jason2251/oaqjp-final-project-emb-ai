from EmotionDetection.emotion_emotion import emotion_detector
import unittest

class TestEmotionDetector(unittest.TestCase):
    def test_sentiment_analyzer(self):
        # Test case for positive sentiment
        result_1 = emotion_detector('I love working with Python')
        self.assertEqual(result_1['label'], 'SENT_POSITIVE')
        
        # Test case for negative sentiment
        result_2 = emotion_detector('I hate working with Python')
        self.assertEqual(result_2['label'], 'SENT_NEGATIVE')
        
        # Test case for neutral sentiment
        result_3 = emotion_detector('I am neutral on Python')
        self.assertEqual(result_3['label'], 'SENT_NEUTRAL')

unittest.main()
