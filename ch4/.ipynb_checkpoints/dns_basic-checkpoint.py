import argparse, dns.resolver

def lookup(name):
    for qtype in 'A', 'AAAA', 'CNAME', 'MX', 'NS': # "type" of record
        answer = dns.resolver.resolve(name, qtype, raise_on_no_answer=False) # 에러는 스킵
        if answer.rrset is not None: # dnspython에서 rrset으로 결과 확인
            print(answer.rrset)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Resolve a name using DNS')
    parser.add_argument('name', help='name that you want to look up in DNS')
    lookup(parser.parse_args().name)
