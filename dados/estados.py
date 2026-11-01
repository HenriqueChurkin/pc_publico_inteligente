"""Estados brasileiros: sigla, nome, capital e uma cidade do interior (usada nos exemplos fictícios)."""

ESTADOS = [
    ("AC", "Acre", "Rio Branco", "Cruzeiro do Sul"),
    ("AL", "Alagoas", "Maceió", "Arapiraca"),
    ("AP", "Amapá", "Macapá", "Santana"),
    ("AM", "Amazonas", "Manaus", "Parintins"),
    ("BA", "Bahia", "Salvador", "Feira de Santana"),
    ("CE", "Ceará", "Fortaleza", "Juazeiro do Norte"),
    ("DF", "Distrito Federal", "Brasília", "Taguatinga"),
    ("ES", "Espírito Santo", "Vitória", "Vila Velha"),
    ("GO", "Goiás", "Goiânia", "Anápolis"),
    ("MA", "Maranhão", "São Luís", "Imperatriz"),
    ("MT", "Mato Grosso", "Cuiabá", "Rondonópolis"),
    ("MS", "Mato Grosso do Sul", "Campo Grande", "Dourados"),
    ("MG", "Minas Gerais", "Belo Horizonte", "Uberlândia"),
    ("PA", "Pará", "Belém", "Santarém"),
    ("PB", "Paraíba", "João Pessoa", "Campina Grande"),
    ("PR", "Paraná", "Curitiba", "Londrina"),
    ("PE", "Pernambuco", "Recife", "Caruaru"),
    ("PI", "Piauí", "Teresina", "Parnaíba"),
    ("RJ", "Rio de Janeiro", "Rio de Janeiro", "Niterói"),
    ("RN", "Rio Grande do Norte", "Natal", "Mossoró"),
    ("RS", "Rio Grande do Sul", "Porto Alegre", "Caxias do Sul"),
    ("RO", "Rondônia", "Porto Velho", "Ji-Paraná"),
    ("RR", "Roraima", "Boa Vista", "Rorainópolis"),
    ("SC", "Santa Catarina", "Florianópolis", "Joinville"),
    ("SP", "São Paulo", "São Paulo", "Campinas"),
    ("SE", "Sergipe", "Aracaju", "Nossa Senhora do Socorro"),
    ("TO", "Tocantins", "Palmas", "Araguaína"),
]

ESTADOS_POR_UF = {e[0]: e for e in ESTADOS}
