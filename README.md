.
├──             
├── core/                   # pasta core com config
│   └── database.py         # Configuração do banco de dados
├── models/                 # Modelos SQLAlchemy
│   └── curso.py
├── schemas/                # Esquemas Pydantic
│   └── curso.py
├── repositories/           # Repositórios para acesso ao banco
│   └── curso_repository.py
├── services/               # Lógica de negócios
│   └── curso_service.py
├── routes/                 # Rotas FastAPI
│   └── curso_routes.py
├── criar_tabelas.py        # Script para criar tabelas
├── main.py                 # Ponto de entrada da aplicação
└── .env                    # Variáveis de ambiente (opcional)
