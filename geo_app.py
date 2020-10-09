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

# @TODO
"""LEGG INN API FRA BYSYKKEL REALTIME:
1. OPPDATER NÅR MAN TRYKKER PÅ OPPDATER
2. VIS HVOR MANGE SYKLER TILGJENGELIG PER STOPP(TALL)
3. VIS HVOR MANGE SYKLER TOTALT!(FARGE/STØRRELSE)

https://matplotlib.org/3.1.1/tutorials/colors/colormaps.html
https://github.com/jwass/mplleaflet
https://nrkbeta.github.io/2018-08-oslobysykkel/
https://oslobysykkel.no/apne-data/sanntid
https://github.com/NABSA/gbfs/blob/master/gbfs.md
https://www.uio.no/studier/emner/matnat/ifi/IN1000/h18/fredags-python/oppgaver-til-fredagspython/uke-9---api.pdf
"""

@app.route("/map")
def to_map():
    return render_template("map.html")

# @app.route('/graph', methods=['GET', 'POST'])
# def graph():
#     '''This function renders the graph.html or stat.html depending on how many boxes with features
#     have been checked.
#     Arguments:
#         nothing
#     Returns:
#         render_template('graph.html')
#         render_template('stat.html')
#     '''
#     acc = 0
#     if request.method == 'POST':
#         features = request.form.getlist('box')
#         model = request.form.get('model')
#         classifier, acc = fit_it(int(model), features, 'diabetes')
#
#         if len(features) == 2:
#             feature1 = features[0]
#             feature2 = features[1]
#             visualize(classifier, feature1, feature2, 'diabetes', show=False)
#
#             return render_template('graph.html', acc=acc)
#         return render_template('stat.html', acc=acc)
#     return render_template('graph.html', acc=acc)


if __name__ == "__main__":
    app.run(debug=True, port=5001)
