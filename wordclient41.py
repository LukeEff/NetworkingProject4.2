import socket
import datetime
import time

def system_seconds_since_1900():
    """
    The time server returns the number of seconds since 1900, but Unix
    systems return the number of seconds since 1970. This function
    computes the number of seconds since 1900 on the system.
    """

    # Number of seconds between 1900-01-01 and 1970-01-01
    seconds_delta = 2208988800

    seconds_since_unix_epoch = int(datetime.datetime.now().strftime("%s"))
    seconds_since_1900_epoch = seconds_since_unix_epoch + seconds_delta

    return seconds_since_1900_epoch

s = socket.socket()

# Connect to gov time server
host = 'time.nist.gov'
port = 37
s.connect((host, port))

# Receive the time
NISTepoch_encoded = s.recv(4)
print(s.recv(4))
time.sleep(3)
NISTepoch = int.from_bytes(NISTepoch_encoded, "big")
s.close()

print('NIST time:', NISTepoch)
print('System NIST time:', system_seconds_since_1900())
