from smtplib import SMTP
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

from send_email import send_mail
from get_data import get_gdp_data
from pretty_html_table import build_table

import pandas as pd

# https://dev.to/siddheshshankar/convert-a-dataframe-into-a-pretty-html-table-and-send-it-over-email-4663

def send_mail(body):

    message = MIMEMultipart()
    message['Subject'] = 'Top 5 Economies of the World!'
    message['From'] = '<sender>@gmail.com'
    message['To'] = '<receiver>@gmail.com'

    body_content = body
    message.attach(MIMEText(body_content, "html"))
    msg_body = message.as_string()

    server = SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(message['From'], 'Unique password')
    server.sendmail(message['From'], message['To'], msg_body)
    server.quit()

def get_gdp_data():
    """
    GDP data
    :return:
    """
    gdp_dict = {'Country': ['United States', 'China', 'Japan', 'Germany', 'India'],
                'GDP': ['$21.44 trillion', '$14.14 trillion', '$5.15 trillion', '$3.86 trillion', '$2.94 trillion']}
    data = pd.DataFrame(gdp_dict)
    return data


def send_country_list():
    gdp_data = get_gdp_data()
    output = build_table(gdp_data, 'blue_light')
    send_mail(output)
    return "Mail sent successfully."


send_country_list()