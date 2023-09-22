import math

# Função para calcular a velocidade inicial do lançamento oblíquo
def calcular_velocidade_inicial(forca, massa_projetil):
    return math.sqrt((2 * forca) / massa_projetil)

# Função para calcular o tempo total de voo
def calcular_tempo_total_voo(velocidade_inicial, angulo, gravidade=9.8):
    return (2 * velocidade_inicial * math.sin(math.radians(angulo))) / gravidade

# Função para calcular o alcance horizontal
def calcular_alcance_horizontal(velocidade_inicial, angulo, gravidade=9.8):
    return (velocidade_inicial ** 2 * math.sin(2 * math.radians(angulo))) / gravidade

# Função para calcular as velocidades vertical e horizontal em cada instante do voo
def calcular_velocidades_instantaneas(velocidade_inicial, angulo, tempo, gravidade=9.8):
    vx = velocidade_inicial * math.cos(math.radians(angulo))
    vy = velocidade_inicial * math.sin(math.radians(angulo)) - gravidade * tempo
    return vx, vy

# Função principal
def main():
    x = float(input("Digite a coordenada x do canhão: "))
    y = float(input("Digite a coordenada y do canhão: "))
    forca = float(input("Digite a força em newtons: "))
    angulo = float(input("Digite o ângulo em graus: "))

    massa_projetil = 0.5  # Massa da bala do canhão em Kg
    gravidade = 9.8  # Aceleração devido à gravidade em m/s^2

    velocidade_inicial = calcular_velocidade_inicial(forca, massa_projetil)
    tempo_total_voo = calcular_tempo_total_voo(velocidade_inicial, angulo, gravidade)
    alcance_horizontal = calcular_alcance_horizontal(velocidade_inicial, angulo, gravidade)
    local_queda_x = x + alcance_horizontal
    local_queda_y = 0  # A bala atinge o solo, então a altura é 0.

    print("Resultados:")
    print(f"1. Velocidade Inicial: {velocidade_inicial:.2f} m/s")
    print(f"2. Tempo Total de Voo: {tempo_total_voo:.2f} segundos")
    print(f"3. Local de Queda do Projétil: ({local_queda_x:.2f}, {local_queda_y:.2f})")
    print("4. Velocidades (Vertical, Horizontal) em cada instante do voo:")

    intervalo_tempo = 0.1  # Intervalo de tempo para calcular as velocidades instantâneas

    for tempo in range(int(tempo_total_voo * 10) + 1):
        tempo_segundos = tempo / 10  # Converter para segundos
        vx, vy = calcular_velocidades_instantaneas(velocidade_inicial, angulo, tempo_segundos, gravidade)
        print(f"   Tempo: {tempo_segundos:.1f} s - Vertical: {vy:.2f} m/s, Horizontal: {vx:.2f} m/s")

    print(f"5. Distância Horizontal entre o Ponto de Lançamento e o Local da Queda: {alcance_horizontal:.2f} metros")

if __name__ == "__main__":
    main()
