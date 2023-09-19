from flask import Flask
import sys
from housing.logger import logging
from housing.exception import HousingException

app = Flask(__name__)

@app.route('/',methods=['GET','POST'])
def index():
    try:
        raise Exception("This is a custom test exception")
    except Exception as e:
        housing = HousingException(error_message=e, error_details=sys)
        logging.error(housing.error_message)
        logging.info("Main page is accessed")
    return 'CI/CD pipeline with Heroku and Github has been setup successfully! This is a simple housing price predictor app.' + '\n' + 'Now we will cover entity and piplines'

if __name__ == '__main__':
    app.run(debug=True)