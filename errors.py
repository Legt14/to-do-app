from .main import app, render_template

@app.errorhandler(404)
def not_found(error):
    return render_template('error/404.html', error=error)


@app.errorhandler(401)
def not_found(error):
    return render_template('error/401.html')


@app.errorhandler(500)
def not_found(error):
    return render_template('error/500.html', error=error)
