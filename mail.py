import base64
import datetime
import argparse
import sys

import yagmail

from argparse import ArgumentParser


def parse_args(args):
    arg_parser = ArgumentParser(description="Used for sending alert emails through GMail. "
                                            "Using yagmail(not official GMail API) Python library "
                                            "for GMail connectivity.")

    arg_parser.add_argument(
        "--subject", "-s", default='yagmail alert', required=False,
        help="mail subject."
    )

    arg_parser.add_argument(
        "--to", "-t", required=False,
        help="mail receiver. To: header value"
    )

    arg_parser.add_argument('--infile', '-i',
                            default=sys.stdin,
                            required=False,
                            type=argparse.FileType('r'),
                            nargs='?',
                            help="mail receiver. To: header value"
                            )

    parsed = arg_parser.parse_args(args)
    return parsed


def main():
    args = parse_args(sys.argv[1:])
    test_send()
    # test_stdin(args)
    # register()


def test_stdin(args):
    print('Enter mail body (finish with ^+D):')
    mail_body = args.infile.read()
    send_to(args.to, args.subject, mail_body)


def test_send():
    # https://stackoverflow.com/questions/60956725/send-email-with-gmail-python
    send('Testing Yagmail ' + str(datetime.datetime.now()), 'Hurray, it worked!')
    print("Email sent successfully")


# def register():
#     yagmail.register(dec(USER_B), dec(PASS_B))
#     print('register successful')


def test_dec():
    # encoded = base64.b64encode(bytes(string, 'utf-8'))
    # print('encoded', encoded)
    decoded = dec(DEFAULT_REC_B)
    print(str(decoded))


def dec(bytes_str):
    return base64.b64decode(bytes_str).decode('utf-8')


USER_B = b'c3Vw'
PASS_B = b'bGF'
DEFAULT_REC_B = b'dG9'


def send(subject, contents):
    send_to(dec(DEFAULT_REC_B), subject, contents)


def send_to(to, subject, contents):
    yag = yagmail.SMTP(user=dec(USER_B), password=dec(PASS_B))
    yag.send(to=to, subject=subject, contents=contents)


if __name__ == "__main__":
    main()
