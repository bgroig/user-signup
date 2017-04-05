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

USER_RE = re.compile(r"^[a-zA-Z0-9_-]{3,20}$")
def valid_username(new_username):
    return new_username and USER_RE.match(new_username)

PASS_RE = re.compile(r"^.{3,20}$")
def valid_password(new_password):
    return new_password and PASS_RE.match(new_password)

EMAIL_RE = re.compile(r"^[\S]+@[\S]+\.[\S]+$")
def valid_email(new_email):
    return new_email or EMAIL_RE.match(new_email)

page_header = """
<!DOCTYPE html>
<html>
<head>
    <title>User-signup</title>
    <style type="text/css">
        .label {
            text-align: right;
        }
        .error {
            color: red;
        }
    </style>
</head>
<body>
    <h1>
        Signup
    </h1>
"""

page_footer = """
</body>
</html>
"""
form = """
    <form method="post">
        <table>
            <tbody>
                <tr>
                    <td>
                        <label for="username">Username</label>
                    </td>
                    <td>
                        <input name="username" type="text" value="{4}">
                        <span class="error">{0}</span>
                    </td>
                </tr>
                <tr>
                    <td>
                        <label for="password">Password</label>
                    </td>
                    <td>
                        <input name="password" type="password" value required>
                        <span class="error">{1}</span>
                    </td>
                </tr>
                <tr>
                    <td>
                        <label for="password">Verify Password</label>
                    </td>
                    <td>
                        <input name="verify" type="password" required />
                        <span class="error">{2}</span>
                    </td>
                </tr>
                <tr>
                    <td>
                        <label for="email">Email (optional)</label>
                    </td>
                    <td>
                        <input name="email" type="email" value="{5}">
                        <span class="error">{3}</span>
                    </td>
                </tr>
            </tbody>
        </table>
        <input type="submit"/>
    </form>
        """


class MainHandler(webapp2.RequestHandler):

    def get(self):

        content = page_header + form.format("","","","","","") + page_footer

        self.response.write(content)

    def post(self):

        username = self.request.get("username")
        password = self.request.get("password")
        verify = self.request.get("verify")
        email = self.request.get("email")


        error1 = ""
        error2 = ""
        error3 = ""
        error4 = ""

        if not valid_username(username):
            error1 = "That's not valid username."

        if not valid_password(password):
            error2 = "That's not a valid password."

        if password != verify:
            error3 = "Passwords don't match."

        if email:
            if "@" and "." not in email:
                error4 = "That's not a valid email address."


        if error1 or error2 or error3 or error4:
            content = page_header + form.format(error1, error2, error3, error4, username, email) + page_footer

        else:
            content = "<h1>Welcome, " + username + "!</h1>"

        username = cgi.escape(username, quote=True)

        self.response.write(content)



        #if len(username) < 3 or ' ' in username:
        #    self.redirect("/?error1= That's not a valid username.")

        # if len(password) < 3:
        #     self.redirect("/?error2= That's not a valid password.")
        #
        # if verify != password:
        #     self.redirect("/?error3= Passwords don't match.")
        #
        # if email:
        #     if "@" and "." not in email:
        #         self.redirect("/?error4= That's not a valid email address.")







app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
