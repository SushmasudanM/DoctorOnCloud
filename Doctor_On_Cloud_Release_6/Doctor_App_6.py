"""
Retrieve username & password and return same username & password
"""

# --------------------
# Retrieving the username and password, return same data in Doctor_On_Cloud App
# --------------------
import flask
Doctor_App_6 = flask.Flask("Doctor_App_6")
# --------------------

# --------------------
# END POINT - 1 : http://127.0.0.1:5000/ URL MAPPED to '/'
# --------------------
@Doctor_App_6.route('/')
def my_index_page():
    return flask.render_template('index.html')
# --------------------

# --------------------
# END POINT - 2 : http://127.0.0.1:5000/about URL MAPPED to '/about'
# --------------------
@Doctor_App_6.route('/about')
def my_about_page():
    return flask.render_template('about.html')
# --------------------

# --------------------
# END POINT - 3 : http://127.0.0.1:5000/login URL MAPPED to '/login'
# --------------------
@Doctor_App_6.route('/login')
def my_login_page():
    return flask.render_template('login.html')
# --------------------

# --------------------
# END POINT - 4 : http://127.0.0.1:5000/validate URL MAPPED to '/validate'
# --------------------
@Doctor_App_6.route('/validate', methods=['POST'])
def my_validate_page():
    # Task - 1 : Get user name & pass word entered by user
    # ----------------
    # framework will keep all the form data entered by use in a dictionary.
    # dictionary is 'flask.request.form'. from this dictionary we can retrieve username & password
    # key will be 'uname' and 'pw'
    entered_username = flask.request.form.get('uname')
    entered_password = flask.request.form.get('pw')
    return f"You have entered username is {entered_username} and password is {entered_password}"
    # ----------------
# --------------------

# --------------------
# Run the server
# --------------------
Doctor_App_6.run()
# --------------------
