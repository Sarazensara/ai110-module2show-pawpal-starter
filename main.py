from pawpal_system import Owner, Pet, Task, Scheduler

# Create owner + pets
owner = Owner("Odette")
dog = Pet("Buddy", "Dog")
cat = Pet("Milo", "Cat")

owner.add_pet(dog)
owner.add_pet(cat)

# Add tasks
dog.add_task(Task("Morning Walk", "08:00"))
dog.add_task(Task("Feed", "09:00"))
cat.add_task(Task("Feed", "09:00"))  # conflict example

# Run scheduler
scheduler = Scheduler(owner)

print("=== Today's Schedule ===")
for pet_name, task in scheduler.get_sorted_tasks():
    print(f"{task.time} - {pet_name}: {task.description}")

# Check conflicts
conflicts = scheduler.detect_conflicts()
if conflicts:
    print("\n⚠️ Conflicts detected:")
    for c in conflicts:
        print(f"Time {c[0]} conflict with {c[1]} task: {c[2]}")