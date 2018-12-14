import cherrypy


class HelloWorld(object):
    @cherrypy.expose
    def index(self, length = 0):
        return """<html>
          <head></head>
          <body>
            <form method="get" action="generate">
              <input type="text" value="8" name="length" />
              <button type="submit">Give it now!</button>
            </form>
          </body>
        </html>"""

    @cherrypy.expose
    def generate(self, length = 0):
        return """<html>
                  <head></head>
                  <body>
                    <form method="get" action="index">
                      <input type="text" value="8" name="length" />
                      <button type="submit">Hit me now</button>
                    </form>
                  </body>
                </html>"""


if __name__ == '__main__':
    cherrypy.quickstart(HelloWorld())