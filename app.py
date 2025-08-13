from flask import Flask, render_template, request, redirect, url_for, flash
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key'

class FlagForm(FlaskForm):
    flag = StringField('Flag', validators=[DataRequired()])
    submit = SubmitField('Submit')

# Dummy challenge data
challenges = [
    {"title": "Warmup", "description": "Submit the flag format: CTF{...}"},
    {"title": "Crypto", "description": "Decrypt the message to find the flag."}
]

@app.route('/', methods=['GET', 'POST'])
def challenges_view():
    form = FlagForm()
    if form.validate_on_submit():
        flag = form.flag.data
        # Here you would check the flag
        flash('Flag submitted: ' + flag)
        return redirect(url_for('challenges_view'))
    return render_template('challenges.html', challenges=challenges, form=form)

if __name__ == '__main__':
    app.run(debug=True)