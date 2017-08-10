import conf
import flask

from trip.views import leyouv_trips
from user.views import leyouv_users


app = flask.Flask('api')

#trip
prefix = "/v1"

app.register_blueprint(leyouv_trips,url_prefix=prefix)
app.register_blueprint(leyouv_users,url_prefix=prefix+"/users")


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3050, debug=True)