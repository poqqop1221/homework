from flask import Flask, render_template,request,redirect,url_for
from pytube import YouTube


app=Flask(__name__)

@app.route('/')
def index():
	filename = request.args.get('filename')
	

	filename2 =request.args.get('filename2')
	return render_template('index.html',filename=filename,filename2=filename2)
	
	


@app.route('/submit',methods=['POST'])
def post_submit():
    yt=YouTube()
    
    url=request.form.get('url')
    
    yt.url=url
    
    viedo=yt.get('mp4','360p')
    
    viedo.download('./')
    
    filename=yt.filename
    
    print(yt)
    print(yt.filename)
    
    
    

    yt2=YouTube()
    url2=request.form.get('url2')
    yt2.url=url2
    viedo2=yt2.get('mp4','720p')
    viedo2.download('./')
    filename2=yt2.filename
    print(yt2)
    print(yt2.filename)
    return redirect(url_for('index',filename=filename,filename2=filename2))

if __name__=="__main__":
	app.run(debug = True)