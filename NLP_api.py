import io
import os
import google.cloud.language
import json
os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="C:\\Users\\HP\\Desktop\\rahul\\lifcare\\VisionAPI\\vision.json"

# Create a Language client.
language_client = google.cloud.language.LanguageServiceClient()

# TODO (Developer): Replace this with the text you want to analyze.
text = u'Hello, world!'
document = google.cloud.language.types.Document(
    content=text,
    type=google.cloud.language.enums.Document.Type.PLAIN_TEXT)

# Use Language to detect the sentiment of the text.
response = language_client.analyze_sentiment(document=document)
sentiment = response.document_sentiment

print(u'Text: {}'.format(text))
print(u'Sentiment: Score: {}, Magnitude: {}'.format(
sentiment.score, sentiment.magnitude))
                 
                