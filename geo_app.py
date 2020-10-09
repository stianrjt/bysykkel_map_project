from flask import Flask, request
from flask import render_template
from geo import draw_map

app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0


@app.route("/", methods=['GET', 'POST'])
def make_graph():
    from flask import request
    system = request.user_agent.platform
    browser = request.user_agent.browser
    draw_map()

    return render_template('home.html', system=system, browser=browser)


@app.route("/map")
def to_map():
    return render_template("map.html")


if __name__ == "__main__":
    app.run(debug=True, port=5001)
