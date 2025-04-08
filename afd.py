afd = {
    '{q0}': {'SELECT': '{q1,q2}'},
    '{q1,q2}': {'FUNCTION': '{q2}', 'column': '{q3,q4}'},
    '{q2}': {'column': '{q3,q4}'},
    '{q3,q4}': {'FROM': '{q5}', 'comma': '{q1,q2}'},
    '{q5}': {'table': '{q6}'},
    '{q6}': {'WHERE': '{q7}'},
    '{q7}': {'filter': '{q8}'},
    '{q8}': {'op_aritmetico': '{q9}'},
    '{q9}': {'value': '{q10,q11}'},
    '{q10,q11}': {'op_logico': '{q7}'}
}

estados_finais = ['{q6}', '{q10,q11}']

valores = {
    'FUNCTION': ['MAX', 'MIN', 'SUM', 'AVG', 'COUNT'],
    'op_aritmetico': ['>', '>=', '<', '<=', '=', '!='],
    'op_logico': ['AND', 'OR']
}

def identificar_valor(simbolo, estado_atual):
    if simbolo in valores['FUNCTION']:
        return 'FUNCTION'
    if simbolo in valores['op_aritmetico']:
        return 'op_aritmetico'
    if simbolo in valores['op_logico']:
        return 'op_logico'
    if simbolo == ',':
        return 'comma'
    if estado_atual in ['{q1,q2}', '{q2}', '{q3,q4}']:
        return 'column'
    if estado_atual == '{q5}':
        return 'table'
    if estado_atual == '{q9}':
        return 'value'
    if estado_atual == '{q7}':
        return 'filter'
    
    return None

def transicao(afd, estado_inicial, cadeia):
    estado_atual = estado_inicial
    fita = [estado_atual]
    tabela_simbolos = []

    for simbolo in cadeia:
        valor = identificar_valor(simbolo, estado_atual)
        transicao_realizada = False

        if valor and valor in afd.get(estado_atual, {}):
            tabela_simbolos.append({'simbolo': simbolo, 'rotulo': valor})
            estado_atual = afd[estado_atual][valor]
            fita.append(estado_atual)
            transicao_realizada = True
            
        elif simbolo in afd.get(estado_atual, {}):
            tabela_simbolos.append({'simbolo': simbolo, 'rotulo': simbolo})
            estado_atual = afd[estado_atual][simbolo]
            fita.append(estado_atual)
            transicao_realizada = True

        if not transicao_realizada:
            fita.append('X') 
            tabela_simbolos.append({'simbolo': simbolo, 'rotulo': 'ERRO'})

    if estado_atual in estados_finais:
        fita.append('$')  

    return fita, tabela_simbolos



arquivo_entrada = r"C:\Users\marco\OneDrive\Documentos\compiladores\Lexical-Recognizer\entrada.txt"

with open(arquivo_entrada, 'r') as arquivo:
        cadeia = arquivo.read().strip().split()

estado_inicial = '{q0}'
fita_saida, tabela_simbolos = transicao(afd, estado_inicial, cadeia)

print("Fita de saída:", ' -> '.join(fita_saida))
print()

print(f"{'Símbolo'.ljust(20)}{'Rótulo'.ljust(20)}\n")
print(f"{'-'*20}{'-'*20}\n")
for entrada in tabela_simbolos:
    print(f"{entrada['simbolo'].ljust(20)}{entrada['rotulo'].ljust(20)}\n")