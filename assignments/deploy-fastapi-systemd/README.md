# 📘 Assignment: Deploying FastAPI with systemd

## 🎯 Objective

Nesta atividade, seu grupo vai preparar e publicar uma API FastAPI como servico Linux usando systemd, praticando execucao em ambiente real, observabilidade basica e validacao de disponibilidade.

## 📝 Tasks

### 🛠️ Prepare the API for Deployment

#### Descrição
Use o codigo inicial para executar a API com Uvicorn e garantir que os endpoints principais estao funcionando antes do deploy como servico.

#### Requisitos
O programa concluído deve:

- Executar a API localmente com `uvicorn starter-code:app --host 0.0.0.0 --port 8000`.
- Expor os endpoints `GET /` e `GET /health` retornando JSON valido.
- Ler a variavel de ambiente `APP_ENV` e inclui-la na resposta de `GET /health`.
- Registrar, no terminal, uma evidencia de sucesso para o endpoint de health check.

### 🛠️ Deploy the API as a systemd Service

#### Descrição
Configure um servico systemd para iniciar a API automaticamente, reiniciar em caso de falha e permitir monitoramento via logs.

#### Requisitos
O programa concluído deve:

- Preencher o arquivo `fastapi-api.service.example` com caminhos corretos do projeto e usuario.
- Instalar o servico como `fastapi-api.service` e executar `daemon-reload`, `enable` e `start`.
- Confirmar que o servico esta `active (running)` usando `systemctl status`.
- Verificar logs com `journalctl -u fastapi-api.service` e identificar ao menos uma inicializacao bem-sucedida.
- Validar novamente `GET /health` apos subir o servico.
- Trabalhar em grupo: cada integrante deve ser responsavel por uma etapa (configuracao, inicializacao, validacao ou logs).
