from flask import Flask, jsonify, render_template, request
from flask_cors import CORS, cross_origin
import json
import sys
import csv
import time

sys.path.append("../../")
from Code.prediction_scripts.item_based import recommendForNewUser
from search import Search

app = Flask(__name__)
app.secret_key = "secret key"

cors = CORS(app, resources={r"/*": {"origins": "*"}})


@app.route("/")
def landing_page():
    return render_template("landing_page1.html")


@app.route("/attempt2")
def landing_page2():
    return render_template("landing_page2.html")


@app.route("/attempt3")
def landing_page3():
    return render_template("landing_page3.html")


@app.route("/attempt4")
def landing_page4():
    return render_template("landing_page4.html")


@app.route("/attempt5")
def landing_page5():
    return render_template("landing_page5.html")


@app.route("/attempt6")
def landing_page6():
    return render_template("landing_page6.html")


@app.route("/predict", methods=["POST"])
def predict():
    data = json.loads(request.data)  # contains movies
    data1 = data["movie_list"]
    training_data = []
    for movie in data1:
        movie_with_rating = {"title": movie, "rating": 5.0}
        training_data.append(movie_with_rating)
    recommendations = recommendForNewUser(training_data)
    recommendations = recommendations[:10]
    resp = {"recommendations": recommendations}
    return resp


@app.route("/random", methods=["POST"])
def random():
    search = Search()
    recommendations = search.random()
    resp = {"recommendations": recommendations}
    return resp


@app.route("/search", methods=["POST"])
def search():
    term = request.form["q"]
    print("term: ", term)

    search = Search()
    filtered_dict = search.resultsTop10(term)

    resp = jsonify(filtered_dict)
    resp.status_code = 200
    return resp


@app.route("/feedback1", methods=["POST"])
def feedbackFromTrue1():
    data = json.loads(request.data)
    with open("experiment_results/feedback_T_1.csv", "w") as f:
        for key in data.keys():
            f.write('"%s", %s\n' % (key, data[key]))
    # print(data)
    return data


@app.route("/feedback2", methods=["POST"])
def feedbackFromRandom1():
    data = json.loads(request.data)
    with open("experiment_results/feedback_R_1.csv", "w") as f:
        for key in data.keys():
            f.write('"%s", %s\n' % (key, data[key]))
    # print(data)
    return data


@app.route("/feedback3", methods=["POST"])
def feedbackFromTrue2():
    data = json.loads(request.data)
    with open("experiment_results/feedback_T_2.csv", "w") as f:
        for key in data.keys():
            f.write('"%s", %s\n' % (key, data[key]))
    # print(data)
    return data


@app.route("/feedback4", methods=["POST"])
def feedbackFromTrue3():
    data = json.loads(request.data)
    with open("experiment_results/feedback_T_3.csv", "w") as f:
        for key in data.keys():
            f.write('"%s", %s\n' % (key, data[key]))
    # print(data)
    return data


@app.route("/feedback5", methods=["POST"])
def feedbackFromRandom2():
    data = json.loads(request.data)
    with open("experiment_results/feedback_R_2.csv", "w") as f:
        for key in data.keys():
            f.write('"%s", %s\n' % (key, data[key]))
    # print(data)
    return data


@app.route("/feedback6", methods=["POST"])
def feedbackFromRandom3():
    data = json.loads(request.data)
    with open("experiment_results/feedback_R_3.csv", "w") as f:
        for key in data.keys():
            f.write('"%s", %s\n' % (key, data[key]))
    # print(data)
    return data


@app.route("/success")
def success():
    return render_template("success.html")


if __name__ == "__main__":
    app.run(port=5000, debug=True)
