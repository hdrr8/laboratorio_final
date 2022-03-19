from NBIOT.send_cmd import send_cmd
import serial
import json

from constants import MY_PHONE_PASS

def enter_pin(ser, response_history=[]):
    cmd_response = send_cmd("AT+CPIN?", ser, 6,  print_response=True)
    response_history.append(cmd_response)

    response_code = response_history[-1]["response"][1][0:-2] # [0:-2] to remove \r\n
    
    if response_code == "+CPIN: SIM PIN":
        cmd_response = send_cmd("AT+CPIN=" + MY_PHONE_PASS, ser, 8,  print_response=True, ms_of_delay_after=1000)
        response_history.append(cmd_response)
        response_status = response_history[-1]["status"]

        if response_status == "ERROR":
            status = "ERROR"
            message = "SIM PIN SENT AND ERROR"
        elif response_status == "OK":
            status = "OK"
            message = "SIM PIN SENT AND SUCCESS"
        else:
            status = "ERROR"
            message = "SIM PIN SENT AND UNFINISHED"
    elif response_code == "+CPIN: READY":
        status = "OK"
        message = "+CPIN: READY"
    else:
        print('==> SIM error with message ' + response_code)
        status = "ERROR"
        message = response_code
        
    return({"response_history": response_history, "status": status, "message": message})

def configure_modem(NBIOT_port):

    send_cmd("AT+CFUN=4", NBIOT_port,  print_response=True, ms_of_delay_after=100)
    send_cmd("AT+QCFG=\"nwscanmode\",3,1", NBIOT_port,  print_response=True, ms_of_delay_after=100)
    send_cmd("AT+QCFG=\"iotopmode\",1,1", NBIOT_port,  print_response=True, ms_of_delay_after=100)
    send_cmd("AT+CGDCONT= 1,\"IPV6\",\"internet.iot\","",0,0", NBIOT_port, print_final_response=False,ms_of_delay_after = 100)
    send_cmd("AT+CFUN=1", NBIOT_port,  print_response=True, ms_of_delay_after=100)

def cofigure_operator(NBIOT_port, response_history=[]):
    
    send_cmd("AT+COPS=1,2,\"74801\",9", NBIOT_port,  print_response=True, ms_of_delay_after=100)

def check_nbiot_conection(NBIOT_port, retries=3, response_history=[], custom_delay=2000):
    
    send_cmd("AT+CPIN?", NBIOT_port,  print_response=True, ms_of_delay_after=100)
    send_cmd("AT", NBIOT_port,  print_response=True, ms_of_delay_after=100)
    send_cmd("AT+CEREG?",NBIOT_port,  print_response=True, ms_of_delay_after=100)
    send_cmd("AT+QNWINFO",NBIOT_port,  print_response=True, ms_of_delay_after=100) #"CAT-NB1","74801","LTE BAND 3",1290
    send_cmd("AT+CGACT=1,1",NBIOT_port,  print_response=True, ms_of_delay_after=100) #/* Activo contexto PDP 1 a la red APN*///OK
    send_cmd("AT+CGPADDR=1",NBIOT_port,  print_response=True, ms_of_delay_after=100) #/* Pregunto por IP la asignada por al contexto PDP 1*///+CGPADDR: 1,167.108.195.136