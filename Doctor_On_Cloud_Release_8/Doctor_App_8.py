"""
Create ENDPOINT for newuser and return registration.html
"""
# --------------------
# Create App for Doctor_On_Cloud App
# --------------------
import flask
Doctor_App_8 = flask.Flask("Doctor_App_8")
# --------------------

# --------------------
# END POINT - 1 : http://127.0.0.1:5000/ URL MAPPED to '/'
# --------------------
@Doctor_App_8.route('/')
def my_index_page():
    return flask.render_template('index.html')
# --------------------

# --------------------
# END POINT - 2 : http://127.0.0.1:5000/about URL MAPPED to '/about'
# --------------------
@Doctor_App_8.route('/about')
def my_about_page():
    return flask.render_template('about.html')
# --------------------

# --------------------
# END POINT - 3 : http://127.0.0.1:5000/login URL MAPPED to '/login'
# --------------------
@Doctor_App_8.route('/login')
def my_login_page():
    return flask.render_template('login.html')
# --------------------

# --------------------
# END POINT - 4 : http://127.0.0.1:5000/validate URL MAPPED to '/validate'
# --------------------
@Doctor_App_8.route('/validate', methods=['POST'])
def my_validate_page():
    # Task - 1 : Get user name & pass word entered by user
    # ----------------
    # framework will keep all the form data entered by use in a dictionary.
    # dictionary is 'flask.request.form'. from this dictionary we can retrieve username & password
    # key will be 'uname' and 'pw'
    entered_username = flask.request.form.get('uname')
    entered_password = flask.request.form.get('pw')
    if ((entered_username == 'abc') and (entered_password == 'xyz')):

        return "Login Success"

    else:
        return "Login Failed. Invalid Credentials <br><br> <a href='/login'>Go Back To Login</a>"


# --------------------
# END POINT - 5 : http://127.0.0.1:5000/newuser URL MAPPED to '/newuser'
# --------------------
@Doctor_App_8.route('/newuser')
def my_newuser_page():
    return flask.render_template('newuser.html')
# --------------------


# --------------------
# Run the server
# --------------------
Doctor_App_8.run()
# --------------------
