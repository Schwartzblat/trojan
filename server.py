import socket

mode = input("enter your IP address or press ENTER to skip: ")
if not len(mode) > 4:
    mode = "normal"
while True:
    try:
        if mode == "normal":
            HOST = socket.gethostbyname(socket.gethostname())
        else:
            HOST = mode
        PORT = 9090
        print(HOST)
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.bind((HOST, PORT))

        server.listen()

        client, address = server.accept()

        while True:
            print(f"Connected to {address}")
            while True:
                command = input("enter a command: ")
                if len(command) > 2:
                    break
                print("please enter valid command")
            client.send(command.encode("utf-8"))
            print(client.recv(32768).decode("utf-8"))
    except:
        print("error")
