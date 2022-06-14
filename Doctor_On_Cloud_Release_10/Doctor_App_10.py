"""
we are validating username and password with registered users
in database
"""

# --------------------
# Create App  for Doctor_On_Cloud App
# --------------------
import flask
Doctor_App_10 = flask.Flask("Doctor_App_10")
# --------------------

# --------------------
# END POINT - 1 : http://127.0.0.1:5000/ URL MAPPED to '/'
# --------------------
@Doctor_App_10.route('/')
def my_index_page():
    return flask.render_template('index.html')
# --------------------

# --------------------
# END POINT - 2 : http://127.0.0.1:5000/about URL MAPPED to '/about'
# --------------------
@Doctor_App_10.route('/about')
def my_about_page():
    return flask.render_template('about.html')
# --------------------

# --------------------
# END POINT - 3 : http://127.0.0.1:5000/login URL MAPPED to '/login'
# --------------------
@Doctor_App_10.route('/login')
def my_login_page():
    return flask.render_template('login.html')
# --------------------

# --------------------
# END POINT - 4 : http://127.0.0.1:5000/validate URL MAPPED to '/validate'
# --------------------
@Doctor_App_10.route('/validate', methods=['POST'])
def my_validate_page():

    entered_username = flask.request.form.get('uname')
    entered_password = flask.request.form.get('password')
    entered_username = entered_username.lower()
    entered_username = entered_username.strip()

    import sqlite3

    print("Create/Connect to database 'users_db.sqlite' ")
    my_db_connection = sqlite3.connect(f'users_db.sqlite')
    print("Done")

    print("Get cursor object, which help us to execute SQL query on database ")
    my_db_cursor = my_db_connection.cursor()
    print("Done")

    print("Executing select query")
    my_db_cursor.execute(
        f"SELECT NAME,PASSWORD FROM USERS_TABLE WHERE NAME ='{entered_username}' AND PASSWORD = '{entered_password}'")
    print("Done")

    print("Retrieve all data from cursor")
    my_db_result = my_db_cursor.fetchall()
    print("Done")

    my_db_connection.close()

    if len(my_db_result) > 0:

         return "<a href='loginsuccess.html'></a> <center><h2>Login Success<br></h2><a href='/'>Home</a></center>"
    else:
        return "<a href='loginfailed.html'></a> <center><h2>Login Failed. Invalid Credentials.<br></h2><a href='/login'>Login</a></center>"



# --------------------
# END POINT - 5 : http://127.0.0.1:5000/newuser URL MAPPED to '/newuser'
# --------------------
@Doctor_App_10.route('/newuser')
def my_newuser_page():
    return flask.render_template('newuser.html')
# --------------------

# --------------------
# END POINT - 6 : http://127.0.0.1:5000/register URL MAPPED to '/register'
# --------------------
@Doctor_App_10.route('/register', methods=['POST'])
def my_register_page():

    # Get all data
    entered_username = flask.request.form.get('uname')
    entered_password_1 = flask.request.form.get('pw1')
    entered_password_2 = flask.request.form.get('pw2')
    entered_email = flask.request.form.get('email')
    entered_username = entered_username.lower()
    entered_username = entered_username.strip()

    # Check whether both the passwords are matching
    if entered_password_1 != entered_password_2:
        return "Both Passwords Are Not Matching. <br><br><a href='/login'>Go Back To Registration</a>"

    # Create Database and table if not present
    import sqlite3

    print("Create/Connect to database 'users_db.sqlite' ")
    my_db_connection = sqlite3.connect('users_db.sqlite')
    print("Done")

    print("Get cursor object, which help us to execute SQL query on database ")
    my_db_cursor = my_db_connection.cursor()
    print("Done")

    print("Create table if not exists")
    my_query = '''CREATE TABLE IF NOT EXISTS users_table(
    NAME    VARCHAR(100),
    PASSWORD    VARCHAR(100),
    EMAIL   VARCHAR(100)
    )
    '''
    my_db_cursor.execute(my_query)
    print("Done")
    # ------------------------

    # verify whether user already exists in the database
    # How? select from table where username = entered_username
    # if we get records then we decide found
    # if we get 0 records the we can decide not found

    my_query = f"SELECT * FROM users_table WHERE name='{entered_username}'"
    my_db_cursor.execute(my_query)
    my_db_result = my_db_cursor.fetchall()
    if len(my_db_result) > 0:
        return "User Already Exists. <br><br><a href='/login'>Go Back To Registration</a>"

    # if user not exists then add new record to database and return account created successfully
    my_query = f"INSERT INTO USERS_TABLE VALUES('{entered_username}', '{entered_password_1}', '{entered_email}')"
    my_db_cursor.execute(my_query)
    my_db_connection.commit()
    my_db_connection.close()
    return "User Created Successfully. <a href='/login'>Click Here To Login</a>"
# --------------------

# --------------------
# Run the server
# --------------------
Doctor_App_10.run()
# --------------------
