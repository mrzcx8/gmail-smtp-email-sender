from flask import Flask, render_template, request
import webbrowser
import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from werkzeug.utils import secure_filename

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route("/", methods=["GET", "POST"])
def index():
    status = []
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]
        subject = request.form["subject"]
        html_file = request.files["html_file"]
        email_list_file = request.files["email_list_file"]

        html_path = os.path.join(UPLOAD_FOLDER, secure_filename(html_file.filename))
        html_file.save(html_path)
        with open(html_path, "r", encoding="utf-8") as f:
            html_content = f.read()

        email_list_path = os.path.join(UPLOAD_FOLDER, secure_filename(email_list_file.filename))
        email_list_file.save(email_list_path)
        with open(email_list_path, "r") as f:
            recipients = [line.strip() for line in f if line.strip()]

        for recipient in recipients:
            try:
                msg = MIMEMultipart("alternative")
                msg["Subject"] = subject
                msg["From"] = email
                msg["To"] = recipient
                msg.attach(MIMEText(html_content, "html"))

                with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
                    server.login(email, password)
                    server.sendmail(email, recipient, msg.as_string())
                status.append(f"✅ Sent to {recipient}")
            except Exception as e:
                status.append(f"❌ Failed to {recipient}: {e}")

    return render_template("index.html", status=status)

if __name__ == "__main__":
    webbrowser.open("http://127.0.0.1:5000")
    app.run()
