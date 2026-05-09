#!/usr/bin/env python3
import etcd3
import time
import random


client = etcd3.client(host='localhost', port=2379)

# lease 60 s = as chaves expiram automaticamente
lease = client.lease(60)

limite = random.randint(10, 20)

for i in range(1, limite + 1):
    print(i)
    time.sleep(1)

print("Libera B e C")
client.put('ready/B', '1', lease=lease)
client.put('ready/C', '1', lease=lease)
print("Fim")

