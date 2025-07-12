import socket
Host='192.168.56.1'
port=9090

server =socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((Host, port))

server.listen(5)
while True:
  communication_socket, address  =server.accept()
  print(f"Connected to{address}")
  message=communication_socket.recv(1024).decode('utf-8')
  print(f"message from client is:{message} ")
  communication_socket.send("got your message,thank you".encode('utf-8'))
  communication_socket.close()
  print(f"connection with{address}ended")
  printf("my name is Akankshya das")