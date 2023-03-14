"""
Flask Documentation:     https://flask.palletsprojects.com/
Jinja2 Documentation:    https://jinja.palletsprojects.com/
Werkzeug Documentation:  https://werkzeug.palletsprojects.com/
This file contains the routes for your application.
"""

import os
from app import app
from flask import flash, render_template, request, redirect, send_from_directory, session, url_for
from app.forms import PropertyForm
from app.models import Property, db
from werkzeug.utils import secure_filename
from flask_sqlalchemy import SQLAlchemy



###
# Routing for your application.
###

@app.route('/')
def home():
    """Render website's home page."""
    return render_template('home.html')


@app.route('/about/')
def about():
    """Render the website's about page."""
    return render_template('about.html', name="Mary Jane")

@app.route('/properties/create/', methods=['POST', 'GET'])
def create_property(): #Display the form to add a new property
    form = PropertyForm()

    if request.method == 'POST' and form.validate_on_submit():
        #Create a property instance using the form data
        new_property = Property(
            title = form.title.data,
            bedroom_number = form.bedroom_number.data,
            location = form.location.data,
            price = form.price.data,
            type = form.type.data, 
            description = form.description.data,
            photo = secure_filename(form.photo.data.filename)
        )

        #Add new property to database and commit change
        db.session.add(new_property)
        db.session.commit()

        #Save the upload photo to the uploads folder
        photo = form.photo.data
        filename = photo.filename
        photo.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))


        flash("Listing Created!")
        #print(session.get('_flashes', []))
        return redirect(url_for('view_properties'))
    else:
        flash_errors(form)

    return render_template('create.html', form=form)

@app.route('/properties')
def view_properties(): #Display a list of all properties in the databse
    all_properties = Property.query.all()
    return render_template('properties.html', all_properties=all_properties)

@app.route('/properties/<propertyid>')
def view_property(propertyid): #View individual property using property id.
    data = Property.query.filter_by(id=propertyid).first()
    return render_template('property.html', data=data)

@app.route('/uploads/<filename>')
def getimage(filename):
    return send_from_directory(os.path.join(os.getcwd(),app.config['UPLOAD_FOLDER']), filename)

def get_upload_images():
    filename=[]
    rootdir = os.getcwd()
    print (rootdir)
    for subdir, dirs, files in os.walk(rootdir + '/uploads'):
        for file in files:
            filename+=[file]
            print (os.path.join(subdir, file))
    return filename


###
# The functions below should be applicable to all Flask apps.
###

# Display Flask WTF errors as Flash messages
def flash_errors(form):
    for field, errors in form.errors.items():
        for error in errors:
            flash(u"Error in the %s field - %s" % (
                getattr(form, field).label.text,
                error
            ), 'danger')

@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also tell the browser not to cache the rendered page. If we wanted
    to we could change max-age to 600 seconds which would be 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404
