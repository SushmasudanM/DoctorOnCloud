"""
Added welcome page to Doctor_App_2.py
"""

# --------------------
# Creating welcome page to Doctor_On_Cloud App
# --------------------
import flask
Doctor_App_2 = flask.Flask("Doctor_App_2")
# --------------------

# --------------------
# END POINT - 1 : http://127.0.0.1:5000/ URL MAPPED to '/'
# --------------------
@Doctor_App_2.route('/')
def my_index_page():
    return "<h1> <center> <body bgcolor='cyan'> <u> DOCTOR ON CLOUD </u> </center> </h1>"
# --------------------

# --------------------
# Run the server
# --------------------
Doctor_App_2.run()
# --------------------
