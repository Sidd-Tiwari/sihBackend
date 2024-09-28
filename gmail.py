# # # # # # # # import imaplib
# # # # # # # # import email
# # # # # # # # from email.header import decode_header
# # # # # # # # from fpdf import FPDF

# # # # # # # # # Function to connect to Gmail and fetch emails from all mailboxes
# # # # # # # # def getGmailMessagesFromAllMailboxes(email_user, email_pass):
# # # # # # # #     # Connect to the Gmail IMAP server
# # # # # # # #     mail = imaplib.IMAP4_SSL("imap.gmail.com")
    
# # # # # # # #     # Login to the account
# # # # # # # #     mail.login(email_user, email_pass)
    
# # # # # # # #     # List all mailboxes
# # # # # # # #     status, mailboxes = mail.list()
    
# # # # # # # #     # List to store email data
# # # # # # # #     emails = []
    
# # # # # # # #     # Iterate through all mailboxes
# # # # # # # #     for mailbox in mailboxes:
# # # # # # # #         # Parse the mailbox name (the mailbox name is the last token in the response)
# # # # # # # #         mailbox_name = mailbox.decode().split(' "/" ')[-1].strip('"')
        
# # # # # # # #         # Select the current mailbox
# # # # # # # #         mail.select(mailbox_name)

# # # # # # # #         # Search for all emails in the current mailbox
# # # # # # # #         status, messages = mail.search(None, "ALL")
        
# # # # # # # #         # Convert the result list into a list of email IDs
# # # # # # # #         email_ids = messages[0].split()

# # # # # # # #         # Fetch and process the last 5 emails from the current mailbox
# # # # # # # #         for email_id in email_ids[-5:]:
# # # # # # # #             # Fetch the email by ID
# # # # # # # #             status, msg_data = mail.fetch(email_id, "(RFC822)")

# # # # # # # #             for response_part in msg_data:
# # # # # # # #                 if isinstance(response_part, tuple):
# # # # # # # #                     msg = email.message_from_bytes(response_part[1])

# # # # # # # #                     # Decode the email subject
# # # # # # # #                     subject, encoding = decode_header(msg["Subject"])[0]
# # # # # # # #                     if isinstance(subject, bytes):
# # # # # # # #                         subject = subject.decode(encoding if encoding else "utf-8")

# # # # # # # #                     # Email sender
# # # # # # # #                     from_ = msg.get("From")

# # # # # # # #                     # Email body
# # # # # # # #                     if msg.is_multipart():
# # # # # # # #                         for part in msg.walk():
# # # # # # # #                             content_type = part.get_content_type()
# # # # # # # #                             content_disposition = str(part.get("Content-Disposition"))
# # # # # # # #                             if "attachment" not in content_disposition:
# # # # # # # #                                 try:
# # # # # # # #                                     body = part.get_payload(decode=True).decode()
# # # # # # # #                                 except:
# # # # # # # #                                     body = "No body found."
# # # # # # # #                     else:
# # # # # # # #                         body = msg.get_payload(decode=True).decode()

# # # # # # # #                     # Append email data with mailbox name
# # # # # # # #                     emails.append({"mailbox": mailbox_name, "subject": subject, "body": body, "from": from_})
    
# # # # # # # #     # Logout from the server
# # # # # # # #     mail.logout()
    
# # # # # # # #     return emails

# # # # # # # # # Function to generate a PDF from Gmail messages
# # # # # # # # def getMailsAndMakePDF(email_user, email_pass):
# # # # # # # #     # Create a new PDF instance
# # # # # # # #     pdf = FPDF()
# # # # # # # #     pdf.add_page()

# # # # # # # #     # Add a Unicode font (you need to provide the path to the .ttf file)
# # # # # # # #     pdf.add_font('DejaVu', '', 'DejaVuSans.ttf', uni=True)
# # # # # # # #     pdf.set_font('DejaVu', '', 14)

# # # # # # # #     # Fetch emails from all mailboxes
# # # # # # # #     emails = getGmailMessagesFromAllMailboxes(email_user, email_pass)

# # # # # # # #     # Iterate through the emails and add them to the PDF
# # # # # # # #     for i, email_data in enumerate(emails, start=1):
# # # # # # # #         subject = email_data.get("subject", "No Subject")
# # # # # # # #         body = email_data.get("body", "No Content")
# # # # # # # #         from_ = email_data.get("from", "Unknown Sender")
# # # # # # # #         mailbox = email_data.get("mailbox", "Unknown Mailbox")

# # # # # # # #         # Add the subject, sender, mailbox, and body to the PDF
# # # # # # # #         pdf.cell(200, 10, f"Email {i} from {mailbox}: {subject}", ln=True)
# # # # # # # #         pdf.cell(200, 10, f"From: {from_}", ln=True)
# # # # # # # #         pdf.multi_cell(0, 10, f"Body: {body}\n", ln=True)

# # # # # # # #     # Output the PDF file
# # # # # # # #     pdf_output = "emails.pdf"
# # # # # # # #     pdf.output(pdf_output)

# # # # # # # #     return pdf_output

# # # # # # # # # # Example usage
# # # # # # # # # if __name__ == "__main__":
# # # # # # # # #     # Replace with actual Gmail credentials
# # # # # # # # #     email_user = "your-email@gmail.com"
# # # # # # # # #     email_pass = "your-password"
    
# # # # # # # # #     # Generate the PDF with Gmail messages
# # # # # # # # #     pdf_file = getMailsAndMakePDF(email_user, email_pass)
# # # # # # # # #     print(f"PDF generated: {pdf_file}")




# # # # # # # # # import imaplib
# # # # # # # # # import email
# # # # # # # # # from email.header import decode_header
# # # # # # # # # from fpdf import FPDF
# # # # # # # # # from io import BytesIO
# # # # # # # # # from flask import send_file
# # # # # # # # # from fpdf import FPDF

# # # # # # # # # # Function to fetch Gmail messages (Placeholder - you need to implement this)
# # # # # # # # # def getGmailMessages(email, password):
# # # # # # # # #     # Here you will write the logic to fetch emails from Gmail using IMAP or Gmail API.
# # # # # # # # #     # The following is just an example structure:
# # # # # # # # #     return [
# # # # # # # # #         {"subject": "Test Email 1 – Special Character", "body": "This is a test email with special character –"},
# # # # # # # # #         {"subject": "Test Email 2", "body": "This is another test email with regular characters."}
# # # # # # # # #     ]

# # # # # # # # # # Function to generate a PDF from Gmail messages
# # # # # # # # # def getMailsAndMakePDF(email, password):
# # # # # # # # #     # Create a new PDF instance
# # # # # # # # #     pdf = FPDF()
# # # # # # # # #     pdf.add_page()

# # # # # # # # #     # Add a Unicode font (you need to provide the path to the .ttf file)
# # # # # # # # #     pdf.add_font('DejaVu', '', 'path/to/DejaVuSans.ttf', uni=True)
# # # # # # # # #     pdf.set_font('DejaVu', '', 14)

# # # # # # # # #     # Fetch emails using your logic
# # # # # # # # #     emails = getGmailMessages(email, password)

# # # # # # # # #     # Iterate through the emails and add them to the PDF
# # # # # # # # #     for i, email in enumerate(emails, start=1):
# # # # # # # # #         subject = email.get("subject", "No Subject")
# # # # # # # # #         body = email.get("body", "No Content")

# # # # # # # # #         # Add the subject and body to the PDF
# # # # # # # # #         pdf.cell(200, 10, f"Email {i}: {subject}", ln=True)
# # # # # # # # #         pdf.multi_cell(0, 10, f"Body: {body}\n", ln=True)

# # # # # # # # #     # Output the PDF file
# # # # # # # # #     pdf_output = "emails.pdf"
# # # # # # # # #     pdf.output(pdf_output)

# # # # # # # # #     return pdf_output

# # # # # # # # # # def getMailsAndMakePDF(username, password):
# # # # # # # # # #     # Create a BytesIO object to hold the PDF in memory
# # # # # # # # # #     pdf_output = BytesIO()
# # # # # # # # # #     pdf = FPDF()
# # # # # # # # # #     pdf.set_auto_page_break(auto=True, margin=15)
# # # # # # # # # #     pdf.add_page()
# # # # # # # # # #     pdf.set_font("Arial", size=12)

# # # # # # # # # #     # Connect to the Gmail IMAP server
# # # # # # # # # #     try:
# # # # # # # # # #         imap = imaplib.IMAP4_SSL("imap.gmail.com")
# # # # # # # # # #         imap.login(username, password)
# # # # # # # # # #     except imaplib.IMAP4.error as e:
# # # # # # # # # #         print(f"Login failed: {str(e)}")
# # # # # # # # # #         return None

# # # # # # # # # #     # Select the mailbox (e.g., "inbox")
# # # # # # # # # #     imap.select("inbox")

# # # # # # # # # #     # Search for all emails
# # # # # # # # # #     status, messages = imap.search(None, "ALL")

# # # # # # # # # #     # Convert message numbers from byte string to a list of integers
# # # # # # # # # #     message_ids = messages[0].split()

# # # # # # # # # #     # Limit to the first 10 emails
# # # # # # # # # #     first_ten_emails = message_ids[:10]

# # # # # # # # # #     # Fetch and display each of the first 10 emails
# # # # # # # # # #     for num in first_ten_emails:
# # # # # # # # # #         status, msg_data = imap.fetch(num, "(RFC822)")

