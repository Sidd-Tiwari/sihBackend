# # import imaplib
# # import email
# # from email.header import decode_header
# # import webbrowser
# # import os

# # # Login credentials
# # username = "ritwikmishrastudent@gmail.com"
# # password = "ezwulfhzabshjvsw"  # Use an app password

# # # Connect to the Gmail IMAP server
# # imap = imaplib.IMAP4_SSL("imap.gmail.com")

# # # Login to the account
# # imap.login(username, password)

# # # Select the mailbox (e.g., "inbox")
# # imap.select("inbox")

# # # Search for all emails (you can also filter using 'UNSEEN', 'FROM', etc.)
# # status, messages = imap.search(None, "ALL")

# # # Fetch and display each email
# # for num in messages[0].split():
# #     # Fetch the email message by ID
# #     status, msg_data = imap.fetch(num, "(RFC822)")
    
# #     for response_part in msg_data:
# #         if isinstance(response_part, tuple):
# #             # Parse the email content
# #             msg = email.message_from_bytes(response_part[1])
            
# #             # Decode email subject
# #             subject, encoding = decode_header(msg["Subject"])[0]
# #             if isinstance(subject, bytes):
# #                 subject = subject.decode(encoding if encoding else "utf-8")
            
# #             # Decode email sender
# #             from_ = msg.get("From")
            
# #             # Print email subject and sender
# #             print("Subject:", subject)
# #             print("From:", from_)

# #             # If the email message is multipart
# #             if msg.is_multipart():
# #                 for part in msg.walk():
# #                     # Check the content type and display
# #                     content_type = part.get_content_type()
# #                     content_disposition = str(part.get("Content-Disposition"))
                    
# #                     # If it's text, decode and print the body
# #                     if content_type == "text/plain" and "attachment" not in content_disposition:
# #                         body = part.get_payload(decode=True).decode()
# #                         print("Body:", body)
                    
# #                     # Handle attachments
# #                     elif "attachment" in content_disposition:
# #                         filename = part.get_filename()
# #                         if filename:
# #                             folder_name = "attachments"
# #                             if not os.path.isdir(folder_name):
# #                                 os.mkdir(folder_name)
# #                             filepath = os.path.join(folder_name, filename)
# #                             with open(filepath, "wb") as f:
# #                                 f.write(part.get_payload(decode=True))
# #                             print(f"Attachment saved: {filepath}")
# #             else:
# #                 # If the email is not multipart, just extract the payload
# #                 body = msg.get_payload(decode=True).decode()
# #                 print("Body:", body)
            
# #             print("=" * 100)

# # # Close the connection and logout
# # imap.close()
# # imap.logout()


# import imaplib
# import email
# from email.header import decode_header
# import os
# from fpdf import FPDF
# from bs4 import BeautifulSoup

# # Initialize PDF
# pdf = FPDF()
# pdf.set_auto_page_break(auto=True, margin=15)

# # Login credentials
# username = "ritwikmishrastudent@gmail.com"
# password = "ezwulfhzabshjvsw"  # Use an app password

# # Connect to the Gmail IMAP server
# imap = imaplib.IMAP4_SSL("imap.gmail.com")

# # Login to the account
# imap.login(username, password)

# # Select the mailbox (e.g., "inbox")
# imap.select("inbox")

# # Search for all emails (you can also filter using 'UNSEEN', 'FROM', etc.)
# status, messages = imap.search(None, "ALL")

# # Fetch and display each email
# for num in messages[0].split():
#     # Fetch the email message by ID
#     status, msg_data = imap.fetch(num, "(RFC822)")

#     for response_part in msg_data:
#         if isinstance(response_part, tuple):
#             # Parse the email content
#             msg = email.message_from_bytes(response_part[1])

#             # Decode email subject
#             subject, encoding = decode_header(msg["Subject"])[0]
#             if isinstance(subject, bytes):
#                 subject = subject.decode(encoding if encoding else "utf-8")

