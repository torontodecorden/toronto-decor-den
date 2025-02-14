from flask import Flask, render_template, request

app = Flask(__name__)

# Home Route
@app.route('/')
def home():
    return render_template('index.html')

# Gallery Route
@app.route('/gallery')
def gallery():
    return render_template('gallery.html')

# Contact Route
@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']
        return render_template('thank_you.html', name=name)
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)
