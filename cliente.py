import time
import socket
import random

def main():  
  while True:
    # Cria um socket para se conectar com o servidor 
    cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
      # Tenta se conectar com o servidor na porta 8080
      cliente.connect(('localhost', 8080))
    except:
      return print('\nHouve uma falha ao se conectar com o servidor')
    print('\nConexão realizada com sucesso')

    # Gera dois números aleatórios entre 1 e 99
    numero1 = random.randint(1, 99)
    numero2 = random.randint(1, 99)

    # Gera uma prioridade aleatória entre 1 e 3
    prioridade = random.randint(1, 3)
    if prioridade < 1 or prioridade > 3:
      print("Prioridade inválida. Usando prioridade 1")
      prioridade = 1

    # Gera um PID aleatório entre 1000 e 4999
    pid = random.randint(1000, 4999)

    # Envia os dados para o servidor
    cliente.send(f"{numero1},{numero2},{prioridade},{pid}".encode('utf-8'))
    print(f"Enviando solicitação - P{prioridade} PID {pid}: {numero1} + {numero2}")

    # Encerra a conexão com o servidor
    cliente.close()

    # Espera 2 segundos para enviar uma nova solicitação
    time.sleep(2)      

main()