import random
from flask import Flask, render_template
from flask_bootstrap import Bootstrap
import json

app = Flask(__name__)
bootstrap = Bootstrap(app)
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

with open('templates/crew.json') as f:
    crew_data = json.load(f)
    crew_members = crew_data['crew_members']


@app.route('/member')
def member():
    random_member = random.choice(crew_members)
    return render_template('member.html', random_member=random_member)


if __name__ == '__main__':
    app.run(debug=True)
