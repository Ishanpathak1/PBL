from flask import Flask, render_template, request
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
from collections import Counter

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        text = request.form["text"]
        # Tokenize words
        tokenized_words = word_tokenize(text)
        # Remove stop words
        stop_words = set(stopwords.words("english"))
        filtered_words = [word for word in tokenized_words if word.lower() not in stop_words]
        # Count bag of words
        bag_of_words = Counter(filtered_words)
        # Count sentences
        sentence_count = len(sent_tokenize(text))
        # Calculate term frequency
        total_words = len(tokenized_words)
        tf = {word: count / total_words for word, count in bag_of_words.items()}
        return render_template("index.html", tokenized_words=tokenized_words, bag_of_words=bag_of_words, sentence_count=sentence_count, tf=tf)
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)










