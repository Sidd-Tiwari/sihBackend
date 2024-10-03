import imaplib
import email
from email.header import decode_header
import json

def fetch_emails(username, password):
    try:
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

        # Prepare a list to store email data
        email_data = []

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

                    # Initialize the email content to store
                    email_content = {
                        "Subject": subject,
                        "From": from_,
                        "Body": ""
                    }

                    # If the email message is multipart
                    if msg.is_multipart():
                        for part in msg.walk():
                            # Check the content type
                            content_type = part.get_content_type()
                            content_disposition = str(part.get("Content-Disposition"))

                            # If it's text, decode the body
                            if content_type == "text/plain" and "attachment" not in content_disposition:
                                try:
                                    body = part.get_payload(decode=True).decode("utf-8")
                                except UnicodeDecodeError:
                                    body = part.get_payload(decode=True).decode("iso-8859-1", errors="ignore")

                                # Clean the body to remove problematic characters
                                body = body.encode('latin1', 'replace').decode('latin1')

                                # Add body to the email content
                                email_content["Body"] = body

                    else:
                        # If the email is not multipart, just extract the payload
                        try:
                            body = msg.get_payload(decode=True).decode("utf-8")
                        except UnicodeDecodeError:
                            body = msg.get_payload(decode=True).decode("iso-8859-1", errors="ignore")

                        # Clean the body to remove problematic characters
                        body = body.encode('latin1', 'replace').decode('latin1')

                        # Add body to the email content
                        email_content["Body"] = body

                    # Append the email data to the list
                    email_data.append(email_content)

        # Close the connection and logout
        imap.close()
        imap.logout()

        # Convert email data to JSON and return
        return json.dumps(email_data, indent=4)

    except Exception as e:
        return json.dumps({"error": str(e)})
# import imaplib
# import email
# from email.header import decode_header
# import json

# def fetch_emails(username, password):
#     try:
#         # Connect to the Gmail IMAP server
#         imap = imaplib.IMAP4_SSL("imap.gmail.com")

#         # Login to the account
#         imap.login(username, password)

#         # Select the mailbox (e.g., "inbox")
#         imap.select("inbox")

#         # Search for all emails (you can also filter using 'UNSEEN', 'FROM', etc.)
#         status, messages = imap.search(None, "ALL")

#         # Convert message numbers from byte string to a list of integers
#         message_ids = messages[0].split()

#         # Limit to the first 10 emails
#         first_ten_emails = message_ids[:10]

#         # Prepare a list to store email data
#         email_data = []

#         # Fetch and display each of the first 10 emails
#         for num in first_ten_emails:
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

#                     # Initialize the email content to store
#                     email_content = {
#                         "Subject": subject,
#                         "From": from_,
#                         "Body": ""
#                     }

#                     # If the email message is multipart
#                     if msg.is_multipart():
#                         for part in msg.walk():
#                             # Check the content type
#                             content_type = part.get_content_type()
#                             content_disposition = str(part.get("Content-Disposition"))

#                             # If it's text, decode the body
#                             if content_type == "text/plain" and "attachment" not in content_disposition:
#                                 try:
#                                     body = part.get_payload(decode=True).decode("utf-8")
#                                 except UnicodeDecodeError:
#                                     body = part.get_payload(decode=True).decode("iso-8859-1", errors="ignore")

#                                 # Clean the body to remove problematic characters
#                                 body = body.encode('latin1', 'replace').decode('latin1')

#                                 # Add body to the email content
#                                 email_content["Body"] = body

#                     else:
#                         # If the email is not multipart, just extract the payload
#                         try:
#                             body = msg.get_payload(decode=True).decode("utf-8")
#                         except UnicodeDecodeError:
#                             body = msg.get_payload(decode=True).decode("iso-8859-1", errors="ignore")

#                         # Clean the body to remove problematic characters
#                         body = body.encode('latin1', 'replace').decode('latin1')

#                         # Add body to the email content
#                         email_content["Body"] = body

#                     # Append the email data to the list
#                     email_data.append(email_content)

#         # Close the connection and logout
#         imap.close()
#         imap.logout()

#         # Convert email data to JSON and return
#         return json.dumps(email_data, indent=4)

#     except Exception as e:
#         return json.dumps({"error": str(e)})