# # # # # # # # # #         for response_part in msg_data:
# # # # # # # # # #             if isinstance(response_part, tuple):
# # # # # # # # # #                 msg = email.message_from_bytes(response_part[1])

# # # # # # # # # #                 # Decode email subject
# # # # # # # # # #                 subject, encoding = decode_header(msg["Subject"])[0]
# # # # # # # # # #                 if isinstance(subject, bytes):
# # # # # # # # # #                     subject = subject.decode(encoding if encoding else "utf-8")

# # # # # # # # # #                 from_ = msg.get("From")

# # # # # # # # # #                 # Add a new page for each email
# # # # # # # # # #                 pdf.add_page()
# # # # # # # # # #                 pdf.set_font("Arial", size=12)
# # # # # # # # # #                 pdf.cell(200, 10, f"Subject: {subject}", ln=True)
# # # # # # # # # #                 pdf.cell(200, 10, f"From: {from_}", ln=True)
# # # # # # # # # #                 pdf.ln(10)  # Line break

# # # # # # # # # #                 # Process email content
# # # # # # # # # #                 if msg.is_multipart():
# # # # # # # # # #                     for part in msg.walk():
# # # # # # # # # #                         content_type = part.get_content_type()
# # # # # # # # # #                         content_disposition = str(part.get("Content-Disposition"))

# # # # # # # # # #                         if content_type == "text/plain" and "attachment" not in content_disposition:
# # # # # # # # # #                             body = decode_email_body(part)
# # # # # # # # # #                             pdf.set_font("Arial", size=10)
# # # # # # # # # #                             pdf.multi_cell(0, 10, body)

# # # # # # # # # #                 else:
# # # # # # # # # #                     body = decode_email_body(msg)
# # # # # # # # # #                     pdf.set_font("Arial", size=10)
# # # # # # # # # #                     pdf.multi_cell(0, 10, body)

# # # # # # # # # #                 pdf.ln(10)  # Line break

# # # # # # # # # #     # Save the PDF to the BytesIO object
# # # # # # # # # #     pdf.output(pdf_output, 'F')
# # # # # # # # # #     pdf_output.seek(0)  # Move to the beginning of the BytesIO buffer

# # # # # # # # # #     # Close the connection and logout
# # # # # # # # # #     imap.close()
# # # # # # # # # #     imap.logout()

# # # # # # # # # #     return pdf_output
# # # # # # # # # # from fpdf import FPDF

# # # # # # # # # # def getMailsAndMakePDF(email, password):
# # # # # # # # # #     pdf = FPDF()
# # # # # # # # # #     pdf.add_page()

# # # # # # # # # #     # Add a Unicode font
# # # # # # # # # #     pdf.add_font('DejaVu', '', 'DejaVuSans.ttf', uni=True)
# # # # # # # # # #     pdf.set_font('DejaVu', '', 14)

# # # # # # # # # #     # Example: Replace this with your actual logic to retrieve emails
# # # # # # # # # #     subject = "Some email subject with special character –"
    
# # # # # # # # # #     # Create the PDF content
# # # # # # # # # #     pdf.cell(200, 10, f"Subject: {subject}", ln=True)
    
# # # # # # # # # #     # Output the PDF
# # # # # # # # # #     pdf_output = "output.pdf"
# # # # # # # # # #     pdf.output(pdf_output)

# # # # # # # # # #     return pdf_output

# # # # # # # # # # def decode_email_body(msg):
# # # # # # # # # #     """Decode email body based on its content type."""
# # # # # # # # # #     try:
# # # # # # # # # #         body = msg.get_payload(decode=True).decode("utf-8")
# # # # # # # # # #     except UnicodeDecodeError:
# # # # # # # # # #         body = msg.get_payload(decode=True).decode("iso-8859-1", errors="ignore")

# # # # # # # # # #     return body.encode('latin1', 'replace').decode('latin1')




# # # # # # # # # # import imaplib
# # # # # # # # # # import email
# # # # # # # # # # from email.header import decode_header
# # # # # # # # # # from fpdf import FPDF
# # # # # # # # # # import os

# # # # # # # # # # def getMailsAndMakePDF(username='ss28092024@gmail.com', password='zedcbmxwmqkbjgro'):
# # # # # # # # # #     # Initialize PDF
# # # # # # # # # #     pdf = FPDF()
# # # # # # # # # #     pdf.set_auto_page_break(auto=True, margin=15)
# # # # # # # # # #     pdf.add_page()
# # # # # # # # # #     pdf.set_font("Arial", size=12)

# # # # # # # # # #     # Connect to the Gmail IMAP server
# # # # # # # # # #     try:
# # # # # # # # # #         imap = imaplib.IMAP4_SSL("imap.gmail.com")
# # # # # # # # # #         imap.login(username, password)
# # # # # # # # # #     except imaplib.IMAP4.error as e:
# # # # # # # # # #         print(f"Login failed: {str(e)}")
# # # # # # # # # #         return

# # # # # # # # # #     # Select the mailbox (e.g., "inbox")
# # # # # # # # # #     imap.select("inbox")

# # # # # # # # # #     # Search for all emails
# # # # # # # # # #     status, messages = imap.search(None, "ALL")

# # # # # # # # # #     # Convert message numbers from byte string to a list of integers
# # # # # # # # # #     message_ids = messages[0].split()

# # # # # # # # # #     # Limit to the first 10 emails
# # # # # # # # # #     first_ten_emails = message_ids[:10]

# # # # # # # # # #     # Fetch and display each of the first 10 emails
# # # # # # # # # #     for num in first_ten_emails:
# # # # # # # # # #         # Fetch the email message by ID
# # # # # # # # # #         status, msg_data = imap.fetch(num, "(RFC822)")

# # # # # # # # # #         for response_part in msg_data:
# # # # # # # # # #             if isinstance(response_part, tuple):
# # # # # # # # # #                 # Parse the email content
# # # # # # # # # #                 msg = email.message_from_bytes(response_part[1])

# # # # # # # # # #                 # Decode email subject
# # # # # # # # # #                 subject, encoding = decode_header(msg["Subject"])[0]
# # # # # # # # # #                 if isinstance(subject, bytes):
# # # # # # # # # #                     subject = subject.decode(encoding if encoding else "utf-8")

# # # # # # # # # #                 # Decode email sender
# # # # # # # # # #                 from_ = msg.get("From")

# # # # # # # # # #                 # Add a new page for each email
# # # # # # # # # #                 pdf.add_page()
# # # # # # # # # #                 pdf.set_font("Arial", size=12)
# # # # # # # # # #                 pdf.cell(200, 10, f"Subject: {subject}", ln=True)
# # # # # # # # # #                 pdf.cell(200, 10, f"From: {from_}", ln=True)
# # # # # # # # # #                 pdf.ln(10)  # Line break

# # # # # # # # # #                 # Process email content
# # # # # # # # # #                 if msg.is_multipart():
# # # # # # # # # #                     for part in msg.walk():
# # # # # # # # # #                         content_type = part.get_content_type()
# # # # # # # # # #                         content_disposition = str(part.get("Content-Disposition"))

# # # # # # # # # #                         if content_type == "text/plain" and "attachment" not in content_disposition:
# # # # # # # # # #                             body = decode_email_body(part)
# # # # # # # # # #                             pdf.set_font("Arial", size=10)
# # # # # # # # # #                             pdf.multi_cell(0, 10, body)

# # # # # # # # # #                 else:
# # # # # # # # # #                     body = decode_email_body(msg)
# # # # # # # # # #                     pdf.set_font("Arial", size=10)
# # # # # # # # # #                     pdf.multi_cell(0, 10, body)

# # # # # # # # # #                 pdf.ln(10)  # Line break

# # # # # # # # # #     # Save the PDF
# # # # # # # # # #     pdf_output_path = "emails.pdf"
# # # # # # # # # #     pdf.output(pdf_output_path)
# # # # # # # # # #     print(f"First 10 emails saved to {pdf_output_path}")

# # # # # # # # # #     # Close the connection and logout
# # # # # # # # # #     imap.close()
# # # # # # # # # #     imap.logout()
# # # # # # # # # # getMailsAndMakePDF()

# # # # # # # # # # def decode_email_body(msg):
# # # # # # # # # #     """Decode email body based on its content type."""
# # # # # # # # # #     try:
# # # # # # # # # #         body = msg.get_payload(decode=True).decode("utf-8")
# # # # # # # # # #     except UnicodeDecodeError:
# # # # # # # # # #         body = msg.get_payload(decode=True).decode("iso-8859-1", errors="ignore")

# # # # # # # # # #     # Clean the body to remove problematic characters
# # # # # # # # # #     return body.encode('latin1', 'replace').decode('latin1')




# # # # # # # # # # import imaplib
# # # # # # # # # # import email
# # # # # # # # # # from email.header import decode_header
# # # # # # # # # # from fpdf import FPDF
# # # # # # # # # # import os

# # # # # # # # # # def getMailsAndMakePDF(username, password):
# # # # # # # # # #     # Initialize PDF
# # # # # # # # # #     pdf = FPDF()
# # # # # # # # # #     pdf.set_auto_page_break(auto=True, margin=15)

# # # # # # # # # #     # Use the default font
# # # # # # # # # #     pdf.add_page()
# # # # # # # # # #     pdf.set_font("Arial", size=12)

