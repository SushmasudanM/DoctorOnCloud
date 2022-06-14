"""
added about.html to Doctor_App_4
"""

# --------------------
# Adding about.html to Doctor_On_Cloud App
# --------------------
import flask
Doctor_App_4 = flask.Flask("Doctor_App_4")
# --------------------

# --------------------
# END POINT - 1 : http://127.0.0.1:5000/ URL MAPPED to '/'
# --------------------
@Doctor_App_4.route('/')
def my_index_page():
    return flask.render_template('index.html')
# --------------------

# --------------------
# END POINT - 2 : http://127.0.0.1:5000/about URL MAPPED to '/about'
# --------------------
@Doctor_App_4.route('/about')
def my_about_page():
    return flask.render_template('about.html')
# --------------------

# --------------------
# Run the server
# --------------------
Doctor_App_4.run()
# --------------------
