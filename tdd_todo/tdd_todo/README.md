# To-Do List System (TDD)

Projeto simples de **lista de tarefas** com CRUD e marcações de status, desenvolvido com **TDD** utilizando `unittest`.

## Requisitos cobertos
1. Adicionar tarefas com **nome** e **descrição** (ambos obrigatórios).
2. Marcar tarefa como **concluída**.
3. Marcar tarefa como **em andamento**.
4. **Editar** nome e descrição de uma tarefa existente.
5. **Excluir** tarefas da lista.

Casos de borda tratados:
- Impedir criação com nome/descrição vazios (erro `ValueError`).
- `mark_done` é **idempotente**: chamar novamente não altera nada e retorna `False`.
- Impedir colocar **em andamento** quando a tarefa já está **concluída** (`InvalidOperationError`).
- Editar/Excluir tarefa inexistente gera `KeyError`.

## Como rodar os testes
```bash
cd tdd_todo
python -m unittest
```
(ou rode `python -m unittest tests/test_todo.py`)

Python 3.10+ recomendado. Não há dependências externas.
