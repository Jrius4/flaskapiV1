from flask import (
    render_template
)
import connexion
#application instance
app = connexion.App(__name__,specification_dir='./')

app.add_api('swagger.yml')


#create a url route
@app.route('/')
def home():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(host='127.0.0.1',port= 5000,debug=True)
