'''
Shannon Lau
SoftDev1 pd7
HW13 -- A RESTful Journey Skyward
2017-11-10
'''

from flask import Flask, render_template, request, redirect, flash, Markup
import urllib2, json, random, os

app = Flask(__name__)
app.secret_key = os.urandom(128)

# root route // access and render NASA information
@app.route("/")
def nasa():
    url = "https://api.nasa.gov/planetary/apod?api_key=fIL3dEQ6aMLbaWIaeDpwT43wQjryP1zNUJCio2SZ"
    # access data as a {}
    d = retrieve_data(url)
    return render_template('nasa.html', img = d["url"], caption = d["explanation"])

# render homepage
@app.route("/home")
def home():
    return render_template("home.html")

# find and display random job under specified keyword
@app.route("/job", methods=['GET','POST'])
def job():
    # check if keyword was requested
    if not request.args.get('keyword'):
        return redirect('home')
    # retrieve and format source
    keyword = request.args['keyword']
    qkeyword = keyword.replace(" ","+")
    url = "https://jobs.github.com/positions.json?description=" + qkeyword
    # access job listings as a [] of {}
    l = retrieve_data(url)
    # check if there are no results
    if l == []:
        flash("Nothing found for " + keyword)
        return redirect('home')
    # access random job in a {}
    job = random.choice(l)
    return render_template("job.html",
                            keyword = keyword,
                            title = job["title"],
                            type = job["type"],
                            location = job["location"],
                            company = job["company"],
                            description = Markup(job["description"]),
                            apply = Markup(job["how_to_apply"]))

# opens URL to be read and returns JSON data as a dict/list
def retrieve_data(url):
    data = urllib2.urlopen(url)
    print "\n\nURL: "
    print data.geturl()
    print "\n\nINFO: "
    print data.info()
    d = json.loads(data.read())
    return d

if __name__ == "__main__":
    app.debug = True
    app.run()
