"""
we are retriving the new patients data
"""

# --------------------
# Create App  for Doctor_On_Cloud App
# --------------------
import flask
Doctor_App_14 = flask.Flask("Doctor_App_14")
# --------------------

# --------------------
# END POINT - 1 : http://127.0.0.1:5000/ URL MAPPED to '/'
# --------------------
@Doctor_App_14.route('/')
def my_index_page():
    return flask.render_template('index.html')
# --------------------

# --------------------
# END POINT - 2 : http://127.0.0.1:5000/about URL MAPPED to '/about'
# --------------------
@Doctor_App_14.route('/about')
def my_about_page():
    return flask.render_template('about.html')
# --------------------
@Doctor_App_14.route('/benefits')
def my_benefits_page():
    return flask.render_template('benefits.html')
# --------------------
# END POINT - 3 : http://127.0.0.1:5000/login URL MAPPED to '/login'
# --------------------
@Doctor_App_14.route('/login')
def my_login_page1():
    return flask.render_template('loginsuccess.html')

@Doctor_App_14.route('/login')
def my_login_page2():
    return flask.render_template('loginfailed.html')
# --------------------

# --------------------
# END POINT - 4 : http://127.0.0.1:5000/validate URL MAPPED to '/validate'
# --------------------
@Doctor_App_14.route('/validate', methods=['POST'])
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

    print("Check whether table exist")
    my_db_cursor.execute(f" SELECT name FROM sqlite_master WHERE type='table' AND name='users_table'; ")
    print("Done")

    print("Retrieve all data from cursor")
    my_db_result = my_db_cursor.fetchall()
    print("Done")

    if len(my_db_result) == 0:
        return "<center>First Register to login<br><a href='/newuser'>Back</a></center>"

    print("Executing select query")
    my_db_cursor.execute(
        f"SELECT NAME,PASSWORD FROM USERS_TABLE WHERE NAME ='{entered_username}' AND PASSWORD = '{entered_password}'")
    print("Done")

    print("Retrieve all data from cursor")
    my_db_result = my_db_cursor.fetchall()
    print("Done")

    my_db_connection.close()
    print('my_db_result',my_db_result)
    if len(my_db_result) > 0:
         return "<a href='loginsuccess.html'></a> <center><h2>Login Success<br></h2><a href='/'>Home</a></center>"
    else:
        return "<a href='loginfailed.html'></a> <center><h2>Login Failed. Invalid Credentials.<br></h2><a href='/login'>Login</a></center>"


# --------------------
# END POINT - 5 : http://127.0.0.1:5000/newuser URL MAPPED to '/newuser'
# --------------------
@Doctor_App_14.route('/newuser')
def my_newuser1_page():
    return flask.render_template('userregister.html')

@Doctor_App_14.route('/newuser')
def my_newuser2_page():
    return flask.render_template('userexist.html')

# --------------------

# --------------------
# END POINT - 6 : http://127.0.0.1:5000/register URL MAPPED to '/register'
# --------------------
@Doctor_App_14.route('/register', methods=['POST'])
def my_register_page():

    # Get all data
    entered_username = flask.request.form.get('uname')
    entered_password_1 = flask.request.form.get('password1')
    entered_password_2 = flask.request.form.get('password2')
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
    # if we get 0 records then, we can decide not found

    my_query = f"SELECT * FROM users_table WHERE name='{entered_username}'"
    my_db_cursor.execute(my_query)
    my_db_result = my_db_cursor.fetchall()
    print('my_db_result', my_db_result)
    if len(my_db_result) > 0:
        return "<a href='userexist.html'></a> <center><h2>User Already Exists. <br></h2><a href='newuser'>Go Back To Registration</a></center>"


    # if user not exists then add new record to database and return account created successfully
    my_query = f"INSERT INTO USERS_TABLE VALUES('{entered_username}', '{entered_password_1}', '{entered_email}')"
    my_db_cursor.execute(my_query)
    my_db_connection.commit()
    my_db_connection.close()
    return "<a href='userregister.html'></a><center><h2>User Created Successfully.<br></h2> <a href='/login'>Click Here To Login</a>"

# --------------------
# END POINT - 7 : http://127.0.0.1:5000/Contact URL MAPPED to '/Contact'
# --------------------
@Doctor_App_14.route('/Contact')
def my_contact_page():
    return flask.render_template('Contact.html')

# ---------------
# END POINT - 8 : http://127.0.0.1:5000/newpatient URL MAPPED to '/newpatient'
# --------------
@Doctor_App_14.route('/newpatient')
def my_newpatient_page():
    return flask.render_template('newpatient.html')
# --------------------

# --------------------

@Doctor_App_14.route('/newpatient', methods=['POST'])
def my_patient_page():

    # Get all data
    entered_patient_name = flask.request.form.get('pname')
    entered_patient_contact =flask.request.form.get('pcontact')
    entered_bp =flask.request.form.get('pdtype-1')
    entered_sugar = flask.request.form.get('pdtype-2')
    entered_fever = flask.request.form.get('pdtype-3')
    entered_cold= flask.request.form.get('pdtype-4')
    entered_remarks = flask.request.form.get('premarks')

    # Create Database and table if not present
    import sqlite3

    print("Create/Connect to database 'patient_db.sqlite' ")
    my_db_connection = sqlite3.connect('patient_db.sqlite')
    print("Done")

    print("Get cursor object, which help us to execute SQL query on database ")
    my_db_cursor = my_db_connection.cursor()
    print("Done")

    my_query = '''CREATE TABLE PATIENT_TABLE(
    PATIENTNAME    VARCHAR(100),
    PATIENTID      INTEGER PRIMARY KEY AUTOINCREMENT,
    PATIENTCONTACT VARCHAR(14),
    BP          REAL,
    SUGAR       REAL,
    FEVER       REAL,
    COLD        REAL,
    REMARKS        VARCHAR(100)
    )
    '''
    my_db_cursor.execute(my_query)
    print("Done")

    my_query = f"INSERT INTO PATIENT_TABLE ( PATIENTNAME, PATIENTCONTACT, BP, SUGAR, FEVER, COLD, REMARKS ) VALUES ('{entered_patient_name}', '{entered_patient_contact}', '{entered_bp}', '{entered_sugar}', '{entered_fever}', '{entered_cold}','{entered_remarks}' )"
    my_db_cursor.execute(my_query)
    my_db_connection.commit()
    my_db_connection.close()
    return "<center><h2>Patient Details Created Successfully.<br> <a href='/'>Home</a></h2></center>"

# --------------------
# END POINT - 9 : http://127.0.0.1:5000/patientdetails URL MAPPED to '/patientdetails'
# ---------------------
@Doctor_App_14.route('/patientdetails')
def my_patientdetails_page():
    return flask.render_template('patientdetails.html')

# -----------------
@Doctor_App_14.route('/patientdetails', methods=['GET'])
def my_patient_list_page():

    import sqlite3

    print("Create/Connect to database 'newpatient_db.sqlite' ")
    my_db_connection = sqlite3.connect('newpatient_db.sqlite')
    print("Done")

    print("Get cursor object, which help us to execute SQL query on database ")
    my_db_cursor = my_db_connection.cursor()
    print("Done")

    print("Executing select query")
    my_db_cursor.execute("SELECT * FROM 'PATIENT_TABLE'")
    print("Done")

    print("Retrieve all data from cursor")
    my_db_result = my_db_cursor.fetchall()
    print("Done")

    return flask.render_template('patientdetails.html', my_data=my_db_result)




# -----------------
# Run the server
# --------------------
Doctor_App_14.run()
# --------------------
