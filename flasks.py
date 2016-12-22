from flask import Flask,render_template
app = Flask(__name__)

@app.route("/")
def main():
	return render_template('home.html')

@app.route("/home")
def home():
	return render_template('home.html')

@app.route("/signin")
def signin():
	return render_template('signin.html')

@app.route("/outputs")
def outputs():
	return render_template('outputs.html')

@app.route("/rules")
def rules():
	return render_template('rules.html')

@app.route("/stream")
def stream():
	return render_template('stream.html')

@app.route("/defrag")
def defrag():
	return render_template('defrag.html')

@app.route("/nfq")
def nfq():
	return render_template("nfq.html")

if __name__ == "__main__":
	app.run()

