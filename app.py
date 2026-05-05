from flask import Flask, render_template, request, flash, redirect, url_for
import os

app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY', 'pragya-portfolio-dev-key-2025')

# ── Routes ────────────────────────────────────────────────────────────

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/services')
def services():
    return render_template('services.html')

@app.route('/portfolio')
def portfolio():
    return render_template('portfolio.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name    = request.form.get('name', '').strip()
        email   = request.form.get('email', '').strip()
        subject = request.form.get('subject', '').strip()
        message = request.form.get('message', '').strip()

        if not all([name, email, subject, message]):
            flash('Please fill in all fields.', 'error')
            return redirect(url_for('contact'))

        # Log to terminal (replace with email sending in production)
        print(f"\n{'='*50}")
        print(f"NEW ENQUIRY from {name} <{email}>")
        print(f"Subject : {subject}")
        print(f"Message : {message}")
        print(f"{'='*50}\n")

        flash("Thanks for reaching out, I'll get back to you within 24 hours!", 'success')
        return redirect(url_for('contact'))

    return render_template('contact.html')

# ── Run ───────────────────────────────────────────────────────────────

if __name__ == '__main__':
    app.run(debug=True)
