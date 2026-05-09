#!/usr/bin/env python3
import etcd3
import time
import random


client = etcd3.client(host='localhost', port=2379)
print("Aguardando")

valor, _ = client.get('done/B')
if valor is None:
    client.watch_once('done/B')

valor, _ = client.get('done/C')
if valor is None:
    client.watch_once('done/C')

limite = random.randint(10, 20)

for i in range(1, limite + 1):
    print(i)
    time.sleep(1)

print("Fim")
# limpar keys (deletando)
client.delete('ready/B')
client.delete('ready/C')
client.delete('done/B')
client.delete('done/C')

