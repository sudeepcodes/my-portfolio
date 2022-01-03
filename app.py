import csv
import os
from flask import Flask, render_template, request, redirect, url_for, send_file

app = Flask(__name__)


@app.route('/')
def home_page():
    return render_template('index.html')


@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)


@app.route('/download/resume')
def get_resume():
    resume_file = './static/Resume.pdf'
    try:
        return send_file(resume_file, as_attachment=True)
    except Exception as e:
        print(e)
        return e


def write_to_csv(filename, data):
    email = data['email']
    subject = data['subject']
    message = data['message']
    if os.path.isfile(filename):
        with open(filename, 'a') as file:
            csv_writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            csv_writer.writerow([email, subject, message])
    else:
        with open(filename, 'a') as file:
            csv_writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            csv_writer.writerow(['EMAIL', 'SUBJECT', 'MESSAGE'])
            csv_writer.writerow([email, subject, message])


@app.route('/submit-form', methods=['POST', 'GET'])
def submit_form():
    try:
        if request.method == 'POST':
            data = request.form.to_dict()
            write_to_csv('database.csv', data)
            return redirect('thankyou.html')
        else:
            return 'Try Again'
    except Exception as e:
        print(e)


if __name__ == '__main__':
    app.run(port=5000, debug=True)
