from flask import *
from flask_bootstrap import Bootstrap

import pandas as pd

from api.recomendations import Recomendations

app = Flask(__name__)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True
bootstrap = Bootstrap(app)

@app.route('/', methods=['GET'])
def home():
   return render_template('form.html')

@app.route("/ui/stocks/recomendations", methods=['POST'])
def recomendations_html_table():
    if request.method == 'POST':
      #print(request.form) #ImmutableMultiDict([('ticker', '')])

      rec = Recomendations()
      df = rec.get(output="dataframe")

      return render_template("table.html", tables=[df.to_html(classes='data')], titles=df.columns.values)

@app.route('/stocks/recomendations', methods=['GET', 'POST'])
def get_recomendations():
    data = request.get_json()

    if data:
        rec = Recomendations()

        if data['output_format'] == "json" and data['indicator'] == "macdh":
            output_format = data['output_format']
            recomendations = rec.get(output=output_format)
            return recomendations, 200

    return jsonify(error_message="Informe os parametros output_format e indicator")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)