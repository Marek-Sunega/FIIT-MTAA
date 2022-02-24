import sipfullproxy
import socketserver

HOST, PORT = '0.0.0.0', 5060


def main():
    server = socketserver.UDPServer((HOST, PORT), sipfullproxy.UDPHandler)
    server.serve_forever()


if __name__ == "__main__":
    main()
