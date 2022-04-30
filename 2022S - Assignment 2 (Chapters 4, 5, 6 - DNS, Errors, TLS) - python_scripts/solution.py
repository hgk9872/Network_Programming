import json
import zlib
import socket
import ssl


class Solution():
    
    def special_bits(self, L=1, R=2, k=1):
        num = -2
        # Write your code between start and end for solution of problem 1
        # Start
        # 입력받은 범위에서, 작은 수부터 반복
        for x in range(L, R+1):
            if bin(x)[2:].count('1') == k: # 입력받은 k와 1의 개수가 같은 number가 나오면 최솟값
                num = x
                break
            elif x == R: # 범위의 마지막 숫자이고, count != k 인 경우
                num = -1
        # End
        return num

    def toggle_string(self, S):
        s = ""
        # Write your code between start and end for solution of problem 2
        # Start
        for ch in S:
            if ord(ch) >= 65 and ord(ch) <= 90: # 대문자를 소문자로 변환
                lower = ord(ch)+32 
                s = s + chr(lower)
            elif ord(ch) >= 97 and ord(ch) <= 122: #소문자를 대문자로 변환
                upper = ord(ch)-32
                s = s + chr(upper)   
        # End
        return s

    def send_message(self, message):
        message = self.to_json(message)
        message = self.encode(message)
        message = self.compress(message)
        return message

    def recv_message(self, message):
        message = self.decompress(message)
        message = self.decode(message)
        message = self.to_python_object(message)
        return message
    
    # String to byte
    def encode(self, message):
        # Write your code between start and end for solution of problem 3
        # Start
        message = message.encode()
        return message
        # End
        
    
    # Byte to string
    def decode(self,message):
        # Write your code between start and end for solution of problem 3
        # Start
        message = message.decode()
        return message
        # End 

    # Convert from python object to json string
    def to_json(self, message):
        # Write your code between start and end for solution of problem 3
        # Start
        message = json.dumps(message)
        return message
        # End 

    # Convert from json string to python object
    def to_python_object(self, message):
        # Write your code between start and end for solution of problem 3
        # Start
        message = json.loads(message)
        return message
        # End 
    
    # Returns compressed message 
    def compress(self, message):
        # Write your code between start and end for solution of problem 3
        # Start
        compressed = zlib.compress(message)
        return compressed
        # End 

    # Returns decompressed message
    def decompress(self, compressed_message):
        # Write your code between start and end for solution of problem 3
        # Start
        message = zlib.decompress(compressed_message)
        return message
        # End 


    def client(self, host, port, cafile=None):
        # Write your code between start and end for solution of problem 4
        # Start
        cert = "" # Variable to store the certificate received from server 
        cipher = "" # Variable to store cipher used for connection
        msg = "" # Variable to store message received from server
        
        context = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
        context.load_verify_locations('ssu.pem')
        
        raw_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        raw_sock.connect((host, port))
        print('Connected to host {!r} and port {}'.format(host, port))
        ssl_sock = context.wrap_socket(raw_sock, server_hostname=host)
        
        while True:
            data = ssl_sock.recv(1024)
            if not data:
                break
            msg = data


        # End
        return cert, cipher, msg

    

    
