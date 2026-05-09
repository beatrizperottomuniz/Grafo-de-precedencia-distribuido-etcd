#!/usr/bin/env python3
import etcd3
import time
import random


client = etcd3.client(host='localhost', port=2379)
print("Aguardando")

# watch_once bloqueia ate receber exatamente um evento na chave
valor, _ = client.get('ready/B')
if valor is None:
    client.watch_once('ready/B')

limite = random.randint(10, 20)

for i in range(1, limite + 1):
    print(i)
    time.sleep(1)

lease = client.lease(60)
print("Libera D")
client.put('done/B', '1', lease=lease)
print("Fim")

