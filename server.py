import socket, cv2, pickle, struct ,imutils
server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host_name  = socket.gethostname()
host_ip = socket.gethostbyname(host_name)
port = 10000
socket_address = (host_ip,port)
server_socket.bind(socket_address)
server_socket.listen(5)
print("LISTENING AT:",socket_address)

while True:
    client_socket,addr = server_socket.accept()
    print('GOT CONNECTION FROM:',addr)
    if client_socket:
        cap = cv2.VideoCapture(0)

        while(cap.isOpened()):
            ret,video = cap.read()
            video = imutils.resize(video,width=720)
            a = pickle.dumps(video)
            message = struct.pack("Q",len(a))+a
            
            client_socket.sendall(message)
            cv2.imshow('TRANSMITTING VIDEO',video)
            key = cv2.waitKey(1) & 0xFF
           
            if key == ord('q'):
                client_socket.close()
cv2.destroyAllWindows()