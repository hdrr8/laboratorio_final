from datetime import datetime
from re import A
from time import sleep
from NBIOT.configuration import configure_modem
from NBIOT.send_cmd import send_cmd
from serial import Serial


NBIOT_port = Serial(port='COM9', baudrate=115200, bytesize=8, parity='N', stopbits=1, timeout=5)

cmd_response = send_cmd("AT", NBIOT_port,  print_response=True, ms_of_delay_after=100)


#response = start_up_nbiot(NBIOT_port)
#send_cmd("AT+CPIN?", NBIOT_port,  print_response=True, ms_of_delay_after=100)
#send_cmd("AT", NBIOT_port,  print_response=True, ms_of_delay_after=100)

#send_cmd("AT+CFUN=4", NBIOT_port,  print_response=True, ms_of_delay_after=100)
#send_cmd("AT+QCFG=\"nwscanmode\",3,1", NBIOT_port,  print_response=True, ms_of_delay_after=100)
#send_cmd("AT+QCFG=\"iotopmode\",1,1", NBIOT_port,  print_response=True, ms_of_delay_after=100)
#send_cmd("AT+CGDCONT=1,\"IP#V6\",\"internet.iot\",\"\",0,0", NBIOT_port,  print_response=True, ms_of_delay_after=100)
#send_cmd("AT+CFUN=1", NBIOT_port,  print_response=True, ms_of_delay_after=100)

#send_cmd("AT+COPS=1,2,\"74801\",9", NBIOT_port,  print_response=True, ms_of_delay_after=100)

#send_cmd("AT+CEREG?", NBIOTg_port,  print_response=True, ms_of_delay_after=100)
#send_cmd("AT+QNWINFO", NBIOT_port,  print_response=True, ms_of_delay_after=100)
#send_cmd("AT+CGACT=1,1", NBIOT_port,  print_response=True, ms_of_delay_after=100)
#send_cmd("AT+CGPADDR=1", NBIOT_port,  print_response=True, ms_of_delay_after=100)

#while True:

    #cmd_response = send_cmd("AT+CSQ", NBIOT_port, print_final_response=False)
    
    # m_of_delay = 
    # s_of_delay = m_of_delay/60

    #s_of_delay = 1

    #sleep(s_of_delay)

NBIOT_port.close()