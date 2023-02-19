from flask import Flask, render_template, request, send_file
from pytube import YouTube

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def download():
    # get the YouTube video URL from the form
    url = request.form['url']

    # create a YouTube object
    yt = YouTube(url)

    # get the highest resolution stream
    stream = yt.streams.get_highest_resolution()

    # download the video to a temporary file
    temp_file = stream.download()

    # send the file to the user for download
    return send_file(temp_file, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
