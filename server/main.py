from server import MyServer


# Function to set up the socket and start our server
def start_server():
    server = MyServer()

    while server.runtime:
        pass
    server.stop_connection()


if __name__ == "__main__":
    start_server()
