import os
import glob
import time
from flask import Flask, render_template, jsonify, request, url_for, redirect, flash
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.secret_key = "$3m.a.k.a9202nd-22.i_23_eag11.y.!#3$3d"
RECEIVED_DIR = "static/received"


@app.route("/", methods=['GET'])
def home():
    # get all files using glob module
    audio_files = glob.glob("static/audios/*")
    video_files = glob.glob("static/videos/*")
    photo_files = glob.glob("static/photos/*")
    app_files = glob.glob("static/apps/*")
    other_files = glob.glob("static/others/*")
    received_files = glob.glob("static/received/*")

    # rewrite path separator
    # for windows based operating systems
    new_audio_files = [file.replace("\\", "/") for file in audio_files]
    new_video_files = [file.replace("\\", "/") for file in video_files]
    new_photo_files = [file.replace("\\", "/") for file in photo_files]
    new_other_files = [file.replace("\\", "/") for file in other_files]
    new_app_files = [file.replace("\\", "/") for file in app_files]
    new_received_files = [file.replace("\\", "/") for file in received_files]

    return render_template("home.html",
                           photos=new_photo_files,
                           videos=new_video_files,
                           audios=new_audio_files,
                           others=new_other_files,
                           apps=new_app_files,
                           received=new_received_files
                           )


@app.route("/about", methods=['GET'])
def about():
    return render_template('about-us.html')


@app.route("/upload")
def upload():
    return render_template('upload.html')


@app.route("/process_upload", methods=['POST', 'GET'])
def process_upload():
    if request.method == "GET":
        return redirect(url_for("upload"))

    else:
        if request.method == "POST":
            current = time.ctime(time.time())
            try:
                # tru to upoad the file
                # get the value from the form field
                incoming_file = request.files["coming"]

                # check if filename is empty and show error
                if incoming_file.filename == "":
                    flash("invalid choice")
                    return redirect(url_for("upload"))
                # if filename != empty save it
                else:
                    # save file to local machine
                    incoming_file_name = str(incoming_file.filename).strip()
                    # safely convert file name of received file
                    secure_file_name = secure_filename(incoming_file.filename)

                    # join received directory and received filename
                    final_path = os.path.join(RECEIVED_DIR, secure_file_name)
                    # save file
                    incoming_file.save(final_path)

                    upload_message = {
                    "status": "success",
                    "file": incoming_file_name,
                    "time": current
                    }
            except Exception as e:
                # should any other exception occur
                upload_message = {
                    "status": "error",
                    "file": "Something went haywire",
                    "time": current
                    }
        flash(message=upload_message)
        return redirect(url_for("upload"))

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8070)