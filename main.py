# Importar as bibliotecas necessárias para o funcionamento do programa
import hashlib, base64


# Definir uma função que codifica as senhas
def codificar_senha(senha):
  senha_encoded = senha.encode("utf-8")
  digest = hashlib.sha512(senha_encoded).digest()
  digest_b64_encoded = base64.b64encode(digest)
  digest_b64_encoded_utf8_decoded = digest_b64_encoded.decode("utf-8")
  return digest_b64_encoded_utf8_decoded


# Definir uma lista que organiza uma lista
def organizar (v):
  limpeza = remove_repetidos (v)
  alfabetica = quicksort (limpeza)
  return alfabetica


# Definir uma função que ordena uma lista
def quicksort(lst):
    if not lst:
        return []
    return (quicksort([x for x in lst[1:] if x <  lst[0]])
            + [lst[0]] +
            quicksort([x for x in lst[1:] if x >= lst[0]]))


# Definir uma função que remove elementos repetidos de uma lista
def remove_repetidos(lista):
    l = []
    for i in lista:
        if i not in l:
            l.append(i)
    l.sort()
    return l


# Definir as contantes de texto a serem printadas durante o programa
cabecalho = """
PROJETO: Quebra de Senhas
Alunos:
Bruno Gustavo Rocha; TIA: 32215029
Murilo Ramos do Nascimento; TIA: 32271166
"""


# Definir as constantes a serem usadas durante o programa
nome = []
senhas_codificadas = []
senhas_decodificadas = []
senhas_codigo = []
how_to_forget_me = []
teste = 0


# Printar o cabeçalho do jogo, com identificações
print(f"{cabecalho}\n\n\n")
print("#######    H A C K E A N D O    #######\n")
print("# Vamos descobrir as senhas? Por favor, aguarde")
print("\n\n")


# Abrir os arquivos
lista_palavras = open("palavras.txt", "r")
lista_senhas = open("usuarios_senhas_decodificadas.txt", "r")
senhas_sucesso = open("senhas_quebradas.txt", "w")
senhas_fracasso = open("senhas_nao_quebradas.txt", "w")


# Transformar a lista das palavras em um array onde cada palavra é um elemento
palavras = [linha.strip("\n") for linha in lista_palavras]


# Transformar a lista de senhas codificadas em um array onde cada senha é um elemento
x = lista_senhas.readlines()
for i in range(len(x)):
  l = x[i].rstrip().split(':')
  nome.append(l[0])
  senhas_codigo.append(l[1])


# Listar todas as possibilidades com 1 palavra;
  # Codificar cada possibilidade;
  # Checar se está no banco de dados das senhas;
    # Colocar na lista "senhas_decodificadas" se a senha estiver igual a codificada;
    # Caso contrário, colocar na lista "senhas_codificadas".
for v in range (len (palavras)):
  aux = str (palavras [v])
  codificar = codificar_senha (aux)
  for i in range (len (senhas_codigo)):
    if codificar == senhas_codigo [i]:
      senhas_decodificadas.append (f"{nome [i]} = {aux}")
    else:
      senhas_codificadas.append (f"{nome [i]}:{senhas_codigo [i]}")
      

  # Listar todas as possibilidades com 2 palavras;
    # Codificar cada possibilidade;
    # Checar se está no banco de dados das senhas;
      # Colocar na lista "senhas_decodificadas" se a senha estiver igual a codificada;
      # Caso contrário, colocar na lista "senhas_codificadas".

  for w in range (len (palavras)):
    aux = str (palavras [v]) + " " + str (palavras [w])
    codificar = codificar_senha (aux)
    for i in range (len (senhas_codigo)):
      if codificar == senhas_codigo [i]:
        senhas_decodificadas.append (f"{nome [i]} = {aux}")
      else:
        senhas_codificadas.append (f"{nome [i]}:{senhas_codigo [i]}")
        

    # Listar todas as possibilidades com 3 palavras;
      # Codificar cada possibilidade;
      # Checar se está no banco de dados das senhas;
        # Colocar na lista "senhas_decodificadas" se a senha estiver igual a codificada;
        # Caso contrário, colocar na lista "senhas_codificadas".
        
    for x in range (len (palavras)):
      aux = str (palavras [v]) + " " + str (palavras [w]) + " " + str (palavras [x])
      codificar = codificar_senha (aux)
      for i in range (len (senhas_codigo)):
        if codificar == senhas_codigo [i]:
          senhas_decodificadas.append (f"{nome [i]} = {aux}")
        else:
          senhas_codificadas.append (f"{nome [i]}:{senhas_codigo [i]}")
          

      # Listar todas as possibilidades com 4 palavras;
        # Codificar cada possibilidade;
        # Checar se está no banco de dados das senhas;
          # Colocar na lista "senhas_decodificadas" se a senha estiver igual a codificada;
          # Caso contrário, colocar na lista "senhas_codificadas".
      
      for y in range (len (palavras)):
        aux = str (palavras [v]) + " " + str (palavras [w]) + " " + str (palavras [x]) + " " + str (palavras [y])
        codificar = codificar_senha (aux)
        for i in range (len (senhas_codigo)):
          if codificar == senhas_codigo [i]:
            senhas_decodificadas.append (f"{nome [i]} = {aux}")
          else:
            senhas_codificadas.append (f"{nome [i]}:{senhas_codigo [i]}")

        # Listar todas as possibilidades com 5 palavras;
          # Codificar cada possibilidade;
          # Checar se está no banco de dados das senhas;
            # Colocar na lista "senhas_decodificadas" se a senha estiver igual a codificada;
            # Caso contrário, colocar na lista "senhas_codificadas".
        
        for z in range (len (palavras)):
          aux = str (palavras [v]) + " " + str (palavras [w]) + " " + str (palavras [x]) + " " + str (palavras [y]) + " " + str (palavras [z])
          codificar = codificar_senha (aux)
          for i in range (len (senhas_codigo)):
            if codificar == senhas_codigo [i]:
              senhas_decodificadas.append (f"{nome [i]} = {aux}")
            else:
              senhas_codificadas.append (f"{nome [i]}:{senhas_codigo [i]}")


# Limpar a lista "senhas_codificadas"
fracassou = organizar (senhas_codificadas)


# Colocar os elementos da lista "senhas_codificadas" no arquivo "senhas_não_quebradas.txt"
for i in fracassou:
  senhas_fracasso.write ("%s\n" % i)


# Limpar a lista "senhas_decodificadas"
acertou = organizar (senhas_decodificadas)


# Colocar os elementos da lista "senhas_decodificadas" no arquivo "senhas_quebradas.txt"
for i in acertou:
  senhas_sucesso.write ("%s\n" % i)

  
# Mostrar para o usuário que o programa terminou o processamento
print ("## Processo finalizado! Por favor, cheque os arquivos de senhas quebradas e de senhas não quebradas")

# Fechar os arquivos
lista_palavras.close()
lista_senhas.close()
senhas_sucesso.close()
senhas_fracasso.close()
