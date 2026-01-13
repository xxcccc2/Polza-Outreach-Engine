"""
Проверка MX-записей email-доменов
pip install dnspython
"""

import dns.resolver
import sys

def check_mx(email: str) -> str:
    """Проверяет MX-записи домена"""
    try:
        domain = email.split('@')[1]
    except IndexError:
        return "MX-записи отсутствуют или некорректны"
    
    try:
        mx = dns.resolver.resolve(domain, 'MX')
        return "домен валиден" if mx else "MX-записи отсутствуют или некорректны"
    except dns.resolver.NXDOMAIN:
        return "домен отсутствует"
    except:
        return "MX-записи отсутствуют или некорректны"


def main():
    # Из файла или через запятую
    if len(sys.argv) < 2:
        print("python 1_email_checker.py emails.txt")
        print("python 1_email_checker.py \"a@gmail.com,b@fake.xyz\"")
        return
    
    arg = sys.argv[1]
    emails = open(arg).read().splitlines() if arg.endswith('.txt') else arg.split(',')
    
    for email in emails:
        email = email.strip()
        if email:
            print(f"{email} — {check_mx(email)}")


if __name__ == "__main__":
    main()
