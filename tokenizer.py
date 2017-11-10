from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import sys
import re
import string
searchString = str(sys.argv[1])
tokenizedString = word_tokenize(searchString)
regex = re.compile('[%s]' % re.escape(string.punctuation))
tokenizedStringNoPunctuation = list()
for token in tokenizedString:
    newToken = regex.sub(u'', token)
    if not newToken == u'':
        tokenizedStringNoPunctuation.append(newToken)
tokenizedStringNoStopwords = list()
for token in tokenizedStringNoPunctuation:
    if token not in stopwords.words('english'):
        tokenizedStringNoStopwords.append(token)
print(tokenizedStringNoStopwords)
# Send the tokenized list to the elastic search function
# Get the results back as a json object
# Return the json object to the webpage