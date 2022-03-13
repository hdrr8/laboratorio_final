import serial

from send_cmd import send_cmd
from constants import MY_PHONE_PASS

DEFALUT_PRINT_RESPONSE = True
DEFAULT_TCP_CONNECT_ID = 0
DEFAULT_HOST_NAME = "54.191.221.113"
DEFAULT_PORT = 1883
DEFAULT_USERNAME = "topic"
DEFEULT_PASSWORD = "password o string secreto"

DEFAULT_TCP_CONNECT_ID = 0
DEFAULT_MSG_ID = 0
DEFAULT_QOS = 0
DEFAULT_RETAIN = 0
DEFAULT_TOPIC = "mychannel"


def open_mqtt_network(
    host_name=DEFAULT_HOST_NAME, 
    port=DEFAULT_PORT, 
    print_response=DEFALUT_PRINT_RESPONSE,
    ):
    '''
    Abrir conexion de red con el broker MQTT
    '''
    send_cmd('AT+QMTOPEN=0',"54.191.221.11",1883),

def connect_to_mqtt_server(
    ser, 
    tcp_connect_id=DEFAULT_TCP_CONNECT_ID, 
    username = DEFAULT_USERNAME,    
    password = DEFEULT_PASSWORD,
    print_response=DEFALUT_PRINT_RESPONSE,
    ):
    
    send_cmd('AT+QMTCONN=0',"54.191.221.11",1883),

def publish_mqtt_message(
    ser, 
    str_to_send,
    topic = DEFAULT_TOPIC,
    tcp_connect_id = DEFAULT_TCP_CONNECT_ID,
    msgID = DEFAULT_MSG_ID,
    qos = DEFAULT_QOS,
    retain = DEFAULT_RETAIN,
    print_response=DEFALUT_PRINT_RESPONSE
    ):
    
    send_cmd('AT+QMTPUB=0',"54.191.221.11",1883),

def close_mqtt_network(ser, tcp_connect_id=DEFAULT_TCP_CONNECT_ID, print_response=DEFALUT_PRINT_RESPONSE):
    send_cmd('AT+QMTCLOSE=0',"54.191.221.11",1883)


def disconnect_to_mqtt_server(ser,  print_response=DEFALUT_PRINT_RESPONSE):
    send_cmd('AT+QMTDISC=0',"54.191.221.11",1883)
    