import unittest
from src.todo import ToDoList, InvalidOperationError

class TestToDoTDD(unittest.TestCase):
    def setUp(self):
        self.todo = ToDoList()

    def test_TEST01_add_task_success(self):
        task = self.todo.add_task("Estudar TDD", "Ler sobre Red-Green-Refactor")
        self.assertIsNotNone(task.id)
        self.assertEqual(task.name, "Estudar TDD")
        self.assertEqual(task.description, "Ler sobre Red-Green-Refactor")
        self.assertEqual(task.status, "pending")

    def test_TEST02_add_task_empty_name_or_description_raises(self):
        with self.assertRaises(ValueError):
            self.todo.add_task("", "desc válida")
        with self.assertRaises(ValueError):
            self.todo.add_task("nome válido", "   ")

    def test_TEST03_mark_done_updates_status(self):
        t = self.todo.add_task("Escrever casos de teste", "Cobrir requisitos")
        changed = self.todo.mark_done(t.id)
        self.assertTrue(changed)
        self.assertEqual(self.todo.get_task(t.id).status, "done")

    def test_TEST04_mark_done_already_done_idempotent(self):
        t = self.todo.add_task("Refatorar", "Melhorar clareza")
        self.todo.mark_done(t.id)
        changed = self.todo.mark_done(t.id)  
        self.assertFalse(changed)  

    def test_TEST05_mark_in_progress_changes_status(self):
        t = self.todo.add_task("Implementar", "Função X")
        changed = self.todo.mark_in_progress(t.id)
        self.assertTrue(changed)
        self.assertEqual(self.todo.get_task(t.id).status, "in_progress")

    def test_TEST06_cannot_mark_in_progress_when_done(self):
        t = self.todo.add_task("Fechar tarefa", "Etapa final")
        self.todo.mark_done(t.id)
        with self.assertRaises(InvalidOperationError):
            self.todo.mark_in_progress(t.id)

    def test_TEST07_edit_updates_fields(self):
        t = self.todo.add_task("Antigo", "Descricao antiga")
        updated = self.todo.edit_task(t.id, name="Novo nome", description="Nova descricao")
        self.assertEqual(updated.name, "Novo nome")
        we = self.assertEqual(updated.description, "Nova descricao")

    def test_TEST08_edit_nonexistent_raises(self):
        with self.assertRaises(KeyError):
            self.todo.edit_task("nao-existe", name="X")

    def test_TEST09_delete_success(self):
        t = self.todo.add_task("Apagar", "Remover da lista")
        self.todo.delete_task(t.id)
        with self.assertRaises(KeyError):
            self.todo.get_task(t.id)

    def test_TEST10_delete_nonexistent_raises(self):
        with self.assertRaises(KeyError):
            self.todo.delete_task("nao-existe")

if __name__ == "__main__":
    unittest.main()
