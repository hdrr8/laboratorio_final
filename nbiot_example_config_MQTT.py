from datetime import datetime
from re import A
from time import sleep
from NBIOT.configuration import check_nbiot_conection, cofigure_operator, configure_modem
from NBIOT.send_cmd import send_cmd
from serial import Serial
from NBIOT.MQTT import   open_mqtt_network, connect_to_mqtt_server, publish_mqtt_message, close_mqtt_network, disconnect_to_mqtt_server


NBIOT_port = Serial(port='COM9', baudrate=115200, bytesize=8, parity='N', stopbits=1, timeout=5)

cmd_response = send_cmd("AT", NBIOT_port,  print_response=True, ms_of_delay_after=100)

#configure_modem(NBIOT_port)
OpenMQTT =  send_cmd('AT+QMTOPEN=0',"54.191.221.11",1883)

#cofigure_operator(NBIOT_port, response_history=[])

#check_nbiot_conection(NBIOT_port, retries=3, response_history=[], custom_delay=2000)

NBIOT_port.close()