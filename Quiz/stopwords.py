from nltk.corpus import stopwords
#import nltk
#nltk.download()
sw = stopwords.words("english")
print len(sw)

from nltk.stem.snowball import SnowballStemmer
stemmer = SnowballStemmer("english")
print(stemmer.stem("daughters"))