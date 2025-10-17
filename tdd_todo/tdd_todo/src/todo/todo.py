from __future__ import annotations
from dataclasses import dataclass, field
from typing import Dict, Optional
import uuid

class InvalidOperationError(Exception):
    """Erro para operações inválidas no estado atual da tarefa."""
    pass

@dataclass
class Task:
    name: str
    description: str
    id: str = field(default_factory=lambda: str(uuid.uuid4()))
    status: str = field(default="pending")  # pending | in_progress | done

    def __post_init__(self):
        if not isinstance(self.name, str) or not self.name.strip():
            raise ValueError("Nome da tarefa é obrigatório e não pode ser vazio.")
        if not isinstance(self.description, str) or not self.description.strip():
            raise ValueError("Descrição da tarefa é obrigatória e não pode ser vazia.")

class ToDoList:
    def __init__(self):
        self._tasks: Dict[str, Task] = {}

    # CRUD básico
    def add_task(self, name: str, description: str) -> Task:
        task = Task(name=name, description=description)
        self._tasks[task.id] = task
        return task

    def get_task(self, task_id: str) -> Task:
        try:
            return self._tasks[task_id]
        except KeyError:
            raise KeyError("Tarefa não encontrada.")

    def edit_task(self, task_id: str, *, name: Optional[str] = None, description: Optional[str] = None) -> Task:
        task = self.get_task(task_id)
        if name is not None:
            if not isinstance(name, str) or not name.strip():
                raise ValueError("Nome não pode ser vazio.")
            task.name = name
        if description is not None:
            if not isinstance(description, str) or not description.strip():
                raise ValueError("Descrição não pode ser vazia.")
            task.description = description
        return task

    def delete_task(self, task_id: str) -> None:
        if task_id not in self._tasks:
            raise KeyError("Tarefa não encontrada.")
        del self._tasks[task_id]

    # Status
    def mark_done(self, task_id: str) -> bool:
        task = self.get_task(task_id)
        if task.status == "done":
            # idempotente, nenhuma alteração
            return False
        task.status = "done"
        return True

    def mark_in_progress(self, task_id: str) -> bool:
        task = self.get_task(task_id)
        if task.status == "done":
            raise InvalidOperationError("Não é possível marcar 'em andamento' uma tarefa concluída.")
        if task.status == "in_progress":
            return False  # já estava em andamento
        task.status = "in_progress"
        return True

    # Utilidades
    def list_tasks(self):
        return list(self._tasks.values())
