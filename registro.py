import socket
import pickle

def main():

    server_socket = socket.socket()
    host = '127.0.0.1'
    
    try:
        f=open('utenti.dump', 'rb')
        utenti = pickle.load(f)
    except:
        utenti={'admin' : 'èsegreta'}
    finally:
        f.close()

    port= 7654
    server_socket.bind ((host, port))
    server_socket.listen (1)

    for i in range (5):
        conn, addr_p = server_socket.accept()
        print(f"connected by {addr_p}\n")
        #conn.sendall('Indicami il tuo Username'.encode())
        conn.sendall(b'Indicami il tuo Username: ')
        username=conn.recv(1024).decode()

        #print(f'il tuo Username é: {username}')

        conn.sendall(b'Indicami la tua Password: ')
        password=conn.recv(1024).decode()

        #print(f'la tua password é: {password}')
       
        if username == 'admin':
            if utenti[username] == password:
                conn.sendall(str(utenti).encode())
            else:
                conn.close()
                continue
        else:
            utenti[username] = password 

        conn.close
    server_socket.close()

    f=open('utenti.dump', 'wb')
    pickle.dump(utenti, f)
    f.close()

    #print(utenti)
    #for u , p in utenti.items():
    #    print(f"Utente: {u} Password: {p}")


if __name__ == "__main__":
    main()