# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Nesta atividade, você vai construir uma API REST com FastAPI para praticar rotas HTTP, validacao com Pydantic, codigos de status e manipulacao basica de dados em memoria.

## 📝 Tasks

### 🛠️ Create a Basic FastAPI Application

#### Descrição
Crie uma aplicacao FastAPI com um endpoint raiz e um endpoint de health check para validar que o servidor esta funcionando corretamente.

#### Requisitos
O programa concluído deve:

- Criar uma instancia `FastAPI` chamada `app`.
- Implementar `GET /` retornando uma mensagem JSON de boas-vindas.
- Implementar `GET /health` retornando status de funcionamento da API.
- Executar localmente com `uvicorn` sem erros.

### 🛠️ Build CRUD Endpoints for Items

#### Descrição
Implemente uma colecao de endpoints para criar, listar, buscar, atualizar e remover itens usando um armazenamento em memoria.

#### Requisitos
O programa concluído deve:

- Definir um modelo `Item` com `id`, `name`, `price` e `in_stock` usando Pydantic.
- Implementar `POST /items` para criar item com validacao de dados.
- Implementar `GET /items` e `GET /items/{item_id}` para listar e buscar itens.
- Implementar `PUT /items/{item_id}` para atualizar item existente.
- Implementar `DELETE /items/{item_id}` para remover item e retornar codigo apropriado.
- Retornar `404` quando um item nao for encontrado.
