from sipfullproxy import *


def main():
    print("Input ip of a device:")
    ip = input()
    libsetup(ip)
    server = socketserver.UDPServer(get_address(), UDPHandler)
    server.serve_forever()


if __name__ == "__main__":
    main()
