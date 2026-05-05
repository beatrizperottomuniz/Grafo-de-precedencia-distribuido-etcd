import etcd3
import time
import random

def main():
    client = etcd3.client(host='localhost', port=2379)

    # Limpa chaves de execuções anteriores
    client.delete('ready/B')
    client.delete('ready/C')
    client.delete('done/B')
    client.delete('done/C')

    limite = random.randint(10, 20)

    for i in range(1, limite + 1):
        print(i)
        time.sleep(1)

    print("Liberando B e C")
    client.put('ready/B', '1')
    client.put('ready/C', '1')
    print("Fim")

if __name__ == '__main__':
    main()