# # # # # # # # # #     # Connect to the Gmail IMAP server
# # # # # # # # # #     imap = imaplib.IMAP4_SSL("imap.gmail.com")

# # # # # # # # # #     # Login to the account
# # # # # # # # # #     imap.login(username, password)

# # # # # # # # # #     # Select the mailbox (e.g., "inbox")
# # # # # # # # # #     imap.select("inbox")

# # # # # # # # # #     # Search for all emails (you can also filter using 'UNSEEN', 'FROM', etc.)
# # # # # # # # # #     status, messages = imap.search(None, "ALL")

# # # # # # # # # #     # Convert message numbers from byte string to a list of integers
# # # # # # # # # #     message_ids = messages[0].split()

# # # # # # # # # #     # Limit to the first 10 emails
# # # # # # # # # #     first_ten_emails = message_ids[:10]

# # # # # # # # # #     # Fetch and display each of the first 10 emails
# # # # # # # # # #     for num in first_ten_emails:
# # # # # # # # # #         # Fetch the email message by ID
# # # # # # # # # #         status, msg_data = imap.fetch(num, "(RFC822)")

# # # # # # # # # #         for response_part in msg_data:
# # # # # # # # # #             if isinstance(response_part, tuple):
# # # # # # # # # #                 # Parse the email content
# # # # # # # # # #                 msg = email.message_from_bytes(response_part[1])

# # # # # # # # # #                 # Decode email subject
# # # # # # # # # #                 subject, encoding = decode_header(msg["Subject"])[0]
# # # # # # # # # #                 if isinstance(subject, bytes):
# # # # # # # # # #                     subject = subject.decode(encoding if encoding else "utf-8")

# # # # # # # # # #                 # Decode email sender
# # # # # # # # # #                 from_ = msg.get("From")

# # # # # # # # # #                 # Add a new page for each email
# # # # # # # # # #                 pdf.add_page()
# # # # # # # # # #                 pdf.set_font("Arial", size=12)
# # # # # # # # # #                 pdf.cell(200, 10, f"Subject: {subject}", ln=True)
# # # # # # # # # #                 pdf.cell(200, 10, f"From: {from_}", ln=True)
# # # # # # # # # #                 pdf.ln(10)  # Line break

# # # # # # # # # #                 # If the email message is multipart
# # # # # # # # # #                 if msg.is_multipart():
# # # # # # # # # #                     for part in msg.walk():
# # # # # # # # # #                         # Check the content type and display
# # # # # # # # # #                         content_type = part.get_content_type()
# # # # # # # # # #                         content_disposition = str(part.get("Content-Disposition"))

# # # # # # # # # #                         # If it's text, decode and print the body
# # # # # # # # # #                         if content_type == "text/plain" and "attachment" not in content_disposition:
# # # # # # # # # #                             try:
# # # # # # # # # #                                 body = part.get_payload(decode=True).decode("utf-8")
# # # # # # # # # #                             except UnicodeDecodeError:
# # # # # # # # # #                                 body = part.get_payload(decode=True).decode("iso-8859-1", errors="ignore")

# # # # # # # # # #                             # Clean the body to remove problematic characters
# # # # # # # # # #                             body = body.encode('latin1', 'replace').decode('latin1')

# # # # # # # # # #                             pdf.set_font("Arial", size=10)
# # # # # # # # # #                             pdf.multi_cell(0, 10, body)

# # # # # # # # # #                 else:
# # # # # # # # # #                     # If the email is not multipart, just extract the payload
# # # # # # # # # #                     try:
# # # # # # # # # #                         body = msg.get_payload(decode=True).decode("utf-8")
# # # # # # # # # #                     except UnicodeDecodeError:
# # # # # # # # # #                         body = msg.get_payload(decode=True).decode("iso-8859-1", errors="ignore")

# # # # # # # # # #                     # Clean the body to remove problematic characters
# # # # # # # # # #                     body = body.encode('latin1', 'replace').decode('latin1')

# # # # # # # # # #                     pdf.set_font("Arial", size=10)
# # # # # # # # # #                     pdf.multi_cell(0, 10, body)

# # # # # # # # # #                 pdf.ln(10)  # Line break

# # # # # # # # # #     # Save the PDF
# # # # # # # # # #     pdf_output_path = "emails.pdf"
# # # # # # # # # #     pdf.output(pdf_output_path)
# # # # # # # # # #     print(f"First 10 emails saved to {pdf_output_path}")

# # # # # # # # # #     # Close the connection and logout
# # # # # # # # # #     imap.close()
# # # # # # # # # #     imap.logout()




# # # # # # # # # # # # # import imaplib
# # # # # # # # # # # # # import email
# # # # # # # # # # # # # from email.header import decode_header
# # # # # # # # # # # # # import webbrowser
# # # # # # # # # # # # # import os

# # # # # # # # # # # # # # Login credentials
# # # # # # # # # # # # # username = "ritwikmishrastudent@gmail.com"
# # # # # # # # # # # # # password = "ezwulfhzabshjvsw"  # Use an app password

# # # # # # # # # # # # # # Connect to the Gmail IMAP server
# # # # # # # # # # # # # imap = imaplib.IMAP4_SSL("imap.gmail.com")

# # # # # # # # # # # # # # Login to the account
# # # # # # # # # # # # # imap.login(username, password)

# # # # # # # # # # # # # # Select the mailbox (e.g., "inbox")
# # # # # # # # # # # # # imap.select("inbox")

# # # # # # # # # # # # # # Search for all emails (you can also filter using 'UNSEEN', 'FROM', etc.)
# # # # # # # # # # # # # status, messages = imap.search(None, "ALL")

# # # # # # # # # # # # # # Fetch and display each email
# # # # # # # # # # # # # for num in messages[0].split():
# # # # # # # # # # # # #     # Fetch the email message by ID
# # # # # # # # # # # # #     status, msg_data = imap.fetch(num, "(RFC822)")
    
# # # # # # # # # # # # #     for response_part in msg_data:
# # # # # # # # # # # # #         if isinstance(response_part, tuple):
# # # # # # # # # # # # #             # Parse the email content
# # # # # # # # # # # # #             msg = email.message_from_bytes(response_part[1])
            
# # # # # # # # # # # # #             # Decode email subject
# # # # # # # # # # # # #             subject, encoding = decode_header(msg["Subject"])[0]
# # # # # # # # # # # # #             if isinstance(subject, bytes):
# # # # # # # # # # # # #                 subject = subject.decode(encoding if encoding else "utf-8")
            
# # # # # # # # # # # # #             # Decode email sender
# # # # # # # # # # # # #             from_ = msg.get("From")
            
# # # # # # # # # # # # #             # Print email subject and sender
# # # # # # # # # # # # #             print("Subject:", subject)
# # # # # # # # # # # # #             print("From:", from_)

# # # # # # # # # # # # #             # If the email message is multipart
# # # # # # # # # # # # #             if msg.is_multipart():
# # # # # # # # # # # # #                 for part in msg.walk():
# # # # # # # # # # # # #                     # Check the content type and display
# # # # # # # # # # # # #                     content_type = part.get_content_type()
# # # # # # # # # # # # #                     content_disposition = str(part.get("Content-Disposition"))
                    
# # # # # # # # # # # # #                     # If it's text, decode and print the body
# # # # # # # # # # # # #                     if content_type == "text/plain" and "attachment" not in content_disposition:
# # # # # # # # # # # # #                         body = part.get_payload(decode=True).decode()
# # # # # # # # # # # # #                         print("Body:", body)
                    
# # # # # # # # # # # # #                     # Handle attachments
# # # # # # # # # # # # #                     elif "attachment" in content_disposition:
# # # # # # # # # # # # #                         filename = part.get_filename()
# # # # # # # # # # # # #                         if filename:
# # # # # # # # # # # # #                             folder_name = "attachments"
# # # # # # # # # # # # #                             if not os.path.isdir(folder_name):
# # # # # # # # # # # # #                                 os.mkdir(folder_name)
# # # # # # # # # # # # #                             filepath = os.path.join(folder_name, filename)
# # # # # # # # # # # # #                             with open(filepath, "wb") as f:
# # # # # # # # # # # # #                                 f.write(part.get_payload(decode=True))
# # # # # # # # # # # # #                             print(f"Attachment saved: {filepath}")
# # # # # # # # # # # # #             else:
# # # # # # # # # # # # #                 # If the email is not multipart, just extract the payload
# # # # # # # # # # # # #                 body = msg.get_payload(decode=True).decode()
# # # # # # # # # # # # #                 print("Body:", body)
            
# # # # # # # # # # # # #             print("=" * 100)

# # # # # # # # # # # # # # Close the connection and logout
# # # # # # # # # # # # # imap.close()
# # # # # # # # # # # # # imap.logout()


# # # # # # # # # # # # import imaplib
# # # # # # # # # # # # import email
# # # # # # # # # # # # from email.header import decode_header
# # # # # # # # # # # # import os
# # # # # # # # # # # # from fpdf import FPDF
# # # # # # # # # # # # from bs4 import BeautifulSoup

# # # # # # # # # # # # # Initialize PDF
# # # # # # # # # # # # pdf = FPDF()
# # # # # # # # # # # # pdf.set_auto_page_break(auto=True, margin=15)

# # # # # # # # # # # # # Login credentials
# # # # # # # # # # # # username = "ritwikmishrastudent@gmail.com"
# # # # # # # # # # # # password = "ezwulfhzabshjvsw"  # Use an app password

