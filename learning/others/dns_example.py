import socket
import dns.resolver
import datetime


#import traceback
# https://github.com/rthalley/dnspython
# https://dnspython.readthedocs.io/en/latest/resolver-class.html
# https://dnspython.readthedocs.io/en/latest/resolver-class.html#dns.resolver.Answer

def build_record(dns_name, address, connected, duration, error):
    if error:
        return {
            'dns': dns_name,
            'address': address,
            'connected': connected,
            'duration_microseconds': duration,
            'error': error
        }
    else:
        return {
            'dns': dns_name,
            'address': address,
            'connected': connected,
            'duration_microseconds': duration
        }


def verify_ip(dns_name, host, port):
    can_connect = False
    ct = datetime.datetime.now()
    error = ''
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        if s.connect_ex((host, port)) == 0:
            can_connect = True
        s.shutdown(socket.SHUT_WR)
        s.close()
    except Exception as ex:
        # traceback.print_exc()
        error = ex.msg
    duration = datetime.datetime.now() - ct
    return build_record(dns_name, f'{host}:{port}', can_connect, duration.microseconds, error)


def verify_dns(dns_name, port):
    result = []
    try:
        res = dns.resolver.resolve(dns_name, 'A')
        for e in res.response.errors:
            print(f'error: {e}')

        ips = [item.address for answer in res.response.answer for item in answer if item.rdtype == dns.rdatatype.RdataType.A]

        for ip in ips:
            result.append(verify_ip(dns_name, ip, port))
    except Exception as ex:
        # traceback.print_exc()
        result.append(
            build_record(dns_name, '', False, 0, ex.msg)
        )
    return result


data = verify_dns('www.yahoo.com', 80)
print(data)