#             # Decode email sender
#             from_ = msg.get("From")

#             # Add a new page for each email
#             pdf.add_page()
#             pdf.set_font("Arial", 'B', 12)
#             pdf.cell(200, 10, f"Subject: {subject}", ln=True, align="L")
#             pdf.cell(200, 10, f"From: {from_}", ln=True, align="L")
#             pdf.ln(10)  # Line break

#             # If the email message is multipart
#             if msg.is_multipart():
#                 for part in msg.walk():
#                     # Check the content type and display
#                     content_type = part.get_content_type()
#                     content_disposition = str(part.get("Content-Disposition"))

#                     # If it's text, decode and print the body
#                     if content_type == "text/plain" and "attachment" not in content_disposition:
#                         body = part.get_payload(decode=True).decode()
#                         pdf.set_font("Arial", '', 10)
#                         pdf.multi_cell(0, 10, body)

#                     # Handle attachments (optional)
#                     elif "attachment" in content_disposition:
#                         filename = part.get_filename()
#                         if filename:
#                             folder_name = "attachments"
#                             if not os.path.isdir(folder_name):
#                                 os.mkdir(folder_name)
#                             filepath = os.path.join(folder_name, filename)
#                             with open(filepath, "wb") as f:
#                                 f.write(part.get_payload(decode=True))
#                             pdf.cell(200, 10, f"Attachment saved: {filename}", ln=True, align="L")
#             else:
#                 # If the email is not multipart, just extract the payload
#                 body = msg.get_payload(decode=True).decode()
#                 pdf.set_font("Arial", '', 10)
#                 pdf.multi_cell(0, 10, body)

#             # Add some separators
#             pdf.ln(10)  # Line break
#             pdf.cell(200, 10, "=" * 50, ln=True, align="L")

# # Save the PDF
# pdf_output_path = "emails.pdf"
# pdf.output(pdf_output_path)
# print(f"Emails saved to {pdf_output_path}")

# # Close the connection and logout
# imap.close()
# imap.logout()




import imaplib
import email
from email.header import decode_header
from fpdf import FPDF
import os

# Initialize PDF
pdf = FPDF()
pdf.set_auto_page_break(auto=True, margin=15)

# Use the default font
pdf.add_page()
pdf.set_font("Arial", size=12)

# Login credentials
username = "ritwikmishrastudent@gmail.com"
password = "ezwulfhzabshjvsw"  # Use an app password

# Connect to the Gmail IMAP server
imap = imaplib.IMAP4_SSL("imap.gmail.com")

# Login to the account
imap.login(username, password)

# Select the mailbox (e.g., "inbox")
imap.select("inbox")

# Search for all emails (you can also filter using 'UNSEEN', 'FROM', etc.)
status, messages = imap.search(None, "ALL")

# Convert message numbers from byte string to a list of integers
message_ids = messages[0].split()

# Limit to the first 10 emails
first_ten_emails = message_ids[:10]

# Fetch and display each of the first 10 emails
for num in first_ten_emails:
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
            pdf.set_font("Arial", size=12)
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

                        pdf.set_font("Arial", size=10)
                        pdf.multi_cell(0, 10, body)

            else:
                # If the email is not multipart, just extract the payload
                try:
                    body = msg.get_payload(decode=True).decode("utf-8")
                except UnicodeDecodeError:
                    body = msg.get_payload(decode=True).decode("iso-8859-1", errors="ignore")

                # Clean the body to remove problematic characters
                body = body.encode('latin1', 'replace').decode('latin1')

                pdf.set_font("Arial", size=10)
                pdf.multi_cell(0, 10, body)

            pdf.ln(10)  # Line break

# Save the PDF
pdf_output_path = "emails.pdf"
pdf.output(pdf_output_path)
print(f"First 10 emails saved to {pdf_output_path}")

# Close the connection and logout
imap.close()
imap.logout()
