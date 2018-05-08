#!/usr/bin/env python
# jaccard.py- Gera o coeficiente de Jaccard
#
# Autor     : Alexandre Cunha (Cunha A.M) <alexandremartinscunha@yahoo.com.br> 
# Manutenção: Alexandre Cunha (Cunha A.M) <alexandremartinscunha@yahoo.com.br>
#
# --------------------------------------------------------------------------------------------------------------------------
# 	Este script trata duas string removendo pontuação e converte o texto para caixa baixa, após retorna o coeficiente de Jaccard entre eles.
# --------------------------------------------------------------------------------------------------------------------------
#
# --------------------------------------------------------------------------------------------------------------------------
#	Tem como base o script de Leandro War (arte dos dados), nome original "keywordsSimilarity.py".
# 	Disponível em: https://github.com/leandrowar/ArtWithDataCodes/blob/master/keywordsSimilarity.py
#  --------------------------------------------------------------------------------------------------------------------------
#
# Codificação: utf-8
#
# Histórico:
#
#    v1.0 2014-XX-XX, Leandro War:
#       - Versão inicial (Obra de Leandro War).
#
#    v1.1 2018-02-09, Alexandre Cunha:
#	- Acrescentando a regex para remover pontuação;
#	- Acrescentando a regex para deixar o texto em minúsculo;
#	- Incluído comentários com explicações e tradução de termos.   
#
# Licença: GPL.


# Uso de Regex
import re

#Calcula o Coeficiênte de Jaccard (case senstitive)
# split() - Método que transforma os caracteres separados por espaço em String.
# set()   - Método que pega apenas uma cópia de cada item, ou seja, remove repetições.
# len()   - Metodo que exibe o tamanho da String (No caso em tela do conjunto).
# &       - Operador lógica E que exerce a função interceção do conjunto.
# |       - Operador lógica OU que exerce a função união do conjunto.

def CoefJaccard(conjunto1, conjunto2):
    conjunto1= set(conjunto1.split())
    conjunto2 = set(conjunto2.split())
    return float(len(conjunto1 & conjunto2)) / len(conjunto1 | conjunto2)


medicamento1 = 'pioria da insônia, pesadelos, nervosismo, confusão, sensação de vertigem, dificuldade na marcha, tontura, falta de coordenação dos músculos, dor de cabeça, sonolência durante o dia, perda da capacidade de vigília, fraqueza muscular ou visão dupla.'
medicamento2 = 'Episódios de confusão; Reação do tipo paradoxal ou psiquiátrica; Sensação de vertigem, instabilidade na marcha, tontura, ataxia; Cefaléia; Sonolência diurna, perda da capacidade de vigília; Fraqueza muscular; Diplopia. Astenia; Distúrbios gastrintestinais; Alterações da libido; Reações cutâneas; Amnésia, insônia de rebote, tolerância e dependência.'

#Remove pontuação  e converte o texto para minúscula via (Regex)
string_medicamento1 = re.sub(u'[^a-zA-Z0-9áéíóúÁÉÍÓÚâêîôÂÊÎÔãõÃÕçÇ ]','', medicamento1.lower())
string_medicamento2 = re.sub(u'[^a-zA-Z0-9áéíóúÁÉÍÓÚâêîôÂÊÎÔãõÃÕçÇ ]','', medicamento2.lower())

##Imprime os dados antes e depois da modificação ###
print(medicamento1)
print ()
print(string_medicamento1.strip())
print ()
print(medicamento2)
print ()
print(string_medicamento2.strip())


print ('-'*60)
print ('Retorna o coeficiente de Jaccard, entre 0 e 1')
print ('-'*60)
print (CoefJaccard(string_medicamento1,string_medicamento2))
print ('-'*60)
print ()
print ()
print ()
