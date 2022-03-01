from sipfullproxy import *


def main():
    device_ip = socket.gethostbyname(socket.gethostname())
    print(f"SIP PROXY ip: {device_ip}")
    libsetup(device_ip)
    server = socketserver.UDPServer(get_address(), UDPHandler)
    server.serve_forever()


if __name__ == "__main__":
    main()
