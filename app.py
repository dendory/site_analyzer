from flask import Flask, render_template, request
import connix

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
	return render_template('index.html')

@app.route('/api/analyze', methods=['POST'])
	site = request.form['site']
#        response = requests.post('https://example.com/api', data={'user_input': user_input})
#        if response.status_code == 200:
#            return 'Success!'
#        else:
#            return 'Error'

if __name__ == '__main__':
	app.run(ssl_context='adhoc')
