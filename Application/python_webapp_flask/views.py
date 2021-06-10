"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import Flask, render_template, request
from python_webapp_flask import app
from python_webapp_flask import azure_nlp
import os

@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""
    return render_template(
        'index.html',
        title='ホーム',
        year=datetime.now().year,
    )


@app.route('/tweet_analysis', methods=['POST'])
def tweet_analysis():
    az = azure_nlp.AzureNlp()
    tweet = request.form['tweet']
    keys = az.find_key([tweet])
    return render_template('tweet_analysis.html',
                            tweet=tweet,
                            tags = keys,
                            year=datetime.now().year,
                            title="Complete")

@app.route('/contact')
def contact():
    """Renders the contact page."""
    return render_template(
        'contact.html',
        title='Contact',
        year=datetime.now().year,
    )

@app.route('/about')
def about():
    """Renders the about page."""
    return render_template(
        'about.html',
        title='About',
        year=datetime.now().year,
    )
