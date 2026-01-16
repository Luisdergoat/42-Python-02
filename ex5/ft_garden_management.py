class Node:
    def __init__(self, plant_name, water_level, sunlight_hours):
        self.plant_name = plant_name
        self.water_level = water_level
        self.sunlight_hours = sunlight_hours
        self.next = None


class Garden:
    def __init__(self):
        self.plant_list_head = None

    def add_plant_to_list(self, plant_name, water_level, sunlight_hours):
        new_node = Node(plant_name, water_level, sunlight_hours)
        if self.plant_list_head is None:
            self.plant_list_head = new_node
            return
        current = self.plant_list_head
        while current.next is not None:
            current = current.next
        current.next = new_node

    def garden_info(self):
        current = self.plant_list_head
        while current is not None:
            print(f"Plant: {current.plant_name} is a healty plant in the "
                  f"Garden")
            current = current.next
