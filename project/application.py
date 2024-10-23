from flask import Flask, request, jsonify
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
import pickle

app = Flask(__name__)

### model loading ###
loaded_model = None
with open('basic_classifier.pkl', 'rb') as fid:
    loaded_model = pickle.load(fid)

vectorizer = None
with open('count_vectorizer.pkl', 'rb') as vd:
    vectorizer = pickle.load(vd)

#how to use model to predict
prediction = loaded_model.predict(vectorizer.transform(["This is a fake news"]))[0]

# output will be 'Fake' if fake, 'REAL' if real


@app.route('/')
def index():
    return "This is a fake news detector"

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get the text data from the post request
        data = request.get_json()
        
        # Check if 'text' key is in the request JSON
        if 'text' not in data:
            return jsonify({"error": "Missing 'text' key in the request"}), 400
        
        text = data['text']

        # Make prediction
        prediction = loaded_model.predict(vectorizer.transform([text]))[0]
        return jsonify({'prediction': prediction})
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500


if __name__ == '__main__':
    app.run()