# # # # # # # # # # # # # Connect to the Gmail IMAP server
# # # # # # # # # # # # imap = imaplib.IMAP4_SSL("imap.gmail.com")

# # # # # # # # # # # # # Login to the account
# # # # # # # # # # # # imap.login(username, password)

# # # # # # # # # # # # # Select the mailbox (e.g., "inbox")
# # # # # # # # # # # # imap.select("inbox")

# # # # # # # # # # # # # Search for all emails (you can also filter using 'UNSEEN', 'FROM', etc.)
# # # # # # # # # # # # status, messages = imap.search(None, "ALL")

# # # # # # # # # # # # # Fetch and display each email
# # # # # # # # # # # # for num in messages[0].split():
# # # # # # # # # # # #     # Fetch the email message by ID
# # # # # # # # # # # #     status, msg_data = imap.fetch(num, "(RFC822)")

# # # # # # # # # # # #     for response_part in msg_data:
# # # # # # # # # # # #         if isinstance(response_part, tuple):
# # # # # # # # # # # #             # Parse the email content
# # # # # # # # # # # #             msg = email.message_from_bytes(response_part[1])

# # # # # # # # # # # #             # Decode email subject
# # # # # # # # # # # #             subject, encoding = decode_header(msg["Subject"])[0]
# # # # # # # # # # # #             if isinstance(subject, bytes):
# # # # # # # # # # # #                 subject = subject.decode(encoding if encoding else "utf-8")

# # # # # # # # # # # #             # Decode email sender
# # # # # # # # # # # #             from_ = msg.get("From")

# # # # # # # # # # # #             # Add a new page for each email
# # # # # # # # # # # #             pdf.add_page()
# # # # # # # # # # # #             pdf.set_font("Arial", 'B', 12)
# # # # # # # # # # # #             pdf.cell(200, 10, f"Subject: {subject}", ln=True, align="L")
# # # # # # # # # # # #             pdf.cell(200, 10, f"From: {from_}", ln=True, align="L")
# # # # # # # # # # # #             pdf.ln(10)  # Line break

# # # # # # # # # # # #             # If the email message is multipart
# # # # # # # # # # # #             if msg.is_multipart():
# # # # # # # # # # # #                 for part in msg.walk():
# # # # # # # # # # # #                     # Check the content type and display
# # # # # # # # # # # #                     content_type = part.get_content_type()
# # # # # # # # # # # #                     content_disposition = str(part.get("Content-Disposition"))

# # # # # # # # # # # #                     # If it's text, decode and print the body
# # # # # # # # # # # #                     if content_type == "text/plain" and "attachment" not in content_disposition:
# # # # # # # # # # # #                         body = part.get_payload(decode=True).decode()
# # # # # # # # # # # #                         pdf.set_font("Arial", '', 10)
# # # # # # # # # # # #                         pdf.multi_cell(0, 10, body)

# # # # # # # # # # # #                     # Handle attachments (optional)
# # # # # # # # # # # #                     elif "attachment" in content_disposition:
# # # # # # # # # # # #                         filename = part.get_filename()
# # # # # # # # # # # #                         if filename:
# # # # # # # # # # # #                             folder_name = "attachments"
# # # # # # # # # # # #                             if not os.path.isdir(folder_name):
# # # # # # # # # # # #                                 os.mkdir(folder_name)
# # # # # # # # # # # #                             filepath = os.path.join(folder_name, filename)
# # # # # # # # # # # #                             with open(filepath, "wb") as f:
# # # # # # # # # # # #                                 f.write(part.get_payload(decode=True))
# # # # # # # # # # # #                             pdf.cell(200, 10, f"Attachment saved: {filename}", ln=True, align="L")
# # # # # # # # # # # #             else:
# # # # # # # # # # # #                 # If the email is not multipart, just extract the payload
# # # # # # # # # # # #                 body = msg.get_payload(decode=True).decode()
# # # # # # # # # # # #                 pdf.set_font("Arial", '', 10)
# # # # # # # # # # # #                 pdf.multi_cell(0, 10, body)

# # # # # # # # # # # #             # Add some separators
# # # # # # # # # # # #             pdf.ln(10)  # Line break
# # # # # # # # # # # #             pdf.cell(200, 10, "=" * 50, ln=True, align="L")

# # # # # # # # # # # # # Save the PDF
# # # # # # # # # # # # pdf_output_path = "emails.pdf"
# # # # # # # # # # # # pdf.output(pdf_output_path)
# # # # # # # # # # # # print(f"Emails saved to {pdf_output_path}")

# # # # # # # # # # # # # Close the connection and logout
# # # # # # # # # # # # imap.close()
# # # # # # # # # # # # imap.logout()






# # # # # # # # # # import imaplib
# # # # # # # # # # import email
# # # # # # # # # # from email.header import decode_header
# # # # # # # # # # from fpdf import FPDF
# # # # # # # # # # import os

# # # # # # # # # # # Initialize PDF
# # # # # # # # # # pdf = FPDF()
# # # # # # # # # # pdf.set_auto_page_break(auto=True, margin=15)

# # # # # # # # # # # Use the default font
# # # # # # # # # # pdf.add_page()
# # # # # # # # # # pdf.set_font("Arial", size=12)

# # # # # # # # # # # Login credentials
# # # # # # # # # # username = "ritwikmishrastudent@gmail.com"
# # # # # # # # # # password = "ezwulfhzabshjvsw"  # Use an app password

# # # # # # # # # # # Connect to the Gmail IMAP server
# # # # # # # # # # imap = imaplib.IMAP4_SSL("imap.gmail.com")

# # # # # # # # # # # Login to the account
# # # # # # # # # # imap.login(username, password)

# # # # # # # # # # # Select the mailbox (e.g., "inbox")
# # # # # # # # # # imap.select("inbox")

# # # # # # # # # # # Search for all emails (you can also filter using 'UNSEEN', 'FROM', etc.)
# # # # # # # # # # status, messages = imap.search(None, "ALL")

# # # # # # # # # # # Convert message numbers from byte string to a list of integers
# # # # # # # # # # message_ids = messages[0].split()

# # # # # # # # # # # Fetch and display each email (now fetching all emails)
# # # # # # # # # # for num in message_ids:
# # # # # # # # # #     # Fetch the email message by ID
# # # # # # # # # #     status, msg_data = imap.fetch(num, "(RFC822)")

# # # # # # # # # #     for response_part in msg_data:
# # # # # # # # # #         if isinstance(response_part, tuple):
# # # # # # # # # #             # Parse the email content
# # # # # # # # # #             msg = email.message_from_bytes(response_part[1])

# # # # # # # # # #             # Decode email subject
# # # # # # # # # #             subject, encoding = decode_header(msg["Subject"])[0]
# # # # # # # # # #             if isinstance(subject, bytes):
# # # # # # # # # #                 subject = subject.decode(encoding if encoding else "utf-8")

# # # # # # # # # #             # Decode email sender
# # # # # # # # # #             from_ = msg.get("From")

# # # # # # # # # #             # Add a new page for each email
# # # # # # # # # #             pdf.add_page()
# # # # # # # # # #             pdf.set_font("Arial", size=12)
# # # # # # # # # #             pdf.cell(200, 10, f"Subject: {subject}", ln=True)
# # # # # # # # # #             pdf.cell(200, 10, f"From: {from_}", ln=True)
# # # # # # # # # #             pdf.ln(10)  # Line break

# # # # # # # # # #             # If the email message is multipart
# # # # # # # # # #             if msg.is_multipart():
# # # # # # # # # #                 for part in msg.walk():
# # # # # # # # # #                     # Check the content type and display
# # # # # # # # # #                     content_type = part.get_content_type()
# # # # # # # # # #                     content_disposition = str(part.get("Content-Disposition"))

# # # # # # # # # #                     # If it's text, decode and print the body
# # # # # # # # # #                     if content_type == "text/plain" and "attachment" not in content_disposition:
# # # # # # # # # #                         try:
# # # # # # # # # #                             body = part.get_payload(decode=True).decode("utf-8")
# # # # # # # # # #                         except UnicodeDecodeError:
# # # # # # # # # #                             body = part.get_payload(decode=True).decode("iso-8859-1", errors="ignore")

# # # # # # # # # #                         # Clean the body to remove problematic characters
# # # # # # # # # #                         body = body.encode('latin1', 'replace').decode('latin1')

# # # # # # # # # #                         pdf.set_font("Arial", size=10)
# # # # # # # # # #                         pdf.multi_cell(0, 10, body)

# # # # # # # # # #             else:
# # # # # # # # # #                 # If the email is not multipart, just extract the payload
# # # # # # # # # #                 try:
# # # # # # # # # #                     body = msg.get_payload(decode=True).decode("utf-8")
# # # # # # # # # #                 except UnicodeDecodeError:
# # # # # # # # # #                     body = msg.get_payload(decode=True).decode("iso-8859-1", errors="ignore")

# # # # # # # # # #                 # Clean the body to remove problematic characters
# # # # # # # # # #                 body = body.encode('latin1', 'replace').decode('latin1')

# # # # # # # # # #                 pdf.set_font("Arial", size=10)
# # # # # # # # # #                 pdf.multi_cell(0, 10, body)

# # # # # # # # # #             pdf.ln(10)  # Line break

