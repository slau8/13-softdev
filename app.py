'''
Shannon Lau
SoftDev1 pd7
HW13 -- A RESTful Journey Skyward
2017-11-10
'''

from flask import Flask, render_template, request, Markup
import urllib2, json
import random

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/job" , methods=['GET','POST'])
def job():
    source = "https://jobs.github.com/positions.json?location=new+york"
    lang = request.args['lang']
    source += "&description=" + lang
    data = urllib2.urlopen(source)
    # access job listings in a []
    data_string = data.read()
    d = json.loads(data_string)
    # access random job in a {}
    job = random.choice(d)
    return render_template("job.html",
                            lang = lang,
                            title = job["title"],
                            type = job["type"],
                            location = job["location"],
                            company = job["company"],
                            description = Markup(job["description"]),
                            apply = Markup(job["how_to_apply"]))


'''
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
    return render_template('nasa.html', img = img, caption = caption)
'''


if __name__ == "__main__":
    app.debug = True
    app.run()
