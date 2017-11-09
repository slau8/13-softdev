from flask import Flask
import urllib2
app = Flask(__name__)

#assign following fxn to run when root route requested
@app.route("/")
def hello_world():
    urlopen = access_api()
    return render_template("base.html",urlopen = urlopen)

def access_api():
    data = urllib2.urlopen("https://api.nasa.gov/planetary/apod?api_key=fIL3dEQ6aMLbaWIaeDpwT43wQjryP1zNUJCio2SZ")
    return data

if __name__ == "__main__":
    app.debug = True
    app.run()


