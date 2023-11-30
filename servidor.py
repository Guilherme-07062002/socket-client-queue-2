import time
import socket
import threading

# Função para imprimir a fila
def printQueue(dado):
  # Separa os dados da string
  numeros = dado.split(',')
  return f'(P{numeros[2]}) PID: {numeros[3]}'

# Função para processar a fila
def processQueue(request_queue):
  while True:
    if not len(request_queue) == 0:
      request = request_queue[0]
      numeros = request.split(',')
      print('----------------------------------------')

      # Imprime a fila
      print(f"Fila: {list(map(printQueue, list(request_queue)))}")
      request_queue.pop(0)
      print(f"Saindo da fila - (P{numeros[2]}) PID {numeros[3]}: {numeros[0]} + {numeros[1]} = {int(numeros[0]) + int(numeros[1])}")
      time.sleep(3)

def servidor():
  servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  servidor.bind(('127.0.0.1', 8080))
  servidor.listen()

  print("Servidor escutando 127.0.0.1 na porta 8080")        

  # Cria a fila de requisições
  request_queue = []
  # Cria a thread para processar a fila
  queue_thread = threading.Thread(target=processQueue, args=(request_queue,))
  # Inicia a thread
  queue_thread.start()

  while True:
    cliente, endereco = servidor.accept()
    # Recebe os dados do cliente
    data = cliente.recv(1024).decode('utf-8')
    # Envia uma mensagem de confirmação
    cliente.send("Conexão aceita".encode('utf-8'))
    # Adiciona os dados na fila
    request_queue.append(data)
    # Ordena a fila
    request_queue.sort(key=lambda x: x.split(',')[2], reverse=True)

servidor()