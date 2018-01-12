import socket
import struct
import json

host = ''
port = 9000

conn = socket.socket()
conn.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

conn.bind((host, port))
conn.listen(5)

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

conn, address = conn.accept()
# return_string = b'\x00\x00\x00\x03SSH'
return_string = "SSH"
print(conn.recv(4096))
print(return_string)
send_message(return_string)

# return_dict = {'username': username, 'password': password, 'hostname': socket.gethostname()}
# return_string = json.dumps(return_dict, sort_keys=True, indent=4, separators=(',', ': '))
# print(return_string)
# send_message(return_string)
# print(conn.recv(4096))

