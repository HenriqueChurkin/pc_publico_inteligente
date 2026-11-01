"""Escalas dos componentes (os degraus em que a configuração é arredondada)."""

RAM_PASSOS = [4, 8, 16, 32, 64, 128]            # GB
SSD_PASSOS = [128, 256, 512, 1024, 2048, 4096]  # GB

CPU_MIN, CPU_MAX = 1, 5  # "classe" de desempenho do processador (1 = entrada)

GPU_ROTULOS = {
    0: "Integrada",
    1: "Dedicada de entrada",
    2: "Dedicada intermediária",
    3: "Dedicada avançada",
}
# Usado em frases como "vídeo dedicado, de entrada a intermediário"
GPU_CURTO = {1: "de entrada", 2: "intermediário", 3: "avançado"}

# (id, nome exibido)
COMPONENTES = [
    ("ram", "Memória RAM"),
    ("ssd", "Armazenamento (SSD)"),
    ("cpu", "Processador"),
    ("gpu", "Placa de vídeo"),
]
