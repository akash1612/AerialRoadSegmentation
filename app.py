from flask import Flask,render_template,request,redirect,url_for
import subprocess,os
app=Flask(__name__)

@app.route('/', methods = ['GET','POST'])
def index():
    if request.method=='POST':
        image = request.files['image']
        image.save(os.path.join('data/test_set_images/test_1/', 'test_1.png'))
        subprocess.run(["python", "run.py"])
        return "Successful"
    else:
        return render_template('index.html')
    