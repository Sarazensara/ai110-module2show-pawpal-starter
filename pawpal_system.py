from dataclasses import dataclass, field
from typing import List


@dataclass
class Task:
    description: str
    time: str  # "HH:MM"
    frequency: str = "once"  # once, daily, weekly
    completed: bool = False

    def mark_complete(self):
        self.completed = True


@dataclass
class Pet:
    name: str
    species: str
    tasks: List[Task] = field(default_factory=list)

    def add_task(self, task: Task):
        self.tasks.append(task)


@dataclass
class Owner:
    name: str
    pets: List[Pet] = field(default_factory=list)

    def add_pet(self, pet: Pet):
        self.pets.append(pet)

    def get_all_tasks(self):
        all_tasks = []
        for pet in self.pets:
            for task in pet.tasks:
                all_tasks.append((pet.name, task))
        return all_tasks


class Scheduler:
    def __init__(self, owner: Owner):
        self.owner = owner

    def get_sorted_tasks(self):
        tasks = self.owner.get_all_tasks()
        return sorted(tasks, key=lambda x: x[1].time)

    def detect_conflicts(self):
        seen = {}
        conflicts = []

        for pet_name, task in self.owner.get_all_tasks():
            if task.time in seen:
                conflicts.append((task.time, pet_name, task.description))
            else:
                seen[task.time] = task

        return conflicts