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

page_header = """
<!DOCTYPE html>
<html>
<head>
    <title>User-signup</title>
    <style type="text/css">
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

class MainHandler(webapp2.RequestHandler):

    def get(self):

        form = """
        <form action='/add' method="post">
            <table>
                <tbody>
                    <tr>
                        <td>
                            <label for="username">Username</label>
                        </td>
                        <td>
                            <input name="username" type="text" value required />
                            <span class="error"></span>
                        </td>
                    </tr>
                    <tr>
                        <td>
                            <label for="password">Password</label>
                        </td>
                        <td>
                            <input name="password" type="password" required />
                            <span class="error"></span>
                        </td>
                    </tr>
                    <tr>
                        <td>
                            <label for="password">Verify Password</label>
                        </td>
                        <td>
                            <input name="password" type="password" required />
                            <span class="error"></span>
                        </td>
                    </tr>
                    <tr>
                        <td>
                            <label for="email">Email (optional)</label>
                        </td>
                        <td>
                            <input name="email" type="email" value/>
                            <span class="error"></span>
                        </td>
                    </tr>
                </tbody>
            </table>
            <input type="submit"/>
        </form>
            """

        error = self.request.get("error")

        if error:
            error_esc = cgi.escape(error, quote=True)
            error_element = '<p class="error">' + error_esc + '</p>'
        else:
            error_element = ''

        content = page_header + form + page_footer

        self.response.write(content)

class addUser(webapp2.RequestHandler):
    """Handles request to '/add'
        at www.user-signup.com/add
    """

    def post(self):

        new_username = self.request.get("username")

        if new_username == '':
            self.redirect("/?error= You forgot to put in a username.")

        new_password = self.request.get("password")
        password_verified = ''

        if new_password == password_verified:
            content = "<h1>Welcome, " + new_username + "!</h1>"
            self.response.write(content)

        elif new_password != password_verified:
            error1 = "Passwords don't match.".format(new_password)
            self.redirect("/?error=" + error1)

app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/add', addUser)
], debug=True)