# # # # # # # # # # # Save the PDF
# # # # # # # # # # pdf_output_path = "emails.pdf"
# # # # # # # # # # pdf.output(pdf_output_path)
# # # # # # # # # # print(f"All emails saved to {pdf_output_path}")

# # # # # # # # # # # Close the connection and logout
# # # # # # # # # # imap.close()
# # # # # # # # # # imap.logout()



# # # # # # # # # # import imaplib
# # # # # # # # # # import email
# # # # # # # # # # from email.header import decode_header
# # # # # # # # # # from fpdf import FPDF
# # # # # # # # # # import os

# # # # # # # # # # # Initialize PDF
# # # # # # # # # # pdf = FPDF()
# # # # # # # # # # pdf.set_auto_page_break(auto=True, margin=15)

# # # # # # # # # # # Load a Unicode font (ensure the font file is in the same directory or provide a path)
# # # # # # # # # # pdf.add_page()
# # # # # # # # # # pdf.add_font("DejaVu", "", "DejaVuSans.ttf", uni=True)  # Adjust the font name and path as needed
# # # # # # # # # # pdf.set_font("DejaVu", size=12)

# # # # # # # # # # # Login credentials
# # # # # # # # # # username = "ritwikmishrastudent@gmail.com"
# # # # # # # # # # password = "ezwulfhzabshjvsw"  # Use an app password

# # # # # # # # # # # Connect to the Gmail IMAP server
# # # # # # # # # # imap = imaplib.IMAP4_SSL("imap.gmail.com")

# # # # # # # # # # # Login to the account
# # # # # # # # # # imap.login(username, password)

# # # # # # # # # # # Select the mailbox (e.g., "inbox")
# # # # # # # # # # imap.select("inbox")

# # # # # # # # # # # Search for all emails (you can also filter using 'UNSEEN', 'FROM', etc.)
# # # # # # # # # # status, messages = imap.search(None, "ALL")

# # # # # # # # # # # Convert message numbers from byte string to a list of integers
# # # # # # # # # # message_ids = messages[0].split()

# # # # # # # # # # # Fetch and display each email (now fetching all emails)
# # # # # # # # # # for num in message_ids:
# # # # # # # # # #     # Fetch the email message by ID
# # # # # # # # # #     status, msg_data = imap.fetch(num, "(RFC822)")

# # # # # # # # # #     for response_part in msg_data:
# # # # # # # # # #         if isinstance(response_part, tuple):
# # # # # # # # # #             # Parse the email content
# # # # # # # # # #             msg = email.message_from_bytes(response_part[1])

# # # # # # # # # #             # Decode email subject
# # # # # # # # # #             subject, encoding = decode_header(msg["Subject"])[0]
# # # # # # # # # #             if isinstance(subject, bytes):
# # # # # # # # # #                 subject = subject.decode(encoding if encoding else "utf-8")

# # # # # # # # # #             # Decode email sender
# # # # # # # # # #             from_ = msg.get("From")

# # # # # # # # # #             # Add a new page for each email
# # # # # # # # # #             pdf.add_page()
# # # # # # # # # #             pdf.set_font("DejaVu", size=12)
# # # # # # # # # #             pdf.cell(200, 10, f"Subject: {subject.encode('latin1', 'replace').decode('latin1')}", new_x="LMARGIN", new_y="NEXT")
# # # # # # # # # #             pdf.cell(200, 10, f"From: {from_}", new_x="LMARGIN", new_y="NEXT")
# # # # # # # # # #             pdf.ln(10)  # Line break

# # # # # # # # # #             # If the email message is multipart
# # # # # # # # # #             if msg.is_multipart():
# # # # # # # # # #                 for part in msg.walk():
# # # # # # # # # #                     # Check the content type and display
# # # # # # # # # #                     content_type = part.get_content_type()
# # # # # # # # # #                     content_disposition = str(part.get("Content-Disposition"))

# # # # # # # # # #                     # If it's text, decode and print the body
# # # # # # # # # #                     if content_type == "text/plain" and "attachment" not in content_disposition:
# # # # # # # # # #                         try:
# # # # # # # # # #                             body = part.get_payload(decode=True).decode("utf-8")
# # # # # # # # # #                         except UnicodeDecodeError:
# # # # # # # # # #                             body = part.get_payload(decode=True).decode("iso-8859-1", errors="ignore")

# # # # # # # # # #                         # Clean the body to remove problematic characters
# # # # # # # # # #                         body = body.encode('latin1', 'replace').decode('latin1')

# # # # # # # # # #                         pdf.set_font("DejaVu", size=10)
# # # # # # # # # #                         pdf.multi_cell(0, 10, body)

# # # # # # # # # #             else:
# # # # # # # # # #                 # If the email is not multipart, just extract the payload
# # # # # # # # # #                 try:
# # # # # # # # # #                     body = msg.get_payload(decode=True).decode("utf-8")
# # # # # # # # # #                 except UnicodeDecodeError:
# # # # # # # # # #                     body = msg.get_payload(decode=True).decode("iso-8859-1", errors="ignore")

# # # # # # # # # #                 # Clean the body to remove problematic characters
# # # # # # # # # #                 body = body.encode('latin1', 'replace').decode('latin1')

# # # # # # # # # #                 pdf.set_font("DejaVu", size=10)
# # # # # # # # # #                 pdf.multi_cell(0, 10, body)

# # # # # # # # # #             pdf.ln(10)  # Line break

# # # # # # # # # # # Save the PDF
# # # # # # # # # # pdf_output_path = "emails.pdf"
# # # # # # # # # # pdf.output(pdf_output_path)
# # # # # # # # # # print(f"All emails saved to {pdf_output_path}")

# # # # # # # # # # # Close the connection and logout
# # # # # # # # # # imap.close()
# # # # # # # # # # imap.logout()




# # # # # # # import imaplib
# # # # # # # import email
# # # # # # # from email.header import decode_header
# # # # # # # from fpdf import FPDF

# # # # # # # # Function to connect to Gmail and fetch emails from all mailboxes
# # # # # # # def getGmailMessagesFromAllMailboxes(email_user, email_pass):
# # # # # # #     # Connect to the Gmail IMAP server
# # # # # # #     mail = imaplib.IMAP4_SSL("imap.gmail.com")
    
# # # # # # #     # Login to the account
# # # # # # #     mail.login(email_user, email_pass)
    
# # # # # # #     # List all mailboxes
# # # # # # #     status, mailboxes = mail.list()

# # # # # # #     if status != 'OK':
# # # # # # #         print("Error fetching mailboxes.")
# # # # # # #         return []

# # # # # # #     # List to store email data
# # # # # # #     emails = []
    
# # # # # # #     # Iterate through all mailboxes
# # # # # # #     for mailbox in mailboxes:
# # # # # # #         # Parse the mailbox name (the mailbox name is the last token in the response)
# # # # # # #         mailbox_name = mailbox.decode().split(' "/" ')[-1].strip('"')
        
# # # # # # #         # Try to select the mailbox
# # # # # # #         try:
# # # # # # #             status, _ = mail.select(mailbox_name)
# # # # # # #             if status != 'OK':
# # # # # # #                 print(f"Could not select mailbox: {mailbox_name}")
# # # # # # #                 continue  # Skip to the next mailbox if this one fails
# # # # # # #         except Exception as e:
# # # # # # #             print(f"Error selecting mailbox {mailbox_name}: {str(e)}")
# # # # # # #             continue
        
# # # # # # #         # Search for all emails in the current mailbox
# # # # # # #         status, messages = mail.search(None, "ALL")
# # # # # # #         if status != 'OK':
# # # # # # #             print(f"Error searching in mailbox: {mailbox_name}")
# # # # # # #             continue
        
# # # # # # #         # Convert the result list into a list of email IDs
# # # # # # #         email_ids = messages[0].split()

# # # # # # #         # Fetch and process the last 5 emails from the current mailbox
# # # # # # #         for email_id in email_ids[-5:]:
# # # # # # #             # Fetch the email by ID
# # # # # # #             status, msg_data = mail.fetch(email_id, "(RFC822)")

# # # # # # #             for response_part in msg_data:
# # # # # # #                 if isinstance(response_part, tuple):
# # # # # # #                     msg = email.message_from_bytes(response_part[1])

# # # # # # #                     # Decode the email subject
# # # # # # #                     subject, encoding = decode_header(msg["Subject"])[0]
# # # # # # #                     if isinstance(subject, bytes):
# # # # # # #                         subject = subject.decode(encoding if encoding else "utf-8")

# # # # # # #                     # Email sender
# # # # # # #                     from_ = msg.get("From")

# # # # # # #                     # Email body
# # # # # # #                     if msg.is_multipart():
# # # # # # #                         for part in msg.walk():
# # # # # # #                             content_type = part.get_content_type()
# # # # # # #                             content_disposition = str(part.get("Content-Disposition"))
# # # # # # #                             if "attachment" not in content_disposition:
# # # # # # #                                 try:
# # # # # # #                                     body = part.get_payload(decode=True).decode()
# # # # # # #                                 except:
# # # # # # #                                     body = "No body found."
# # # # # # #                     else:
# # # # # # #                         body = msg.get_payload(decode=True).decode()

# # # # # # #                     # Append email data with mailbox name
# # # # # # #                     emails.append({"mailbox": mailbox_name, "subject": subject, "body": body, "from": from_})
    
