from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread
import time
from person import Person

HOST = 'localhost'
PORT = 5500
BUFSIZ = 512
ADDR = (HOST, PORT)
MAX_CONNECTION = 10

persons = []

SERVER = socket(AF_INET, SOCK_STREAM)
SERVER.bind(ADDR)


def broadcast(msg, name):
    for person in persons:
        client = person.client
        client.send(bytes(name, "utf8") + msg)


def client_communication(person):
    client = person.client

    # get person's name
    name = client.recv(BUFSIZ).decode("utf8")
    person.set_name(name)
    msg = bytes(f"{name} has joined the chat!", "utf8")
    broadcast(msg, "") # broadcast welcom message

    while True:
        try:
            msg = client.recv(BUFSIZ)
            print(f"{name}: ", msg.decode("utf8"))
            if msg == bytes("{quit}", "utf8"):
                # client.send(bytes("{quit}", "utf8"))
                client.close()
                persons.remove(person)
                broadcast(bytes(f"{name} has left the chat...", "utf8"), "")
                print(f"[DISCONNECTED] {name} disconnected")
                break
            else:
                broadcast(msg, name + ": ")
        except Exception as e:
            print("[EXCEPTION]", e)
            break


def wait_for_connection():
    while True:
        try:
            client, addr = SERVER.accept()
            person = Person(addr, client)
            persons.append(person)
            print(f"[CONNECTION] {addr} connected to the server at {time.time()}")
            Thread(target=client_communication, args=(person,)).start()
        except Exception as e:
            print("[FAILURE", e)
            break

    print("SERVER CRASHED")


if __name__ == "__main__":
    SERVER.listen(MAX_CONNECTION)
    print("[STARTED] Waiting for connection...")
    ACCEPT_THREAD = Thread(target=wait_for_connection)
    ACCEPT_THREAD.start()
    ACCEPT_THREAD.join()
    SERVER.close()