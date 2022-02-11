# -*-coding:utf-8-*-
from hashlib import md5

def get_token(port_name: str, port_number: str):
    string = port_name + port_number + 'ecnu1024'
    return md5(string.encode('utf-8')).hexdigest()
