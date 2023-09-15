from flask import Flask

app = Flask(__name__)

@app.route('/',methods=['GET','POST'])
def index():
    return 'CI/CD pipeline with Heroku and Github has been setup successfully! This is a simple housing price predictor app'

if __name__ == '__main__':
    app.run(debug=True)