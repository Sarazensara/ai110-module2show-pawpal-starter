from pawpal_system import Task, Pet


def test_task_completion():
    task = Task("Feed", "09:00")
    task.mark_complete()
    assert task.completed is True


def test_add_task_to_pet():
    pet = Pet("Buddy", "Dog")
    task = Task("Walk", "08:00")

    pet.add_task(task)

    assert len(pet.tasks) == 1