from flask import Flask

app=Flask(__name__)

if __name__ == '__main__':
    app.run(port=5000,debug=True)

@app.route('/')
def home():
    return "<p>Dit is mijn eigen verzonnen tekst.</p>"