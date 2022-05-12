from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/afiliate')
def afiliate():
    return render_template('afiliate.html')

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

if(__name__ == '__main__'):
    app.run(port = 3000, debug = True)
