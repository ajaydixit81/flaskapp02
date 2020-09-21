from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home():
    #return "Hey there!"
    return render_template('home.html')

@app.route('/about/')
def about():
    #return "Hey there!"
    return render_template('about.html')

@app.route('/contact/')
def contact():
    #return "Hey there! please contact me on +91-9270695475"
    return render_template('contact.html')


if __name__ == '__main__':
    #app.run(debug=True)
    app.run()