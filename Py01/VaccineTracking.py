# Importing libraries
import time
import hashlib
from urllib.request import urlopen, Request
import smtplib

def send_email():
    # creates SMTP session
    s = smtplib.SMTP('smtp.gmail.com', 587)
    # start TLS for security
    s.starttls()
    # Authentication
    s.login("eprojectx1", "L1bertyx1")

    sender = "eprojectx1@gmail.com"
    receiver = "thao1901@gmail.com"
    # message to be sent

    message = "Vaccine check "

    # sending the mail
    s.sendmail(sender, receiver, message)
    # terminating the session
    s.quit()

# setting the URL you want to monitor
url = Request('https://mytest.gatech.edu/vaccine-schedule',
              headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) '
                                     'AppleWebKit/537.36 (KHTML, '
                                     'like Gecko) Chrome/39.0.2171.95 Safari/537.36'})


# to perform a GET request and load the
# content of the website and store it in a var
response = urlopen(url).read()

# to create the initial hash
currentHash = hashlib.sha224(response).hexdigest()
print("running")
# time.sleep(5)
while True:
    try:
        # perform the get request and store it in a var
        response = urlopen(url).read()

        # create a hash
        currentHash = hashlib.sha224(response).hexdigest()

        # wait for 30 seconds
        time.sleep(30)

        # perform the get request
        response = urlopen(url).read()

        # create a new hash
        newHash = hashlib.sha224(response).hexdigest()

        # check if new hash is same as the previous hash
        if newHash == currentHash:
            print("still the same")

            continue

        # if something changed in the hashes
        else:
            # notify
            print("----------------------- Slot available -----------------------")
            send_email()
            print("sent")
            # again read the website
            response = urlopen(url).read()

            # create a hash
            currentHash = hashlib.sha224(response).hexdigest()

            # wait for 30 seconds
            time.sleep(30)
            continue

    # To handle exceptions
    except Exception as e:
        print(e)

