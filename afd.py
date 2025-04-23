# Transições do AFD conforme especificadas
afd = {
    'q0': {'s': 'q1', 'f': 'q7', 'v': 'q22', 'o': 'q42', 'c': 'q16_q25', 't': 'q33_q37', 'w': 'q11_q29'},

    'q1': {'e': 'q2'},
    'q2': {'l': 'q3'},
    'q3': {'e': 'q4'},
    'q4': {'c': 'q5'},
    'q5': {'t': 'q6'},  # SELECT

    'q7': {'r': 'q8'},
    'q8': {'o': 'q9'},
    'q9': {'m': 'q10'},  # FROM

    'q22': {'a': 'q23'},
    'q23': {'r': 'q24'},  # VAR

    'q42': {'p': 'q43'},  # OP

    'q16_q25': {'r': 'q17', 'a': 'q26'},
    'q17': {'e': 'q18'},
    'q18': {'a': 'q19'},
    'q19': {'t': 'q20'},
    'q20': {'e': 'q21'},  # CREATE

    'q26': {'s': 'q27'},
    'q27': {'e': 'q28'},  # CASE

    'q33_q37': {'h': 'q34', 'a': 'q38'},
    'q34': {'e': 'q35'},
    'q35': {'n': 'q36'},  # THEN

    'q38': {'b': 'q39'},
    'q39': {'l': 'q40'},
    'q40': {'e': 'q41'},  # TABLE

    'q11_q29': {'h': 'q12_q30'},
    'q12_q30': {'e': 'q13_q31'},
    'q13_q31': {'r': 'q14', 'n': 'q32'},
    'q14': {'e': 'q15'},  # WHERE
}

# Estados de aceitação
estados_finais = ['q6', 'q10', 'q15', 'q21', 'q24', 'q28', 'q32', 'q36', 'q41', 'q43']

def transicao(afd, estado_inicial, cadeia):
    fita_saida = []
    tabela_simbolos = []

    for token in cadeia:
        estado_atual = estado_inicial
        for letra in token.lower():
            if letra in afd.get(estado_atual, {}):
                estado_atual = afd[estado_atual][letra]
            else:
                estado_atual = 'X'
                break

        if estado_atual in estados_finais:
            fita_saida.append(estado_atual)
        else:
            fita_saida.append('X')

        tabela_simbolos.append({'token': token, 'estado_final': estado_atual})

    return fita_saida, tabela_simbolos

# Lê os tokens de um arquivo (palavras separadas por espaço)
def ler_entrada(nome_arquivo):
    with open(nome_arquivo, 'r') as f:
        conteudo = f.read()
        return conteudo.strip().split()

# --------- Execução ---------
entrada = ler_entrada("entrada.txt")
estado_inicial = 'q0'

fita_saida, tabela_simbolos = transicao(afd, estado_inicial, entrada)

print("Fita de saída:", fita_saida)
print("\nTabela de símbolos:")
for entrada in tabela_simbolos:
    print(entrada)
