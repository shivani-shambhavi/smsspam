from flask import Flask, render_template, request
import pickle

app = Flask(__name__)

# Load the trained model
with open('Naive_model.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/result', methods=['POST'])
def result():
    email = request.form.get('email', '')
    prediction = model.predict([email])[0]
    return render_template('result.html', email=email, prediction=prediction)

if __name__ == '__main__':
    app.run(debug=True)
