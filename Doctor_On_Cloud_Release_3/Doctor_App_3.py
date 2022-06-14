"""
calling index.html to Doctor_App_3
"""

# --------------------
# Creating index page to Doctor_On_Cloud App
# --------------------
import flask
Doctor_App_3 = flask.Flask("Doctor_App_3")
# --------------------

# --------------------
# END POINT - 1 : http://127.0.0.1:5000/ URL MAPPED to '/'
# --------------------
@Doctor_App_3.route('/')
def my_index_page():
    return flask.render_template('index.html')
# --------------------

# --------------------
# Run the server
# --------------------
Doctor_App_3.run()
# --------------------