# # # # # # #     # Logout from the server
# # # # # # #     mail.logout()
    
# # # # # # #     return emails

# # # # # # # # Function to generate a PDF from Gmail messages
# # # # # # # def getMailsAndMakePDF(email_user, email_pass):
# # # # # # #     # Create a new PDF instance
# # # # # # #     pdf = FPDF()
# # # # # # #     pdf.add_page()

# # # # # # #     # Add a Unicode font (you need to provide the path to the .ttf file)
# # # # # # #     pdf.add_font('DejaVu', '', 'DejaVuSans.ttf', uni=True)
# # # # # # #     pdf.set_font('DejaVu', '', 14)

# # # # # # #     # Fetch emails from all mailboxes
# # # # # # #     emails = getGmailMessagesFromAllMailboxes(email_user, email_pass)

# # # # # # #     # Iterate through the emails and add them to the PDF
# # # # # # #     for i, email_data in enumerate(emails, start=1):
# # # # # # #         subject = email_data.get("subject", "No Subject")
# # # # # # #         body = email_data.get("body", "No Content")
# # # # # # #         from_ = email_data.get("from", "Unknown Sender")
# # # # # # #         mailbox = email_data.get("mailbox", "Unknown Mailbox")

# # # # # # #         # Add the subject, sender, mailbox, and body to the PDF
# # # # # # #         pdf.cell(200, 10, f"Email {i} from {mailbox}: {subject}", ln=True)
# # # # # # #         pdf.cell(200, 10, f"From: {from_}", ln=True)
# # # # # # #         pdf.multi_cell(0, 10, f"Body: {body}\n", ln=True)

# # # # # # #     # Output the PDF file
# # # # # # #     pdf_output = "emails.pdf"
# # # # # # #     pdf.output(pdf_output)

# # # # # # #     return pdf_output

# # # # # # # # # Example usage
# # # # # # # # if __name__ == "__main__":
# # # # # # # #     # Replace with actual Gmail credentials
# # # # # # # #     email_user = "your-email@gmail.com"
# # # # # # # #     email_pass = "your-password"
    
# # # # # # # #     # Generate the PDF with Gmail messages
# # # # # # # #     pdf_file = getMailsAndMakePDF(email_user, email_pass)
# # # # # # # #     print(f"PDF generated: {pdf_file}")




# # # # # # import imaplib
# # # # # # import email
# # # # # # from email.header import decode_header
# # # # # # from bs4 import BeautifulSoup
# # # # # # from fpdf import FPDF

# # # # # # # Function to authenticate and get mailboxes
# # # # # # def authenticate_gmail(username, password):
# # # # # #     mail = imaplib.IMAP4_SSL("imap.gmail.com")
# # # # # #     mail.login(username, password)
# # # # # #     return mail

# # # # # # # Function to get Gmail messages from all mailboxes
# # # # # # def get_gmail_messages_from_all_mailboxes(email_user, email_pass):
# # # # # #     mail = authenticate_gmail(email_user, email_pass)

# # # # # #     # List all mailboxes
# # # # # #     status, mailboxes = mail.list()
# # # # # #     if status != "OK":
# # # # # #         raise Exception("Failed to retrieve mailboxes")

# # # # # #     all_emails = []

# # # # # #     # Select and retrieve emails from each mailbox
# # # # # #     for mailbox in mailboxes:
# # # # # #         mailbox_info = mailbox.decode().split(' "/" ')
# # # # # #         mailbox_name = mailbox_info[-1]
        
# # # # # #         mail.select(mailbox_name)
# # # # # #         status, messages = mail.search(None, "ALL")

# # # # # #         if status != "OK":
# # # # # #             print(f"Failed to retrieve emails from {mailbox_name}")
# # # # # #             continue

# # # # # #         for num in messages[0].split():
# # # # # #             status, msg_data = mail.fetch(num, "(RFC822)")
# # # # # #             if status != "OK":
# # # # # #                 print(f"Failed to fetch message {num}")
# # # # # #                 continue

# # # # # #             for response_part in msg_data:
# # # # # #                 if isinstance(response_part, tuple):
# # # # # #                     msg = email.message_from_bytes(response_part[1])
# # # # # #                     subject, encoding = decode_header(msg["Subject"])[0]
# # # # # #                     if isinstance(subject, bytes):
# # # # # #                         subject = subject.decode(encoding if encoding else "utf-8")
# # # # # #                     from_ = msg.get("From")
# # # # # #                     date_ = msg.get("Date")

# # # # # #                     if msg.is_multipart():
# # # # # #                         for part in msg.walk():
# # # # # #                             content_type = part.get_content_type()
# # # # # #                             if "text/plain" in content_type or "text/html" in content_type:
# # # # # #                                 try:
# # # # # #                                     body = part.get_payload(decode=True).decode("utf-8")
# # # # # #                                 except:
# # # # # #                                     continue

# # # # # #                                 if "html" in content_type:
# # # # # #                                     soup = BeautifulSoup(body, "html.parser")
# # # # # #                                     body = soup.get_text()

# # # # # #                     else:
# # # # # #                         content_type = msg.get_content_type()
# # # # # #                         body = msg.get_payload(decode=True).decode("utf-8")
# # # # # #                         if "html" in content_type:
# # # # # #                             soup = BeautifulSoup(body, "html.parser")
# # # # # #                             body = soup.get_text()

# # # # # #                     email_data = {
# # # # # #                         "subject": subject,
# # # # # #                         "from": from_,
# # # # # #                         "date": date_,
# # # # # #                         "body": body[:100],  # Just a snippet for summary
# # # # # #                     }

# # # # # #                     all_emails.append(email_data)

# # # # # #     mail.logout()
# # # # # #     return all_emails

# # # # # # # Function to generate PDF from email data
# # # # # # def create_pdf(emails, output_filename):
# # # # # #     pdf = FPDF()
# # # # # #     pdf.set_auto_page_break(auto=True, margin=15)
# # # # # #     pdf.add_page()
# # # # # #     pdf.set_font("Arial", "B", 16)
# # # # # #     pdf.cell(200, 10, txt="Gmail Emails Report", ln=True, align="C")

# # # # # #     for i, email_data in enumerate(emails, 1):
# # # # # #         pdf.set_font("Arial", "B", 12)
# # # # # #         pdf.cell(200, 10, txt=f"Email {i}:", ln=True)

# # # # # #         pdf.set_font("Arial", "", 11)
# # # # # #         pdf.multi_cell(0, 10, f"From: {email_data['from']}")
# # # # # #         pdf.multi_cell(0, 10, f"Date: {email_data['date']}")
# # # # # #         pdf.multi_cell(0, 10, f"Subject: {email_data['subject']}")
# # # # # #         pdf.multi_cell(0, 10, f"Body: {email_data['body']}\n")

# # # # # #     pdf.output(output_filename)

# # # # # # # Main function to get emails and create PDF
# # # # # # def getMailsAndMakePDF(email_user, email_pass, output_filename="gmail_emails.pdf"):
# # # # # #     emails = get_gmail_messages_from_all_mailboxes(email_user, email_pass)
# # # # # #     create_pdf(emails, output_filename)
# # # # # #     return output_filename


# # # # # import imaplib
# # # # # import email
# # # # # from email.header import decode_header
# # # # # from bs4 import BeautifulSoup
# # # # # from fpdf import FPDF

# # # # # # Function to authenticate and get mailboxes
# # # # # def authenticate_gmail(username, password):
# # # # #     mail = imaplib.IMAP4_SSL("imap.gmail.com")
# # # # #     mail.login(username, password)
# # # # #     return mail

# # # # # # Function to get Gmail messages from all mailboxes
# # # # # def get_gmail_messages_from_all_mailboxes(email_user, email_pass):
# # # # #     mail = authenticate_gmail(email_user, email_pass)

# # # # #     # Select the "INBOX" mailbox explicitly
# # # # #     mail.select("inbox")
    
# # # # #     status, messages = mail.search(None, "ALL")
# # # # #     if status != "OK":
# # # # #         raise Exception("Failed to retrieve emails")

# # # # #     all_emails = []
    
# # # # #     for num in messages[0].split():
# # # # #         status, msg_data = mail.fetch(num, "(RFC822)")
# # # # #         if status != "OK":
# # # # #             print(f"Failed to fetch message {num}")
# # # # #             continue

# # # # #         for response_part in msg_data:
# # # # #             if isinstance(response_part, tuple):
# # # # #                 msg = email.message_from_bytes(response_part[1])
# # # # #                 subject, encoding = decode_header(msg["Subject"])[0]
# # # # #                 if isinstance(subject, bytes):
# # # # #                     subject = subject.decode(encoding if encoding else "utf-8")
# # # # #                 from_ = msg.get("From")
# # # # #                 date_ = msg.get("Date")

# # # # #                 if msg.is_multipart():
# # # # #                     for part in msg.walk():
# # # # #                         content_type = part.get_content_type()
# # # # #                         if "text/plain" in content_type or "text/html" in content_type:
# # # # #                             try:
# # # # #                                 body = part.get_payload(decode=True).decode("utf-8")
# # # # #                             except:
# # # # #                                 continue

# # # # #                             if "html" in content_type:
# # # # #                                 soup = BeautifulSoup(body, "html.parser")
# # # # #                                 body = soup.get_text()

