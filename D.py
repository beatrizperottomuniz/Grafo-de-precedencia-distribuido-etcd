import etcd3
import time
import random

def esperar_chave(client, chave):
    """Aguarda uma chave aparecer no etcd sem espera ocupada.
    Se a chave já existir quando chegarmos aqui, retorna imediatamente."""
    valor, _ = client.get(chave)
    if valor is not None:
        return  # já está pronta

    events, cancel = client.watch(chave)
    for event in events:
        if isinstance(event, etcd3.events.PutEvent):
            cancel()
            break

def main():
    client = etcd3.client(host='localhost', port=2379)

    print("Aguardando")

    # Aguarda B terminar (sem espera ocupada)
    esperar_chave(client, 'done/B')

    # Aguarda C terminar (sem espera ocupada)
    esperar_chave(client, 'done/C')

    limite = random.randint(10, 20)

    for i in range(1, limite + 1):
        print(i)
        time.sleep(1)

    print("Fim")

if __name__ == '__main__':
    main()
