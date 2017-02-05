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
    <h1>User Signup
    </h1>
"""
page_footer = """
</body>
</html>
"""

#def build(self, username = "", password = "", verified_password = "", email = "", error = ""):
    #Set of strings containing all the parts of the page
    #String will optionally add components that are passed in

form_header = """
<form action="/Welcome" method="post">"""


add_username = """
    <label>
        Username
        <input type="text" name="username" required>%(username)s</input>
        <span class="error">%(error)s</span>
    </label>
"""


add_password = """
    <label>
        Password
        <input type="text" name="password" required>%(password)s</input>
    <span class="error">%(error)s</span>
    </label>
"""



add_verified_password = """
    <label>
        Password
        <input type="text" name="verified_password" required>%(verified_password)s</input>
        <span class="error">%(error)s</span>
    </label>
"""


add_email = """
    <label>
        Email (Optional)
        <input type="text" name="email">%(email)s</input>
        <span class="error">%(error)s</span>
    </label>
"""

form_footer = """
    <input type="submit" value"></input>
    """

    #content = page_header + form_header + add_username + add_password + add_verified_password + add_email + form_footer + page_footer
    #return content

    #self.response.out.write(content %{"username": cgi.escape(username), "password": cgi.escape(password), "verified_password": cgi.escape(verified_password), "email": cgi.escape(email)})
#user_input = {:}



user_RE = re.compile(r"^[a-zA-Z0-9_-]{3,20}$")
def valid_username(username):
    return user_RE.match(username)


def password_match(password):
    if valid_password == True:
        pass


PASSWORD_RE = re.compile(r"^[a-zA-Z0-9_-]{3,20}$")
def valid_password(password):
    return PASSWORD_RE.match(password)


EMAIL_RE = re.compile(r"^[\S]+@[\S]+.[\S]+$")
def valid_email(email):
    return EMAIL_RE.match(email)





class MainHandler(webapp2.RequestHandler):
# sets up input boxes for Username, Password, Verify Password, and Email(Optional)
    def build(self, username = "", password = "", verified_password = "", email = ""):
        content = page_header + form_header + add_username + add_password + add_verified_password + add_email + form_footer + page_footer
        self.response.out.write(content %{"username": cgi.escape(username), "password": cgi.escape(password), "verified_password": cgi.escape(verified_password), "email": cgi.escape(email)})




    def get(self):
        self.build()








class Welcome(webapp2.RequestHandler):



    def post(self):
        # dictionary = {'user' : self.request.get("username"),
        # 'password' : self.request.get("password"),
        # 'verified_password' : self.request.get("verified_password"),
        # 'email' : self.request.get("email")
        # }


        username = self.request.get("username")
        password = self.request.get("password")
        verified_password = self.request.get("verified_password")
        email = self.request.get("email")




        good_username = valid_username(username)
        good_password = valid_password(password)
        good_verified_password = password_match(verified_password)
        good_email = valid_email(email)

        # Two steps:
        # first, is *anything* wrong? If not, send them to the welcome screen.
        if good_username == True:
            pass
        else:
            error = "Invalid Entry. No spaces and must be 3-20 characters."
            self.redirect("/?error=" + cgi.escape(error))

        if good_password == True:
            pass
        else:
            error = "Invalid Entry. Must be 3-20 characters."
            self.redirect("/?error=" + cgi.escape(error))

        if good_verified_password == True:
            pass
        else:
            error = "Invalid Entry. Passwords do not match."
            self.redirect("/?error=" + cgi.escape(error))

        if good_email == True:
            pass
        else:
            error = "Invalid Entry. Not a valid email address."
            self.redirect("/?error=" + cgi.escape(error))

        # if something *is* wrong, check each field in turn, and come up with
        # an error message if that field needs work.

        # Send them the build() form again, this time with error messages.

        welcome_message = str(good_username)
        welcome_message = "<h1>" + "Welcome " + "<strong>" + welcome_message + "</strong>" + "!" + "</h1>"
        self.response.write(welcome_message)


# The user does not enter a username
# The user's username is not valid -- for example, contains a space character. Full spec is included in the notes underneath the video.
# The user's password and password-confirmation do not match
# The user provides an email, but it's not a valid email.

## WHERE IS MY BUG?
## HOW DO I USE THE DICTIONARY FOR FUNCTIONS?
## HAVE MY CREDENTIALS GONE THROUGH USING THE SUCCESS CLASS?
## HOW DO I USE ERROR MESSAGES CORRECTLY?



class Success(webapp2.RequestHandler):
    def success_input(self):
        final_username = self.request.get(good_username)
        final_password = self.request.get(good_password)
        final_email = self.request.get(good_email)
        self.redirect('/success?final_username=' + email + '&final_password=' + product)


app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/Welcome', Welcome),
    ('/Success', Success)

], debug=True)
