'''
Shannon Lau
SoftDev1 pd7
HW13 -- A RESTful Journey Skyward
2017-11-10
'''

from flask import Flask, render_template
import urllib2, json

app = Flask(__name__)

#assign following fxn to run when root route requested
@app.route("/")
def hello_world():
    source = "https://api.nasa.gov/planetary/apod?api_key=fIL3dEQ6aMLbaWIaeDpwT43wQjryP1zNUJCio2SZ"
    data = urllib2.urlopen(source)
    print "\n\nURL:"
    print data.geturl()
    print "\n\nHEADER INFO:"
    print data.info()
    print "\n\nSOURCE CODE:"
    # access API data
    data_string = data.read()
    print data_string
    # convert data into a dict
    d = json.loads(data_string)
    img = d["url"]
    caption = d["explanation"]
    return render_template('base.html', img = img, caption = caption)


if __name__ == "__main__":
    app.debug = True
    app.run()
