import socket
import time
from socket import *
from threading import Thread


class MyClient:
    server_port = 50000  # Port for the server
    bufsize = 1024  # Set maximum bufsize
    host = input("Enter Server-IP Address: ").replace(" ", "")  # Set IP of host
    name = input("Set name: ").capitalize().replace(" ", "")  # Set up a custom name

    def __init__(self):
        self.data_recv = None  # Storage for received messages
        self.data_send = None  # Storage for sent messages

        self.socket_connection = socket(AF_INET, SOCK_STREAM)  # Create IpV4-TCP/IP-socket

        self.thread_recv = Thread(target=self.worker_recv)  # Setup thread for receiving messages
        self.thread_send = Thread(target=self.worker_send)  # Setup thread for sending messages

        self.runtime = 30  # Setup how long the connection should stay alive

        self.socket_connection.connect((self.host, self.server_port))  # Connect to the server via IP and port

        print(f"Connected to Server: '{self.host}'.")

        self.exit = False  # Initiate boolean to end it all

        self.thread_recv.start()  # Start thread to receive messages
        self.thread_send.start()  # Start thread to send messages

    # Function to receive messages
    def worker_recv(self):
        while not self.exit:
            try:
                self.data_recv = self.socket_connection.recv(self.bufsize)
                if self.data_recv:
                    print(self.data_recv)
            except Exception as e:  # Catch error and print
                print(f"Error in receiving message: {e}")

    # Function to send messages
    def worker_send(self):
        while not self.exit:
            try:
                # Setup sendable data for the server which displays information about the client cpu frequency
                self.data_send = input()  # Send custom text message to server
                print(f"You sent: '{self.data_send}'.")  # Printing custom text message
                if self.data_send.lower() == "exit":
                    # Execute stop_connection() on keyword "exit"
                    self.stop_connection()  # Doesn't work
                else:
                    # Format the data to a nice string
                    self.data_send = f"{self.name}: '{self.data_send}', still running for {self.runtime}."

                    # Send the server the data_send string
                    self.socket_connection.send(self.data_send.encode())

                    # Lower the runtime
                    self.runtime -= 1

                    # Sleep for a second
                    time.sleep(1)
            except Exception as e:  # Catch error and print
                print(f"Error occurred in sending message: {e}")

    # Function to stop the connection
    def stop_connection(self):
        self.exit = True  # Stop everything that depends on exit
        self.thread_recv.join()  # Stop thread after function is executed completely
        print("Stopped 'thread_recv'.")
        self.thread_send.join()  # Stop thread after function is executed completely
        print("Stopped 'thread_send'.")
        self.socket_connection.shutdown(socket.SHUT_RDWR)  # Shutdown the socket
        print("Shutting down...")
        self.socket_connection.close()  # Close socket
        print("Executing stop_connection() is done.")  # Debug
