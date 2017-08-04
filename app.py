import json
import flask
import conf

from trip.views import leyouv_trips


app = flask.Flask('api')

#trip
prefix = "/api/v1"
app.register_blueprint(leyouv_trips,url_prefix=prefix)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)