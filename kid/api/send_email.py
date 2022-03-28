import smtplib

MY_EMAIL = '<email>'
MY_PASSWORD = '<password>'


def send_data(name_of_receiver):
    with smtplib.SMTP('smtp.gmail.com') as smtp:
        smtp.starttls()
        smtp.login(
            user=MY_EMAIL,
            password=MY_PASSWORD
        )
        smtp.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=name_of_receiver,
            msg=f"Subject: Unknown\n\nYour child does not upload food images."
        )
