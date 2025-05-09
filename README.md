```markdown


# API de E-commerce para Tablets

Uma API baseada em FastAPI para gerenciar produtos de tablets. Este projeto inclui web scraping para popular o banco de dados, operações CRUD e testes automatizados.

## Funcionalidades

- **Operações CRUD**: Criar, Ler, Atualizar e Deletar produtos (tablets).

- **Web Scraping**: Popular automaticamente o banco de dados com tablets de um site pré-definido.

- **Paginação e Busca**: Recuperar resultados paginados e buscar produtos por nome.

- **Testes**: Testes automatizados com banco de dados simulado para endpoints.

- **Design RESTful**: Segue padrões REST com códigos de status HTTP e modelos de resposta adequados.

## Instalação

1. **Clone o repositório**:

```bash

git clone https://github.com/LuizAlbar/TabletsAPI.git

cd TabletsAPI

```

2. **Instale as dependências**:

```bash

pip install -r requirements.txt

```

**Dependências**:

`beautifulsoup4`, `requests`, `sqlalchemy`, `fastapi`, `uvicorn`, `pydantic`, `pydantic-settings`, `httpx`

3. **Configuração do Banco de Dados**:

- Certifique-se de que o MySQL está rodando localmente.

- Atualize a `DATABASE_URL` no arquivo `.env` (crie o arquivo se não existir):

```env

DATABASE_URL=mysql+pymysql://root:root@localhost:3306/products

```

## Uso

1. **Execute o servidor**:

```bash

uvicorn app.main:app --reload

```

- Acesse a interface Swagger: `http://127.0.0.1:8000/docs`

2. **Web Scraping**:

Ao iniciar, o aplicativo coleta dados de [webscraper.io/test-sites/e-commerce/allinone/computers/tablets](https://webscraper.io/test-sites/e-commerce/allinone/computers/tablets) e popula o banco de dados.

## Endpoints da API

| Endpoint                | Método | Descrição                          |

|-------------------------|--------|------------------------------------|

| `/tablets/`             | GET    | Listar todos os tablets (paginado) |

| `/tablets/{tablet_id}`  | GET    | Obter um tablet por ID             |

| `/tablets/`             | POST   | Criar um novo tablet               |

| `/tablets/{tablet_id}`  | PUT    | Atualizar um tablet por ID         |

| `/tablets/{tablet_id}`  | DELETE | Deletar um tablet por ID           |

| `/simulator-tablets/`   | GET    | Dados simulados para testes        |

### Exemplos de Requisições

**Criar um Tablet**:

```bash

curl -X POST "http://127.0.0.1:8000/tablets/" \

-H "Content-Type: application/json" \

-d '{"name": "iPad Pro", "description": "12.9 polegadas", "price": 999.99, "link": "https://apple.com/ipad"}'

```

## Estrutura do Projeto

```

.

├── app/

│   ├── crud/             # Operações CRUD

│   ├── db/               # Configuração do banco de dados

│   ├── models/           # Modelos SQLAlchemy

│   ├── routers/          # Endpoints da API

│   ├── schemas/          # Modelos Pydantic

│   └── main.py           # Configuração do FastAPI

├── tests/                # Testes automatizados

├── requirements.txt      # Dependências

```


## Licença

[MIT](https://choosealicense.com/licenses/mit/)

```
