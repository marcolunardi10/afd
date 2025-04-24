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

estados_finais = ['q6', 'q10', 'q15', 'q21', 'q24', 'q28', 'q32', 'q36', 'q41', 'q43']

def transicao(token):
    estado = 'q0'
    caminho = []
    for letra in token:
        if estado in afd and letra in afd[estado]:
            estado = afd[estado][letra]
            caminho.append(estado)
        else:
            return caminho, 'ERRO'
    if estado in estados_finais:
        return caminho, 'PALAVRA_RESERVADA'
    else:
        return caminho, 'ERRO'

def processar_entrada(caminho_arquivo):
    tabela_simbolos = []
    fita_saida = []

    with open(caminho_arquivo, 'r') as arquivo:
        linhas = arquivo.readlines()

    for numero_linha, linha in enumerate(linhas, start=1):
        tokens = linha.strip().split()
        for token in tokens:
            caminho, rotulo = transicao(token)
            fita_saida.append(caminho[-1] if rotulo != 'ERRO' else 'X')
            tabela_simbolos.append({
                'linha': numero_linha,
                'identificador': token,
                'rotulo': rotulo
            })

    return fita_saida, tabela_simbolos


entrada = '/home/marco/Documents/afd/afd/entrada.txt'

fita, tabela = processar_entrada(entrada)

print("Fita de saída:")
print(fita)
print("\nTabela de Símbolos:\n")
print(f"{'Linha':<8}{'Token':<20}{'Rótulo':<20}")
print("-" * 48)
for simb in tabela:
    print(f"{simb['linha']:<8}{simb['identificador']:<20}{simb['rotulo']:<20}")
