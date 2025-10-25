from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World from Shivani Sogal! I am adding my first code change.'

@app.route('/hello')
def hello():
    return render_template('hello.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/about-css')
def about_css():
    return render_template('about-css.html')

@app.route('/greetings')
def greetings():
    return render_template('greetings.html')


@app.route('/favorite-course')
def favorite_course():
    subject = request.args.get('subject')
    course_number = request.args.get('course_number')
    return render_template('favorite-course.html', subject=subject, course_number=course_number)

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        firstName = request.form.get('firstName')
        lastName = request.form.get('lastName')
        email = request.form.get('email')
        message = request.form.get('message')
        return render_template('contact.html', form_submitted=True, firstName=firstName, lastName=lastName, email=email, message=message)
    return render_template('contact.html', form_submitted=False)


if __name__ == '__main__':
    app.run()
