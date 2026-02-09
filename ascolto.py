import socket

def main():

    server_socket = socket.socket()
    host = '127.0.0.1'
    port= 6364
    server_socket.bind ((host, port))
    server_socket.listen (1)

    f = open('logfile.txt', "w")

    f.write (f"server listening on {host} : {port}\n")
    richiesta = ''
    for i in range (10):
        conn, addr = server_socket.accept()
        f.write(f"connected by {addr}\n")

        try:
            while True:
                data = conn.recv(1024)
                if not data:
                    break    
                else:
                    richiesta= data.decode()
                    if richiesta == 'SHUTDOWN':
                        exit()
                    else:
                        risposta = f"ho ricevuto il messaggio: {richiesta}\n"
                        f.write(risposta)
                        conn.sendall(risposta.encode())

        finally:
            conn.close()
        if richiesta == 'SHUTDOWN':
            break
    f.close()
    server_socket.close()


if __name__ == "__main__":
    main()