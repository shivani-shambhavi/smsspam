from flask import Flask, render_template, request
import pickle

app = Flask(__name__)

# Load the trained model
with open('Naive_model1.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Get the email input from the form
        email = request.form['email']
        
        # Perform classification using the loaded model
        prediction = model.predict([email])[0]
        
        # Return the classification result
        return render_template('index.html', email=email, prediction=prediction)
    else:
        return render_template('index.html', email='', prediction='')

if __name__ == '__main__':
    app.run(debug=True)
