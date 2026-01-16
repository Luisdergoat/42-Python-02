class Node:
    def __init__(self, plant_name,):
        self.name = plant_name
        self.water_true = False
        self.next = None


class Garden:
    def __init__(self):
        self.plant_list_head = None

    def add_plant_to_list(self, plant_name):
        new_node = Node(plant_name)
        if self.plant_list_head is None:
            self.plant_list_head = new_node
            print()
            return
        current = self.plant_list_head
        while current.next is not None:
            current = current.next
        current.next = new_node

    def water_plant(self):
        current = self.plant_list_head
        while current is not None:
            current.water_true = True
            print(f"The plant {current.name} has been watered.")
            current = current.next

    def Plant_status(self):
        print("=" * 30)
        print("=== Info about the Garden ===")
        print("=" * 30)
        print("\n")
        current = self.plant_list_head
        while current is not None:
            if current.water_true is True:
                status = "Watered"
            else:
                status = "Not Watered"
            print(f"Plant {current.name} is {status}.")
            current = current.next
        print("\n")
        print("=" * 30)
        print("Cleanup always happens, even with errors!")
        print("=" * 30)


def water_plants(plant_list):
    print("=" * 30)
    print("Testing watering system with list of plants")
    print("=" * 30)
    Plot = Garden()
    for Plant in plant_list:
        if Plant is None:
            print("\n❌ Error: Cannot water None - invalid plant!\n")
            continue
        Plot.add_plant_to_list(Plant)
        print(f"✅ Added {Plant} to Garden")
    print("\n")
    Plot.water_plant()
    print("\n")
    print("✅ Watering completed successfully\n")
    Plot.Plant_status()


def test_watering_system():
    plant_list = ["Tomato", "Cucumber", "Oak Tree"]
    wrong_list = ["Tomato", "Cucumber", None]
    water_plants(plant_list)
    water_plants(wrong_list)


def test_with_inputs():
    Plot = Garden()
    while True:
        new_plant = input("Add a Plant to the Garden: ")
        Plot.add_plant_to_list(new_plant.capitalize())
        go_on = input("Do you want to addd another Plant? (yes/no) ")
        if go_on.lower() == "no":
            break
        elif go_on.lower() == "yes":
            pass
        else:
            print("Invalid input no more Plants to add")
            break

    Water_status = input("Do you want to water the plantss? (yes/no)")
    if Water_status.lower() == "no":
        print("Okay, no plants will be watered.")
    elif Water_status.lower() == "yes":
        print("Opening watering system")
        Plot.water_plant()
        print("Watering completed successfully")
    else:
        print("Invalid input, no plants will be watered.")
    Plot.Plant_status()


test_watering_system()
