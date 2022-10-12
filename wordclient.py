import sys
import socket

# How many bytes is the word length?
WORD_LEN_SIZE = 2

def usage():
    print("usage: wordclient.py server port", file=sys.stderr)

packet_buffer = b''

def get_next_word_packet(s):
    """
    Return the next word packet from the stream.

    The word packet consists of the encoded word length followed by the
    UTF-8-encoded word.

    Returns None if there are no more words, i.e. the server has hung
    up.
    """

    # Receive 5 bytes
    # Check size of word using head
    # Receive 5 bytes until buffer has all bytes
    # Split by that size
        # First half goes to local var
        # Second half reassigns buffer

    global packet_buffer

    packet_buffer += s.recv(5)

    # Exit condition if empty buffer
    if (packet_buffer == b''):
        return None

    desired_size = int.from_bytes(packet_buffer[:2], "big")
    desired_size_including_header = desired_size + 2
    # Add two so we account for the header
    while len(packet_buffer) < desired_size_including_header:
        # Add more bytes to the buffer
        packet_buffer += s.recv(5)
    
    word_packet = packet_buffer[:desired_size_including_header]
    packet_buffer = packet_buffer[desired_size_including_header:]

    return word_packet


def extract_word(word_packet):
    """
    Extract a word from a word packet.

    word_packet: a word packet consisting of the encoded word length
    followed by the UTF-8 word.

    Returns the word decoded as a string.
    """
    word_packet_body = word_packet[2:]
    return word_packet_body.decode()

# Do not modify:

def main(argv):
    try:
        host = argv[1]
        port = int(argv[2])
    except:
        usage()
        return 1

    s = socket.socket()
    s.connect((host, port))

    print("Getting words:")

    while True:
        word_packet = get_next_word_packet(s)

        if word_packet is None:
            break

        word = extract_word(word_packet)

        print(f"    {word}")

    s.close()

if __name__ == "__main__":
    sys.exit(main(sys.argv))
