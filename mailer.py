import smtplib 

class Mailer():
    @staticmethod
    def send_mail(subject, body):
        server = smtplib.SMTP('SMTP.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.ehlo()
    
        server.login('hollyjanecooperr@gmail.com', 'pqqqzufgzqsybcni')
        msg = f" Subject{subject} \n\n{body} "
        success = False
    
        try:
            server.sendmail(
            'hollyjanecooperr@gmail.com',
            'holly_cooper@live.com.au',
            msg
            )
            print('Email has been sent! :-)')
            success = True
        except:
            print('Something wrong - no email sent')
        finally:
            #closing server connection
            server.quit()
    
        return success
  