#!/usr/bin/python3
""" this module displays the value of the X-Request-Id
variable found in the header of a response taken as cmd line arg """

if __name__ == '__main__':
    import sys
    import urllib.request as request_url

    url = sys.argv[1]
    with request_url.urlopen(url) as response:
        x_request_id = response.headers.get('X-Request-Id')
        print(x_request_id)
