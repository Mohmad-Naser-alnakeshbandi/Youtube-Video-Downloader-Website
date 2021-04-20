from pytube import YouTube
from flask import Flask, render_template, request
app = Flask(__name__)
@app.route('/', methods=['POST',"GET"])
def Loading():
        if request.method == 'POST':
                name = request.form.get('name')
                yt = YouTube(name)
                ys = yt.streams.get_highest_resolution()
                ys.download()
        return render_template('index.html')
if __name__=="__main__":
    app.run(debug=True)