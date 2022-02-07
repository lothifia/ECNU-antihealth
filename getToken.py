# -*-coding:utf-8-*-
import hashlib

def get_token(port_name: str, port_number: str):
    string = port_name + port_number + 'ecnu1024'
    return hashlib.md5(string.encode('utf-8')).hexdigest()
