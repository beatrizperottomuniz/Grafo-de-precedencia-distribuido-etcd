import etcd3
import time
import random

def main():
    client = etcd3.client(host='localhost', port=2379)

    print("Aguardando")

    # watch_once bloqueia até receber exatamente um evento na chave
    valor, _ = client.get('ready/C')
    if valor is None:
        client.watch_once('ready/C')

    limite = random.randint(10, 20)

    for i in range(1, limite + 1):
        print(i)
        time.sleep(1)

    lease = client.lease(60)
    print("Liberando D")
    client.put('done/C', '1', lease=lease)
    print("Fim")

if __name__ == '__main__':
    main()
