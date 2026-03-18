import smtplib
import ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# --- CONFIGURATION ---
# 1. For Google Workspace, use "smtp.gmail.com"
# 2. If you have 2FA enabled (highly recommended), generate an "App Password" 
#    at: https://myaccount.google.com/apppasswords
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587  # TLS port

# TODO: Fill in your credentials and recipient
SENDER_EMAIL = "ai@acantix.com"
SENDER_PASSWORD = "Blackberry@123"  # NOT your regular password if using 2FA
RECIPIENT_EMAIL = "rehanmakrani727@gmail.com"

def send_test_email():
    """Sends a simple test email using SMTP."""
    
    # Create the email message
    message = MIMEMultipart()
    message["From"] = SENDER_EMAIL
    message["To"] = RECIPIENT_EMAIL
    message["Subject"] = "Test Email from Acantix Script"

    body = "This is a test email sent from the test-email.py script to verify SMTP settings."
    message.attach(MIMEText(body, "plain"))

    # Create a secure SSL context
    context = ssl.create_default_context()

    print(f"Attempting to send email from {SENDER_EMAIL} to {RECIPIENT_EMAIL}...")

    try:
        # Connect to the server and send the email
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.set_debuglevel(1)  # Set to 1 to see the full SMTP transaction
            server.starttls(context=context)  # Upgrade the connection to secure
            server.login(SENDER_EMAIL, SENDER_PASSWORD)
            server.send_message(message)
            
        print("\n" + "="*30)
        print(f"✅ Success! Email sent successfully.")
        print("="*30)
        
    except smtplib.SMTPAuthenticationError:
        print("\n" + "!"*30)
        print("❌ Authentication Failed.")
        print("Tip: If you're using Google Workspace, ensure you're using an 'App Password'.")
        print("Regular passwords often fail if 2FA is enabled or 'Less Secure Apps' is disabled.")
        print("!"*30)
    except Exception as e:
        print("\n" + "!"*30)
        print(f"❌ An error occurred: {e}")
        print("!"*30)

if __name__ == "__main__":
    # Check if placeholders are still present
    if "your-email" in SENDER_EMAIL or "your-app-password" in SENDER_PASSWORD:
        print("⚠️ Warning: Please update the SENDER_EMAIL and SENDER_PASSWORD in the script.")
    else:
        send_test_email()
