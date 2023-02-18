from flask import Flask, render_template, request
import connix

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
	return render_template('index.html')

@app.route('/api/analyze', methods=['POST'])
	site = request.form['site']
	return "Success."

if __name__ == '__main__':
	app.run(ssl_context='adhoc')
