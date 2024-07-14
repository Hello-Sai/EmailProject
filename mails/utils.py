from django.core.mail import EmailMessage

def mail_service(zipfile,email,screenshot,repository_link,cc='hr@themedius.ai'):
    body=f"""
                Hello Team,

                I hope this email finds you well. Please find below and attached the details of my assignment submission for the Google Form Automation task.

                GitHub Repository
                You can access the source code for this assignment on my GitHub repository: {repository_link}

                Approach and Methodology
                I have automated the process of submitting the Google Form using a Django Core Library.

                The Methodology performs the following steps:

                1. Generating a Gmail App Password:
                    To use Gmail SMTP, especially from a third-party app like Django, you often need to generate an "App Password" from your Google account:


                2. Using in Django Project
                    After setting up the .env file and configuring settings.py as shown above, Django will use these settings to send emails using Gmail SMTP securely.


                3. UrlConf Setup:  
                    Implement a Django view mapped to the homepage URL (/). Utilize utilities (utils.py) to handle form submission and screenshot capture.



                4. Email Sending: 
                    Utilize Django's email functionality to compose and send an email with both plain text and HTML content, including attachments of source code, documentation, and the 
                    captured screenshot.


                Attached Files
                1. Source Code: A zip file containing all the source code.
                2. Screenshot: A screenshot of the form submitted page.

                

                Thank you for your time and consideration.

                Best regards,
                Sai Kumar
                9515693255
            """

    mail = EmailMessage(subject='Python (Selenium) Assignment - Sai Kumar Dagudu',to=[email],cc=[cc],body=body)
    mail.attach_file(zipfile)
    mail.attach_file(screenshot)
    mail.send()