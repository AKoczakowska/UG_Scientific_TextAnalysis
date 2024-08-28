import re
from collections import Counter

import pandas as pd
from nltk.corpus import stopwords
import matplotlib.pyplot as plt
from wordcloud import WordCloud


stop_words = set(stopwords.words('english'))


custom_stop_words = {'article', 'also', 'first','one','st','author','text','well','new','used','maybe','among','made','two','analysis','research'}
stop_words.update(custom_stop_words)

df = pd.read_excel("C:/Uczelnia sem 4/abstract.xlsx", index_col=0)


abstracts = df['abstrakt (ang)'].dropna().tolist()
words = []
for abstract in abstracts:
    words.extend([word for word in re.findall(r'\b\w+\b', abstract.lower()) if word not in stop_words])

common_words = Counter(words).most_common(20)

for i, (word, count) in enumerate(common_words):
    if word == "polish":
        for j, (w, c) in enumerate(common_words):
            if w == "poland":
                common_words[j] = ("poland", c + count)
                del common_words[i]
                break

for i, (word, count) in enumerate(common_words):
    if word == "gdansk":
        for j, (w, c) in enumerate(common_words):
            if w == "gdańsk":
                common_words[j] = ("gdańsk", c + count)
                del common_words[i]
                break


print(common_words)


for word, _ in common_words:
    print("\nArtykuły zawierające słowo '{}':".format(word))
    for idx, row in df.iterrows():
        if isinstance(row['abstrakt (ang)'], str) and word in row['abstrakt (ang)'].lower():
            print("- Tytuł: {}".format(row['tytuł (ang)']))
            print("  Czasopismo: {}".format(row['czasopismo']))


wordcloud = WordCloud(width=800, height=400, background_color='white').generate_from_frequencies(dict(common_words))

plt.figure(figsize=(10, 6))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.show()

common_words = sorted(common_words, key=lambda x: x[1], reverse=True)

words, counts = zip(*common_words)
plt.figure(figsize=(10, 6))
plt.bar(words, counts, color='skyblue')
plt.xlabel('Słowo')
plt.ylabel('Częstotliwość występowania')
plt.title('20 najczęciej występujących słów')
plt.xticks(rotation=45)
plt.show()