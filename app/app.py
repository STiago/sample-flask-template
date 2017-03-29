from flask import Flask, Response, render_template
app = Flask(__name__)
app.config['DEBUG'] = True

@app.route('/html')
def htmlfunction():
    return render_template('index.html')

@app.route('/text')
def textfunction():
    resp = Response()
    resp.headers['Content-Type'] = 'text/plain; charset = utf-8'
    resp.set_data("My text is here!")
    return resp

@app.route('/image')
def imgfunction():
    return '<!DOCTYPE html><html lang="es"><head><meta charset="utf-8"><title>Images</title></head><body><img src="static/images/image.jpg" alt="imagen1"/><img src="static/images/logougr.jpg" alt="imagen"/></body></html>'

@app.errorhandler(404)
def page_not_found(error):
    return render_template('error.html'), 404
    #return '<!DOCTYPE html><html lang="es"><head><meta charset="utf-8"><title>ERROR</title></head><body><header>[ERROR 404] - NOT FOUND</header></body></html>'

if __name__ == '__main__':
    app.run(host="localhost",port=9000)
