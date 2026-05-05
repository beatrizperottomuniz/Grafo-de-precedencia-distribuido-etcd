import etcd3
import time
import random

def main():
    client = etcd3.client(host='localhost', port=2379)

    print("Aguardando")

    # Bloqueia sem espera ocupada até a chave ready/B aparecer
    events, cancel = client.watch('ready/B')
    for event in events:
        if isinstance(event, etcd3.events.PutEvent):
            cancel()
            break

    limite = random.randint(10, 20)

    for i in range(1, limite + 1):
        print(i)
        time.sleep(1)

    print("Liberando D")
    client.put('done/B', '1')
    print("Fim")

if __name__ == '__main__':
    main()
