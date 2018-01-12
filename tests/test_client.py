import socket
import struct
import json

conn = socket.socket()
conn.connect(("localhost", 9000))

username = "device-1"
password = "password-1"

def send_message(output_str):
    """ Sends message to the core
     :param output_str: string message that will go to the core
    """
    print("will send this " + str(output_str))
    byte_array_message = str.encode(output_str)
    # We are packing the lenght of the packet to unsigned big endian struct to make sure that it is always constant length
    conn.send(struct.pack('>I', len(byte_array_message)) + byte_array_message)

return_dict = {'username': username, 'password': password, 'hostname': socket.gethostname()}
return_string = json.dumps(return_dict, sort_keys=True, indent=4, separators=(',', ': '))
print(return_string)
send_message(return_string)
conn.send(b'')
conn.send(b'')
conn.send(b'')
conn.send(b'')
print(conn.recv(4096))