# # # # #                 else:
# # # # #                     content_type = msg.get_content_type()
# # # # #                     body = msg.get_payload(decode=True).decode("utf-8")
# # # # #                     if "html" in content_type:
# # # # #                         soup = BeautifulSoup(body, "html.parser")
# # # # #                         body = soup.get_text()

# # # # #                 email_data = {
# # # # #                     "subject": subject,
# # # # #                     "from": from_,
# # # # #                     "date": date_,
# # # # #                     "body": body[:100],  # Just a snippet for summary
# # # # #                 }

# # # # #                 all_emails.append(email_data)

# # # # #     mail.logout()
# # # # #     return all_emails

# # # # # # Function to generate PDF from email data
# # # # # def create_pdf(emails, output_filename):
# # # # #     pdf = FPDF()
# # # # #     pdf.set_auto_page_break(auto=True, margin=15)
# # # # #     pdf.add_page()
# # # # #     pdf.set_font("Arial", "B", 16)
# # # # #     pdf.cell(200, 10, txt="Gmail Emails Report", ln=True, align="C")

# # # # #     for i, email_data in enumerate(emails, 1):
# # # # #         pdf.set_font("Arial", "B", 12)
# # # # #         pdf.cell(200, 10, txt=f"Email {i}:", ln=True)

# # # # #         pdf.set_font("Arial", "", 11)
# # # # #         pdf.multi_cell(0, 10, f"From: {email_data['from']}")
# # # # #         pdf.multi_cell(0, 10, f"Date: {email_data['date']}")
# # # # #         pdf.multi_cell(0, 10, f"Subject: {email_data['subject']}")
# # # # #         pdf.multi_cell(0, 10, f"Body: {email_data['body']}\n")

# # # # #     pdf.output(output_filename)

# # # # # # Main function to get emails and create PDF
# # # # # def getMailsAndMakePDF(email_user, email_pass, output_filename="gmail_emails.pdf"):
# # # # #     emails = get_gmail_messages_from_all_mailboxes(email_user, email_pass)
# # # # #     create_pdf(emails, output_filename)
# # # # #     return output_filename



# # # # import imaplib
# # # # import email
# # # # from email.header import decode_header
# # # # from fpdf import FPDF
# # # # import os

# # # # # Function to authenticate and login to Gmail
# # # # def login_to_gmail(email_user, email_pass):
# # # #     try:
# # # #         mail = imaplib.IMAP4_SSL("imap.gmail.com")
# # # #         mail.login(email_user, email_pass)
# # # #         return mail
# # # #     except imaplib.IMAP4.error:
# # # #         return None

# # # # # Function to fetch emails from Gmail
# # # # def get_gmail_messages_from_all_mailboxes(email_user, email_pass):
# # # #     mail = login_to_gmail(email_user, email_pass)
# # # #     if mail is None:
# # # #         return None
    
# # # #     emails = []

# # # #     mail.select("inbox")  # Select inbox, can change to any other folder
# # # #     status, messages = mail.search(None, "ALL")
# # # #     email_ids = messages[0].split()

# # # #     for num in email_ids:
# # # #         status, msg_data = mail.fetch(num, "(RFC822)")
# # # #         for response_part in msg_data:
# # # #             if isinstance(response_part, tuple):
# # # #                 msg = email.message_from_bytes(response_part[1])
# # # #                 subject, encoding = decode_header(msg["Subject"])[0]
# # # #                 if isinstance(subject, bytes):
# # # #                     subject = subject.decode(encoding if encoding else "utf-8")
# # # #                 from_ = msg.get("From")
# # # #                 date = msg.get("Date")

# # # #                 # Get the email body
# # # #                 if msg.is_multipart():
# # # #                     for part in msg.walk():
# # # #                         if part.get_content_type() == "text/plain":
# # # #                             body = part.get_payload(decode=True).decode("utf-8", errors="ignore")
# # # #                             break
# # # #                 else:
# # # #                     body = msg.get_payload(decode=True).decode("utf-8", errors="ignore")

# # # #                 emails.append({
# # # #                     "from": from_,
# # # #                     "date": date,
# # # #                     "subject": subject,
# # # #                     "body": body
# # # #                 })
    
# # # #     mail.logout()
# # # #     return emails

# # # # # Function to create PDF from email data
# # # # # Function to create PDF from email data
# # # # def create_pdf(emails, output_filename):
# # # #     pdf = FPDF()
# # # #     pdf.set_auto_page_break(auto=True, margin=15)
# # # #     pdf.add_page()
# # # #     pdf.set_font("Arial", "B", 16)
# # # #     pdf.cell(200, 10, txt="Gmail Emails Report", ln=True, align="C")

# # # #     for i, email_data in enumerate(emails, 1):
# # # #         pdf.set_font("Arial", "B", 12)
# # # #         pdf.cell(200, 10, txt=f"Email {i}:", ln=True)

# # # #         pdf.set_font("Arial", "", 11)
        
# # # #         # Handle 'from' field safely
# # # #         from_data = email_data['from'] if email_data['from'] else "Unknown Sender"
# # # #         pdf.multi_cell(0, 10, f"From: {truncate_text(from_data, 100)}")  # Truncate if necessary
        
# # # #         # Handle 'date' field safely
# # # #         date_data = email_data['date'] if email_data['date'] else "Unknown Date"
# # # #         pdf.multi_cell(0, 10, f"Date: {truncate_text(date_data, 50)}")  # Truncate date if necessary
        
# # # #         # Handle 'subject' field and truncate long subjects
# # # #         subject_data = email_data['subject'] if email_data['subject'] else "No Subject"
# # # #         pdf.multi_cell(0, 10, f"Subject: {truncate_text(subject_data, 100)}")  # Truncate subject if too long
        
# # # #         # Handle 'body' field and truncate long bodies
# # # #         body_data = email_data['body'] if email_data['body'] else "No Content"
# # # #         pdf.multi_cell(0, 10, f"Body: {truncate_text(body_data, 500)}\n")  # Truncate body content

# # # #     pdf.output(output_filename)

# # # # # Helper function to truncate text
# # # # def truncate_text(text, max_length):
# # # #     if len(text) > max_length:
# # # #         return text[:max_length] + "..."
# # # #     return text

# # # # # Function to fetch emails and generate a PDF
# # # # def getMailsAndMakePDF(email_user, email_pass):
# # # #     emails = get_gmail_messages_from_all_mailboxes(email_user, email_pass)
# # # #     if emails is None:
# # # #         return None

# # # #     output_filename = "gmail_emails_report.pdf"
# # # #     create_pdf(emails, output_filename)

# # # #     return output_filename



# # # import imaplib
# # # import email
# # # from email.header import decode_header
# # # from fpdf import FPDF
# # # import os

# # # def getMailsAndMakePDF(email_user, email_pass):
# # #     try:
# # #         # Connect to the Gmail IMAP server
# # #         mail = imaplib.IMAP4_SSL("imap.gmail.com")
# # #         mail.login(email_user, email_pass)

# # #         # Select the mailbox you want to read from (in this case, "inbox")
# # #         mail.select("inbox")

# # #         # Search for all emails in the inbox
# # #         status, messages = mail.search(None, "ALL")
# # #         mail_ids = messages[0].split()

# # #         # Create a PDF
# # #         pdf = FPDF()
# # #         pdf.set_auto_page_break(auto=True, margin=15)
# # #         pdf.add_page()
# # #         pdf.set_font("Arial", size=12)

# # #         # Process each email
# # #         for i in range(min(10, len(mail_ids))):  # Fetch max 10 emails
# # #             mail_id = mail_ids[i]
# # #             status, msg_data = mail.fetch(mail_id, "(RFC822)")

# # #             for response_part in msg_data:
# # #                 if isinstance(response_part, tuple):
# # #                     msg = email.message_from_bytes(response_part[1])
# # #                     subject, encoding = decode_header(msg["Subject"])[0]
# # #                     if isinstance(subject, bytes):
# # #                         subject = subject.decode(encoding if encoding else "utf-8")
# # #                     from_ = msg.get("From")
# # #                     date_ = msg.get("Date")

# # #                     # Write email details to PDF
# # #                     pdf.cell(200, 10, txt=f"From: {from_}", ln=True)
# # #                     pdf.cell(200, 10, txt=f"Subject: {subject}", ln=True)
# # #                     pdf.cell(200, 10, txt=f"Date: {date_}", ln=True)

# # #                     if msg.is_multipart():
# # #                         for part in msg.walk():
# # #                             content_type = part.get_content_type()
# # #                             try:
# # #                                 body = part.get_payload(decode=True).decode()
# # #                                 if content_type == "text/plain":
# # #                                     pdf.multi_cell(0, 10, body)
# # #                             except:
# # #                                 pass
# # #                     else:
# # #                         content_type = msg.get_content_type()
# # #                         body = msg.get_payload(decode=True).decode()
# # #                         if content_type == "text/plain":
# # #                             pdf.multi_cell(0, 10, body)

# # #         # Save the PDF to a file
# # #         output_filename = "emails.pdf"
# # #         pdf.output(output_filename)

# # #         mail.logout()
# # #         return output_filename

# # #     except Exception as e:
# # #         print(f"An error occurred: {str(e)}")
# # #         return None



# # import imaplib
# # import email
# # from email.header import decode_header
# # import os
# # from fpdf import FPDF

# # def getMailsAndMakePDF(email_user, email_pass):
# #     try:
# #         # Connect to the Gmail server
# #         imap = imaplib.IMAP4_SSL("imap.gmail.com")
# #         imap.login(email_user, email_pass)

