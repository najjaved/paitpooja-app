from flask import render_template
from app import app


''' A decorator modifies the function that follows it. The @app.route decorator creates an association between the URL given as an argument and the function. 
In this example there are two decorators, which associate the URLs / and /index to this function. This means that when a web browser requests either of these two URLs, Flask is going to invoke this function and pass the return value of it back to the browser as a response
'''

@app.route('/')
@app.route('/index')
def index():
    user = {'username' : 'Najma'}
    posts = [
        {
            'author': {'username': 'Karsten'},
            'body': 'Try out my new recipe for potato salad !'
        },
        {
            'author': {'username':'Najma'},
            'body': 'Adding chili improves every dish !'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)
