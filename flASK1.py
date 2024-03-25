from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return "<p>Welcome to my first small project.</p>"

@app.route("/Aboutme")
def aboutme():
    return "<p>My name is Shreyash Chaurasia. I'm currently a 3rd year student at MIT ADTU Pune for Blockchain specialization. I've graduated my high school from Navrachana School, Vadodara in the year 2021. <p>"

@app.route("/interests")
def interests():
    return render_template('index.html')
    
if __name__=="__main__":
    app.run(debug=True, port=8000)
