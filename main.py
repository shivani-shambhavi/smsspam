from flask import Flask, render_template, request
import pickle

app = Flask(__name__)

pipe = pickle.load(open("Naive_model1.pkl", "rb"))

@app.route('/', methods=["GET", "POST"])
def main_function():
    if request.method == "POST":
        text = request.form
        emails = text['email']

        list_email = [emails]
        output = pipe.predict(list_email)[0]

        return output

    else:
        return render_template("index.html")

if __name__ == '__main__':
    app.run(debug=True)