# #         # Select the mailbox (in this case, "inbox")
# #         imap.select("inbox")

# #         # Search for all emails
# #         status, messages = imap.search(None, "ALL")
# #         if status != "OK":
# #             raise Exception("Failed to retrieve emails")

# #         email_ids = messages[0].split()

# #         # Create PDF instance
# #         pdf = FPDF()
# #         pdf.set_auto_page_break(auto=True, margin=15)
# #         pdf.add_page()
# #         pdf.set_font("Arial", size=12)

# #         # Iterate through each email
# #         for email_id in email_ids[-10:]:  # Fetch last 10 emails for testing
# #             res, msg = imap.fetch(email_id, "(RFC822)")
# #             if res != "OK":
# #                 raise Exception(f"Failed to fetch email with ID: {email_id}")

# #             for response_part in msg:
# #                 if isinstance(response_part, tuple):
# #                     msg = email.message_from_bytes(response_part[1])
# #                     subject, encoding = decode_header(msg["Subject"])[0]
# #                     if isinstance(subject, bytes):
# #                         subject = subject.decode(encoding if encoding else "utf-8")
# #                     sender = msg.get("From")
# #                     date = msg.get("Date")

# #                     # Debugging logs
# #                     print(f"Processing email from {sender}, subject: {subject}")

# #                     # Add email details to PDF
# #                     pdf.cell(200, 10, txt=f"From: {sender}", ln=True)
# #                     pdf.cell(200, 10, txt=f"Subject: {subject}", ln=True)
# #                     pdf.cell(200, 10, txt=f"Date: {date}", ln=True)

# #                     # Email body
# #                     if msg.is_multipart():
# #                         for part in msg.walk():
# #                             if part.get_content_type() == "text/plain":
# #                                 body = part.get_payload(decode=True).decode("utf-8", errors="ignore")
# #                                 pdf.multi_cell(0, 10, body[:200])  # Limiting to 200 characters for testing
# #                                 break
# #                     else:
# #                         body = msg.get_payload(decode=True).decode("utf-8", errors="ignore")
# #                         pdf.multi_cell(0, 10, body[:200])  # Limiting to 200 characters for testing

# #                     pdf.cell(200, 10, txt="------------------------", ln=True)

# #         # Save the generated PDF
# #         output_filename = "emails.pdf"
# #         pdf.output(output_filename)
# #         print(f"PDF saved as {output_filename}")

# #         # Logout and close the connection
# #         imap.logout()

# #         return output_filename

# #     except Exception as e:
# #         print(f"Error: {str(e)}")

# import imaplib
# import email
# from email.header import decode_header
# from fpdf import FPDF
# from io import BytesIO

# def getMailsAndMakePDF(username, password):
#     # Create a buffer for PDF content (BytesIO)
#     pdf_buffer = BytesIO()
    
#     # Initialize PDF
#     pdf = FPDF()
#     pdf.set_auto_page_break(auto=True, margin=15)

#     # Use the default font
#     pdf.add_page()
#     pdf.set_font("Arial", size=12)

#     # Connect to the Gmail IMAP server
#     imap = imaplib.IMAP4_SSL("imap.gmail.com")

#     try:
#         # Login to the account
#         imap.login(username, password)

#         # Select the mailbox (e.g., "inbox")
#         imap.select("inbox")

#         # Search for all emails (you can also filter using 'UNSEEN', 'FROM', etc.)
#         status, messages = imap.search(None, "ALL")

#         # Convert message numbers from byte string to a list of integers
#         message_ids = messages[0].split()

#         # Fetch and display each email
#         for num in message_ids:
#             # Fetch the email message by ID
#             status, msg_data = imap.fetch(num, "(RFC822)")

#             for response_part in msg_data:
#                 if isinstance(response_part, tuple):
#                     # Parse the email content
#                     msg = email.message_from_bytes(response_part[1])

#                     # Decode email subject
#                     subject, encoding = decode_header(msg["Subject"])[0]
#                     if isinstance(subject, bytes):
#                         subject = subject.decode(encoding if encoding else "utf-8")

#                     # Decode email sender
#                     from_ = msg.get("From")

#                     # Add a new page for each email
#                     pdf.add_page()
#                     pdf.set_font("Arial", size=12)
#                     pdf.cell(200, 10, f"Subject: {subject}", ln=True)
#                     pdf.cell(200, 10, f"From: {from_}", ln=True)
#                     pdf.ln(10)  # Line break

#                     # If the email message is multipart
#                     if msg.is_multipart():
#                         for part in msg.walk():
#                             # Check the content type and display
#                             content_type = part.get_content_type()
#                             content_disposition = str(part.get("Content-Disposition"))

#                             # If it's text, decode and print the body
#                             if content_type == "text/plain" and "attachment" not in content_disposition:
#                                 try:
#                                     body = part.get_payload(decode=True).decode("utf-8")
#                                 except UnicodeDecodeError:
#                                     body = part.get_payload(decode=True).decode("iso-8859-1", errors="ignore")

#                                 # Clean the body to remove problematic characters
#                                 body = body.encode('latin1', 'replace').decode('latin1')

#                                 pdf.set_font("Arial", size=10)
#                                 pdf.multi_cell(0, 10, body)

#                     else:
#                         # If the email is not multipart, just extract the payload
#                         try:
#                             body = msg.get_payload(decode=True).decode("utf-8")
#                         except UnicodeDecodeError:
#                             body = msg.get_payload(decode=True).decode("iso-8859-1", errors="ignore")

#                         # Clean the body to remove problematic characters
#                         body = body.encode('latin1', 'replace').decode('latin1')

#                         pdf.set_font("Arial", size=10)
#                         pdf.multi_cell(0, 10, body)

#                     pdf.ln(10)  # Line break

#         # Save PDF content to the buffer instead of a file
#         pdf.output(pdf_buffer)
#         pdf_buffer.seek(0)  # Move the pointer to the beginning of the buffer

#     finally:
#         # Close the connection and logout
#         imap.close()
#         imap.logout()

#     return pdf_buffer  # Return the buffer containing the PDF content



import imaplib
import email
from email.header import decode_header
from fpdf import FPDF
from io import BytesIO

def getMailsAndMakePDF(username, password):
    # Create a buffer for PDF content (BytesIO)
    pdf_buffer = BytesIO()
    
    # Initialize PDF
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)

    # Add a custom font
    pdf.add_font("DejaVu", "", "DejaVuSans.ttf", uni=True)  # Replace with the correct path to the font file
    pdf.set_font("DejaVu", size=12)  # Use the custom font

    # Connect to the Gmail IMAP server
    imap = imaplib.IMAP4_SSL("imap.gmail.com")

    try:
        # Login to the account
        imap.login(username, password)

        # Select the mailbox (e.g., "inbox")
        imap.select("inbox")

        # Search for all emails
        status, messages = imap.search(None, "ALL")

        # Convert message numbers from byte string to a list of integers
        message_ids = messages[0].split()

        # Fetch and display each email
        for num in message_ids:
            # Fetch the email message by ID
            status, msg_data = imap.fetch(num, "(RFC822)")

            for response_part in msg_data:
                if isinstance(response_part, tuple):
                    # Parse the email content
                    msg = email.message_from_bytes(response_part[1])

                    # Decode email subject
                    subject, encoding = decode_header(msg["Subject"])[0]
                    if isinstance(subject, bytes):
                        subject = subject.decode(encoding if encoding else "utf-8")

                    # Decode email sender
                    from_ = msg.get("From")

                    # Add a new page for each email
                    pdf.add_page()
                    pdf.set_font("DejaVu", size=12)
                    pdf.cell(200, 10, f"Subject: {subject}", ln=True)
                    pdf.cell(200, 10, f"From: {from_}", ln=True)
                    pdf.ln(10)  # Line break

                    # If the email message is multipart
                    if msg.is_multipart():
                        for part in msg.walk():
                            # Check the content type and display
                            content_type = part.get_content_type()
                            content_disposition = str(part.get("Content-Disposition"))

                            # If it's text, decode and print the body
                            if content_type == "text/plain" and "attachment" not in content_disposition:
                                try:
                                    body = part.get_payload(decode=True).decode("utf-8")
                                except UnicodeDecodeError:
                                    body = part.get_payload(decode=True).decode("iso-8859-1", errors="ignore")

                                # Clean the body to remove problematic characters
                                body = body.encode('latin1', 'replace').decode('latin1')

                                pdf.set_font("DejaVu", size=10)
                                pdf.multi_cell(0, 10, body)

                    else:
                        # If the email is not multipart, just extract the payload
                        try:
                            body = msg.get_payload(decode=True).decode("utf-8")
                        except UnicodeDecodeError:
                            body = msg.get_payload(decode=True).decode("iso-8859-1", errors="ignore")

                        # Clean the body to remove problematic characters
                        body = body.encode('latin1', 'replace').decode('latin1')

                        pdf.set_font("DejaVu", size=10)
                        pdf.multi_cell(0, 10, body)

                    pdf.ln(10)  # Line break

        # Save PDF content to the buffer instead of a file
        pdf.output(pdf_buffer)
        pdf_buffer.seek(0)  # Move the pointer to the beginning of the buffer

    finally:
        # Close the connection and logout
        imap.close()
        imap.logout()

    return pdf_buffer  # Return the buffer containing the PDF content
