import io
import os
import math
import json
import argparse
import sys

from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types
import six

os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="C:\\Users\\HP\\Desktop\\rahul\\lifcare\\VisionAPI\\vision.json"

def entities_text(movie_review_filename):
    """Detects entities in the text."""
    client = language.LanguageServiceClient()

#    if isinstance(text, six.binary_type):
#        text = text.decode('utf-8')
    with open(movie_review_filename, 'r', encoding='utf-8') as review_file:
        content = review_file.read()

    # Instantiates a plain text document.
    document = types.Document(
        content=content,
        type=enums.Document.Type.PLAIN_TEXT)

    # Detects entities in the document. You can also analyze HTML with:
    #   document.type == enums.Document.Type.HTML
    entities = client.analyze_entities(document).entities
    text_files = open("medicinenlp.txt", "w", encoding='utf-8')
    # entity types from enums.Entity.Type
    entity_type = ('UNKNOWN', 'PERSON', 'LOCATION', 'ORGANIZATION',
                   'EVENT', 'WORK_OF_ART', 'CONSUMER_GOOD','MEDICINE_NAME', 
                   'SALTS', 'MOLECULES', 'GUIDELINES', 'OTHER')

    for entity in entities:
        #text_files.write('=' * 20)
        text_files.write(entity.name)
        #text_files.write(u'{:<16}: {}'.format('type', entity_type[entity.type]))  
        #text_files.write(u'{:<16}: {}'.format('metadata', entity.metadata))  
        #text_files.write(u'{:<16}: {}'.format('salience', entity.salience)) 
        #text_files.write(u'{:<16}: {}'.format('wikipedia_url',
        #    entity.metadata.get('wikipedia_url', '-')))  
    text_files.close()        
#entities_text('Joanne Rowling, who writes under the pen names J. K. Rowling and Robert Galbraith, is a British novelist and screenwriter who wrote the Harry Potter fantasy series.')
if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument(
        'movie_review_filename',
        help='The filename of the movie review you\'d like to analyze.')
    args = parser.parse_args()

    entities_text(args.movie_review_filename)