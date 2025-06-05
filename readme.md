📧 Gmail SMTP Email Sender (with HTML Templates)
A simple and secure tool built using Python (Flask) and Bootstrap to send bulk emails via Gmail SMTP, complete with HTML email templates and recipient list support.

🧰 Features
✅ Send emails via Gmail using App Password

✅ Upload HTML template to use as email body

✅ Upload .txt recipient list (one email per line)

✅ Real-time results display after sending

✅ Auto-fill email & encrypted password in browser

✅ Fully responsive & Bootstrap 5.3 styled

✅ Tutorial modal for easy Gmail setup

🖼️ UI Preview

🚀 Getting Started
1. Clone this repository
bash
Copy
Edit
git clone https://github.com/yourusername/email-sender.git
cd email-sender
2. Install dependencies
bash
Copy
Edit
pip install flask
3. Run the app
bash
Copy
Edit
python app.py
📂 HTML Form Uploads
HTML Email Template
Upload a .html file that contains your email content.

Recipient List
Upload a .txt file with one email address per line.

🔒 Security Notes
Password is stored in the browser’s localStorage in encrypted format using CryptoJS.

Encryption key is stored in the frontend (not suitable for public/production).

This tool is meant for personal/local use only.

Make sure to use Gmail App Password, not your normal Gmail password.

💡 Gmail App Password Setup
Go to Google Account Security

Enable 2-Step Verification

Create an App Password under "App passwords"

Select Mail and Windows Computer, then generate

Use the generated 16-character password in this app

📁 File Structure
cpp
Copy
Edit
email-sender/
├── templates/
│   └── index.html
├── uploads/
│   └── (everything you upload goes here)
├── app.py
└── README.md
❤️ Credits
Made with ❤️ by Mr. Syah
©️ {{ current_year }} · All rights reserved

📃 License
This project is licensed under the MIT License – see the LICENSE file for details.