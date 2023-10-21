from flask import Flask, render_template

@app.route('/')
def home():
    return "<p>Dit is mijn eigen verzonnen tekst.</p>"