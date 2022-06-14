"""
added login.html to Doctor_App_5
"""

# --------------------
# Adding login.html to Doctor_On_Cloud App
# --------------------
import flask
Doctor_App_5 = flask.Flask("Doctor_App_5")
# --------------------

# --------------------
# END POINT - 1 : http://127.0.0.1:5000/ URL MAPPED to '/'
# --------------------
@Doctor_App_5.route('/')
def my_index_page():
    return flask.render_template('index.html')
# --------------------

# --------------------
# END POINT - 2 : http://127.0.0.1:5000/about URL MAPPED to '/about'
# --------------------
@Doctor_App_5.route('/about')
def my_about_page():
    return flask.render_template('about.html')
# --------------------

# --------------------
# END POINT - 3 : http://127.0.0.1:5000/login URL MAPPED to '/login'
# --------------------
@Doctor_App_5.route('/login')
def my_login_page():
    return flask.render_template('login.html')
# --------------------

# --------------------
# Run the server
# --------------------
Doctor_App_5.run()
# --------------------
