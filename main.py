#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
import cgi
import re

page_header = """
<!DOCTYPE html>
<html>
<head>
    <title>User Signup</title>
    <style type="text/css">
        .error {
            color: red;
        }
    </style>
</head>
<body>
    <h1>
    User Signup
    </h1>
"""
page_footer = """
</body>
</html>
"""



form  = """
<form method="post">
    <label>
        Username
        <input type="text" name="username" value="%(username)s"/>
    </label>
    <div style="color: red">%(error1)s</div>

    <label>
        Password
        <input type="password" name="password" value=""/>
    </label>
    <div style="color: red">%(error2)s</div>

    <label>
        Verify Password
        <input type="password" name="match" value=""/>
    </label>
    <div style="color: red">%(error3)s</div>

    <label>
        Email (Optional)
        <input type="text" name="email" value="%(email)s"/>
    </label>
    <div style="color: red">%(error4)s</div>

    <input type="submit" value="Submit"/>
</form>
"""

content = page_header + form + page_footer

def escape_html(s):
    return cgi.escape(s, quote = True)

USER_RE = re.compile(r"^[a-zA-Z0-9_-]{3,20}$")
def valid_username(username):
    return USER_RE.match(username)

def password_match(match, password):
    return match == password

PASSWORD_RE = re.compile(r"^[a-zA-Z0-9_-]{3,20}$")
def valid_password(password):
    return PASSWORD_RE.match(password)


EMAIL_RE = re.compile(r"^[\S]+@[\S]+.[\S]+$")
def valid_email(email):
    if email:
        return EMAIL_RE.match(email)
    else:
        return True





class MainHandler(webapp2.RequestHandler):

    def build(self, username="", error1="", error2="", email="", error3="", error4=""):

        self.response.out.write(content % {"username": username, "error1": error1, "error2": error2, "email": email, "error3": error3, "error4": error4})


    def get(self):
        self.build()


    def post(self):
        input_error = False
        user_name = self.request.get("username")
        user_password = self.request.get("password")
        user_verified_password = self.request.get("match")
        user_email = self.request.get("email")


        username = valid_username(user_name)
        password = valid_password(user_password)
        email = valid_email(user_email)
        match = password_match(user_password, user_verified_password)

        if username and password and email and match:
            self.redirect("/welcome?username=" + user_name)

        else:

            if not username:
                error1 = "Invalid Entry. No spaces and must be 3-20 characters."
            else:
                error1 = ""


            if not password:
                error2 = "Invalid Entry. Must be 3-20 characters."
            else:
                error2 = ""


            if not match:
                error3 = "Invalid Entry. Passwords do not match."
            else:
                error3 = ""


            if not email:
                error4 = "Invalid Entry. Not a valid email address."
            else:
                error4 = ""

            self.build(user_name, error1, error2, user_email, error3, error4)

class Welcome(webapp2.RequestHandler):

    def get(self):

        username = self.request.get('username')

        if valid_username(username):
            welcome_message = "<h1>" + "Welcome " + "<strong>" + username + "</strong>" + "!" + "</h1>"
            self.response.write(welcome_message)

        else:
            self.redirect('/')


app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/welcome', Welcome)

], debug=True)
