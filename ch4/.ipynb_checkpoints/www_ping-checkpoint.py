#!/usr/bin/env python
# coding: utf-8
# %%

# %%


## 특정 호스트에 connect하여 'www' 서비스를 제공 하는지 확인하는 ping 코드

import argparse, socket, sys

def connect_to(hostname_or_ip):
    try:
        infolist = socket.getaddrinfo(
            hostname_or_ip, 'www', 0, socket.SOCK_STREAM, 0,
            socket.AI_ADDRCONFIG | socket.AI_V4MAPPED | socket.AI_CANONNAME
            )
    except socket.gaierror as e: # getaddrinfo 과정에서 발생하는 예외처리
        print('Name service failure:', e.args[1])
        sys.exit(1)
    
    info = infolist[0] # 보통 첫 번째 정보사용
    socket_args = info[0:3] # socket을 만들기 위한 3 items (family, type, proto)
    address = info[4] # connect를 위한 sockaddr정보 (IP, Port)
    s = socket.socket(*socket_args) # 개별적인 값(튜플)으로 파라미터 전달
    try:
        s.connect(address) #호스트에 연결
    except socket.error as e:
        print('Network failue:', e.args[1]) # connect과정에서 발생하는 에러 처리
    else:
        print('Success: host', info[3], 'is listening on port 80')
        
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Try connect to port 80')
    parser.add_argument('hostname', help='hostname that you want to connect')
    connect_to(parser.parse_args().hostname)

