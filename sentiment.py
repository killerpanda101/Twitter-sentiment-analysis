import pandas as pd 

df = pd.read_csv("tweets.csv")
tweets = list(df["Tweet_Text"])
teeee = []

for text in tweets:
	# split into words
	from nltk.tokenize import word_tokenize
	tokens = word_tokenize(text)

	# convert to lower case
	tokens = [w.lower() for w in tokens]

	# remove remaining tokens that are not alphabetic
	words = [word for word in tokens if word.isalpha()]

	# filter out stop words
	# stop words are like ['i', 'me', 'my', 'myself', 'we', 'our', 'ours'...]
	# they stitch together sentenses and are not useful for anlysis  
	from nltk.corpus import stopwords
	stop_words = set(stopwords.words('english'))
	words = [w for w in words if not w in stop_words]

	import string
	temp = "".join([" "+i if not i.startswith("'") and i not in string.punctuation else i for i in words]).strip()
	teeee.append(temp)
	

from textblob import TextBlob
analysis = []
for text in teeee:
	analysis.append(TextBlob(text).sentiment.polarity)

neutral = 0
negetive = 0
positive = 0

for data in analysis:
	if data > 0:
		positive += 1
	elif data == 0:
		neutral += 1
	else:
		negetive += 1


print(negetive, positive, neutral)