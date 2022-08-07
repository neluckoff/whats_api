import os
import platform
from whatsapp.user import User
from whatsapp.client import Client
import re
import phonenumbers
import pywhatkit

if __name__ == '__main__':
    client = Client()
    client.send_image()
