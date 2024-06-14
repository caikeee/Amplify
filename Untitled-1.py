# def verificarmulti(arr):
#   if not arr:
#    return False
  
#   soma_total = sum(arr)
#   dobro = 2 * soma_total


#   for a in range(len(arr)): 
#     for b in range(len(arr)):
#       if arr[a] * arr[b] > dobro:
#         return True

#   return False
# arr = [3,5,7,5,4,]
# print(verificarmulti(arr))

# def SumMultiplier(arr):

#   if not arr:
#     return False

#   soma_total = sum(arr)
#   dobro = 2 * soma_total

#   for a in range(len(arr)):
#     for b in range(len(arr)):
#       if arr[a] * arr[b] > dobro:
#         return True
      
#   return False

# arr =[5,6,3,7,9,2]
# print(SumMultiplier(arr))

# def LongestWord(sen):
#   sen = re.sub(r'[^\w\s]', '', sen)
#   palavras = sen.split()
#   maiorpalavra = palavras[0]

#   for palavra  in palavras:
#     if len(palavra) > len(maiorpalavra):
#      maiorpalavra = palavra
  
#   return maiorpalavra

# sen =  "apenas testando a maior palavra"
# print("a palavra mais longa é: ",LongestWord(sen))





def LetterCount(frase):
    # Separar a frase em palavras
    palavras = frase.split()

    max_letras_repetidas = 0  
    palavra_com_max_repetidas = ""

    for palavra in palavras:
        # Contar as ocorrências de cada letra na palavra
        contagem_letras = {}
        for letra in palavra:
            if letra in contagem_letras:
                contagem_letras[letra] += 1
            else:
                contagem_letras[letra] = 1

        # Encontrar a letra mais repetida na palavra
        max_contagem = max(contagem_letras.values()) if contagem_letras else 0

        # Verificar se essa palavra tem mais letras repetidas do que as anteriores
        if max_contagem > max_letras_repetidas:
            max_letras_repetidas = max_contagem
            palavra_com_max_repetidas = palavra

    if max_letras_repetidas > 1:
        return palavra_com_max_repetidas
    else:
        return -1

# Exemplo de uso:
frase_exemplo = "Hoje é o melhor dia de todos toooooo eeeeeee!"
resultado = LetterCount(frase_exemplo)
print(resultado)  # Saída esperada: "melhor"


# def LetterCount(frase):
#   palavras = frase.split()
#   max_letras_repetidas = 0
#   maximorepetidas = ""

#   for palavra in palavras:
#         contagem_letras = {}
#         for letra in palavras:
#           if letra in contagem_letras:

#             contagem_letras[letra] += 1
#           else:
#             contagem_letras[letra] = 1
        
#         max_contagem = max(contagem_letras.values()) if contagem_letras else 0

#         if max_contagem > max_letras_repetidas:
#               max_letras_repetidas = max_contagem
#               maximorepetidas = palavra 

#   if max_letras_repetidas > 1:
#     return maximorepetidas
#   else:
#     return -1


# frase_exemplo = " por favor isso tem que dar certoooo agora"

    
#     # keep this function call here 
# print(LetterCount(frase_exemplo))




def VowelCount(frase):
 contadordevogais = 0
 vogais = "aeiouAEIOU"

 for letra in frase:
   if letra in vogais:
      contadordevogais +=1
 return contadordevogais

frase = " essa frase é um teste"

# keep this function call here 
print(VowelCount(frase))