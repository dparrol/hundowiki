"""An ultra-minimalist, rather crappy wiki in less than a hundred lines of code. Public domain."""

from flask import Flask, abort, request, redirect, url_for
import os, cgi, re
app = Flask(__name__)

### Routes ###

@app.route('/')
@app.route('/<name>')
def page(name='MainPage'):
    """Show a page: load the thing, and convert to HTML."""
    verifyNameOrAbort(name, status=404)
    try:
        # Read page, escape special characters, and add HTML paragraph markers.
        html = cgi.escape(open(pathFor(name)).read()).replace('\n\n', '\n\n<p>')
        # Convert WikiWords to page links.
        html = re.sub(r'\b((?:[A-Z][a-z0-9]*){2,})\b', r'<a href="/\1">\1</a>', html)
    except IOError:
        html = 'The page %s does not exist. You can totally create it, though!' % name
    return '<html><head><title>%s</title></head>\n<body><header><a href="/edit/%s">Edit</a><hr><p></header>\n<article>\n%s\n</article></body>' % (name, name, html)

@app.route('/edit/<name>', methods=['GET'])
def edit(name):
    """Show the edit box for a page."""
    verifyNameOrAbort(name)
    try:
        text = open(pathFor(name)).read()
    except IOError:
        text = ''
    return '<form method=post>\n<textarea rows=30 cols=120 name=text>%s</textarea><br>\n<input type=submit value="Save">\n</form>' % cgi.escape(text)

@app.route('/edit/<name>', methods=['POST', 'PUT'])
def save(name):
    """Save a page's new contents. This is invoked when someone presses Save on the edit page."""
    verifyNameOrAbort(name)
    text = request.form['text'].strip() or abort(400)
    open(pathFor(name), 'w').write(text)
    return redirect(url_for('page', name=name))

### Utility stuff ###

def pathFor(name):
    """Return the path for the text file containing the contents of a page with a given name."""
    return os.path.join(os.path.dirname(__file__), 'pages', name)

def verifyNameOrAbort(name, status=400):
    """Try to verify a WikiWord's validity, or abort with a given HTTP status code."""
    if not re.match(r'^(?:[A-Z][a-z0-9]*){2,}$', name):
        abort(status)


if __name__ == '__main__':
    app.run()
