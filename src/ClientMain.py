import python.connection.SocketClientClass as cl

if __name__ == "__main__":
    Client = cl.SocketClientClass(2040, 8080)
    Client.Client_ON()
