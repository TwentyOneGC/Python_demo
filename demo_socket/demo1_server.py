import socket
sk = socket.socket()
address = ('127.0.0.1', 8888)
sk.bind(address)
sk.listen(5)
conn, addr = sk.accept()
accept_data = conn.recv(1024).decode('utf-8')
print('接收内容：{}   客户端端口：{}'.format(accept_data, addr[1]))
send_data = input('输入发送内容:')
conn.sendall(bytes(send_data.encode('utf-8')))
sk.close()