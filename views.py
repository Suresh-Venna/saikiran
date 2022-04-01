# from django.shortcuts import render
# from flask import render_template
# from main_app import app
# from main_app.models import Projects

# @app.route('/')
# def home():
#     # projects = Projects.query.all()
#     return render_template('index.html',projects=none)

# @app.route('/description/<int:project_id>',methods = ['POST', 'GET'])
# def description(project_id):
#     project = Projects.query.filter_by(project_id=project_id).first()
#     return render_template('product_description.html',project=project)
