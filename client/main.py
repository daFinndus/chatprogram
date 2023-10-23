from client import MyClient


# Function to set up the socket and connect to the server
def start_client():
    client = MyClient()
    
    while client.runtime:
        pass
    client.stop_connection()


if __name__ == "__main__":
    start_client()
