#!/usr/bin/python3
"""Alta3 Research | rzfeeser@alta3.com
   Learning about Python SSH"""

import paramiko
import json

def read_connection_info(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)


def main():
    """Our runtime code that calls other functions"""
    connection_info_file = "connection.jason"

    credz = read_connection_info("/home/student/mycode/paramikosshrsa/connection.json")

    # harvest private key for all 3 servers
    mykey = paramiko.RSAKey.from_private_key_file("/home/student/.ssh/id_rsa")

    # loop across the collection credz
    for cred in credz:
        ## create a session object
        sshsession = paramiko.SSHClient()

        ## add host key policy
        sshsession.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        ## display our connections
        print("Connecting to... " + cred.get("un") + "@" + cred.get("ip"))

        ## make a connection
        sshsession.connect(hostname=cred.get("ip"), username=cred.get("un"), pkey=mykey)

        ## touch the file goodnews.everyone in each user's home directory
        sshsession.exec_command("touch /home/" + cred.get("un") + "/goodnews.everyone")

        ## list the contents of each home directory
        sessin, sessout, sesserr = sshsession.exec_command("ls /home/" + cred.get("un"))

        ## display output
        print(sessout.read().decode('utf-8'))
        
        results_file = open("results.log", "w")
        results_file.write(f"Results from {cred.get('un')}@{cred.get('ip')}:\n")
        results_file.write(output)
        results_file.write("\n\n")

        ## close/cleanup SSH connection
        sshsession.close()
     
    print("Thanks for looping with Alta3!")

main()

