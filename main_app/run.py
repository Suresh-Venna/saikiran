from flask import  render_template, Flask
from main_app import templates
app = Flask(__name__)
@app.route('/')
def home():
    # projects = Projects.query.all()
    return render_template('/index.html')
if __name__=="__main__":
    app.run(debug=True)