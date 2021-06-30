import os
import glob
from flask import Flask, request, redirect
from werkzeug.utils import secure_filename
from datetime import datetime



def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in file_exten


app = Flask(__name__)
@app.route('/upload', methods = ['POST'])


def upload_file():
    if request.method == 'POST':
        uploaded_file = request.files['file']
        
        # --> Making Directory
        if not os.path.exists('images'):
            os.makedirs('images')

        if uploaded_file.filename != '':
            #Adding Secure Name File 
            secure_name = secure_filename(uploaded_file.filename)
            file_name, file_exten = os.path.splitext(uploaded_file.filename) #File Extension Split
            if file_exten == '.jpg':
                #Saving File
                date = datetime.now().strftime("%Y_%m_%d_%I_%M_%S_%p")
                final_name = secure_name + date
                uploaded_file.save('images/' + final_name + '.jpg')
                return 'File Save'
        #             return redirect(url_for('index'))
        #             print("File Uploaded!")
            else:
                return "Just JPG file accpeted!"

        elif uploaded_file.filename == '':
            return 'File not uploaded'

@app.route('/images', methods = ['GET'])

def fetch_data():
    if request.method == 'GET':
        if os.path.exists('images'):
            images_list = os.listdir("images")
            # return images_list
            for all_images in images_list:
                return all_images



# if __name__ == '__main__':
app.run()


