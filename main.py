from flask import Flask, render_template, redirect, url_for, flash
from flask_bootstrap import Bootstrap5
from morse import MorseCipher
from forms import TextForm
import os

app = Flask(__name__)
app.secret_key = os.environ.get("FLASK_KEY")
bootstrap = Bootstrap5(app)

m_cipher = MorseCipher()

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/<mode>", methods=["GET", "POST"])
def cipher(mode):
    text_form = TextForm()
    if text_form.validate_on_submit():
        user_input = text_form.user_input.data.upper()
        if mode == "encrypt":
            result = m_cipher.text_to_morse(user_input)
        elif mode == "decrypt":
            result = m_cipher.morse_to_text(user_input)
        if not result:
            flash("Input contains Invalid characters. Try again.")
            return redirect(url_for("cipher", mode=mode))
        return render_template("cipher.html", mode=mode, form=text_form, result=result, sent=True)
    return render_template("cipher.html", mode=mode, form=text_form)


if __name__ == "__main__":
    app.run(debug=False)
