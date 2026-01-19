class GardenError(Exception):
    pass


class EmptyNameError(GardenError):
    def __init__(self, message="Error: Plant name cannot be empty"):
        self.message = message
        super().__init__(message)


class PlantNotFoundError(GardenError):
    pass


class InvalidWaterAmountError(GardenError):
    pass


class GardenFullError(GardenError):
    pass


class DeadPlantError(GardenError):
    pass


class DuplicatePlantError(GardenError):
    pass


class Node:
    def __init__(self, plant_name, water_requ):
        self.plant_name = plant_name
        self.water_requirements = water_requ
        self.Plant_status = "healthy"
        self.list_size = 0
        self.water_level = 5
        self.plant_alive = True
        self.next = None


# ======================= Garden Manager Class =========================


class GardenManager:
    """Manages a collection of plants in the garden."""

    def __init__(self, max_plants=10):
        self.plant_list_head = None
        self.plant_list_size = 0
        self.max_plants = max_plants
        self.operation_log = []  # Log of operations for debugging
        self.water_usage = 0

    def log_operation(self, operation):
        self.operation_log.append(operation)

    def add_plant_to_list(self, name, water_requ=3):
        """Adds a new plant to the garden."""
        new_node = Node(name, water_requ)
        try:
            if not name or name == "":
                raise EmptyNameError()
            if self.plant_list_head is None:
                self.plant_list_head = new_node
                self.plant_list_head.list_size += 1
                return
            current = self.plant_list_head
            while current is not None:
                if current.plant_name == name:
                    raise DuplicatePlantError()
                current = current.next
            if self.plant_list_size >= self.max_plants:
                raise GardenFullError()
            if self.plant_list_head is None:
                self.plant_list_head = new_node
                return
            current = self.plant_list_head
            while current.next is not None:
                current = current.next
            current.next = new_node
            current.list_size += 1
            print(f"✅ Plant '{name}' added to the garden.")
            self.log_operation(f"✅ Plant '{name}' added to the garden.")

        except (EmptyNameError, DuplicatePlantError, GardenFullError) as e:
            self.log_operation(f"❌ Error trying to add plant: {e}")
            raise  # Re-raise
        except Exception as e:
            self.log_operation(f"❌ Error unknown {e}")
            raise GardenError(f"❌ Unknowen Error type: {e}")

    def water_plant(self, amount=3):
        """waters all plants in the garden"""
        try:
            print(f"💧 All plants were watered with {amount}L of water!")
            if amount < 1:
                raise InvalidWaterAmountError()
            current = self.plant_list_head
            while current is not None:
                if current.plant_alive is False:
                    print(f"💀 Plant '{current.plant_name}' is dead and "
                          f"cannot be watered.")
                current.water_level += amount
                if current.water_level > current.water_requirements * 2:
                    current.plant_alive = False
                    print(f"💀 Plant '{current.plant_name}' has drowned "
                          f"due to overwatering!")
                current = current.next
            self.log_operation(f"💧 All plants were watered with {amount}L "
                               f"of water")

        except (InvalidWaterAmountError, DeadPlantError) as e:
            self.log_operation(f"❌ Error watering: {e}")
            raise
        except Exception as e:
            self.log_operation(f"❌ Unknowen Error: {e}")
            raise GardenError(f"Unknown Error while watering: {e}")
        finally:
            # CLEANUP
            print("🔒 watering finished")

    def check_plant_health(self, name):
        try:
            if not isinstance(name, str):
                raise TypeError("Plantname must be a string!")
            current = self.plant_list_head
            checker = 0
            while current is not None:
                if current.plant_name == name:
                    checker = 1
                current = current.next
            if checker == 0:
                raise PlantNotFoundError(f"Plant {name} is not found in "
                                         f"the Garden")
            plant = self.plants[name]
            health = plant.check_health()
            print(f"Healthcheck of '{name}': {health}")
            print(f" Waterlevel: {plant.water_level:.1f}")
        except (PlantNotFoundError, TypeError)as e:
            self.log_operation(f"Health check failed: {e}")
            raise

    def check_all_plants(self):
        """checking healty of all plants in the Garden"""
        current = self.plant_list_head
        if current is None:
            print("The garden is empty")
            return

        print("\n" + "=" * 30)
        print("Garden Status")
        print("=" * 30 + "\n")

        current = self.plant_list_head
        counter = 0
        while current is not None:
            if current.plant_alive is False:
                print(f"{current.plant_name} is Dead!!!")
                counter += 1
            if current.water_requirements > current.water_level:
                print(f"{current.plant_name} is low on water!")
                counter += 1
            if current.plant_alive is True and \
               current.water_level >= current.water_requirements:
                print(f"{current.plant_name} is healthy.")
            current = current.next

    def simulate_day(self):
        """Is simulating a Day in the Garden"""
        print("\n⏰ One day past...")
        current = self.plant_list_head
        while current is not None:
            if current.plant_alive is False:
                current = current.next
                continue
            if current.water_level <= 0:
                current.plant_alive = False
                print(f"💀 Plant '{current.plant_name}' has died due to "
                      f"lack of water!")
            if current.water_requirements > current.water_level:
                current.water_level - 1
                current.plant_alive = False
                print(f"💀 Plant '{current.plant_name}' has died due to too "
                      f"little water!")
            current.water_level - 1
            current = current.next
        print("New Day Started check the plant status")

    def get_plant_statistics(self):
        print("\n" + "=" * 30)
        print("The statistics of the Garden are")
        print("=" * 30 + "\n")
        current = self.plant_list_head
        dead_plants = 0
        plants_alive = 0
        healty_plants = 0
        unhealthy_plants = 0
        while current is not None:
            if current.plant_alive is False:
                dead_plants += 1
            elif current.water_level < current.water_requirements:
                print(f"{current.plant_name} is low on water")
                unhealthy_plants += 1
                plants_alive += 1
            plants_alive += 1
            healty_plants += 1
            current = current.next
        plants_alive = plants_alive - dead_plants
        unhealthy_plants = unhealthy_plants + dead_plants
        healty_plants = healty_plants - unhealthy_plants
        if plants_alive == 0:
            healty_plants = 0
        print(f"Total plants alive: {plants_alive}")
        print(f"Total dead plants: {dead_plants}")
        print(f"Healty plants: {healty_plants}")
        print(f"Unhealty plants: {unhealthy_plants}")

# ==================== Test Function ========================


def test_garden_management():
    """testing the Garden management system"""
    print("=" * 30)
    print("GARDEN MANAGEMENT SYSTEM _ DEMO")
    print("=" * 30)

    garden = GardenManager()

# ========== Test 1 valid numbers =========
    print("\n ==== Test 1:  ====")

    garden.add_plant_to_list("Tomato", 3)
    garden.add_plant_to_list("Rose", 5)
    garden.add_plant_to_list("Sunflower", 5)
    garden.add_plant_to_list("Potato", 4)
    garden.add_plant_to_list("Oak Tree", 7)
    garden.add_plant_to_list("Cucumber", 5)
    garden.get_plant_statistics()
    garden.check_all_plants()
    garden.water_plant(2)
    garden.simulate_day()
    garden.simulate_day()
    garden.simulate_day()
    garden.simulate_day()
    garden.simulate_day()
    garden.simulate_day()
    garden.get_plant_statistics()
    garden.water_plant(50)
    garden.check_all_plants()
    garden.get_plant_statistics()
    print("Garden simulation is over")

# =========== Test 2 unvalid input ===============


def test_garden_management_case_2():
    print("\n ==== Test 2:  ====")
    plot = GardenManager()
    plot.add_plant_to_list("Tomato", 2)
    plot.add_plant_to_list("Rose", 5)
    plot.add_plant_to_list("Sunflower", 3)
    plot.add_plant_to_list("Potato", 4)
    plot.add_plant_to_list("Oak Tree", 7)
    plot.add_plant_to_list("Cucumber", -1)
    plot.water_plant(-3)
    plot.add_plant_to_list(None, 9)
    plot.simulate_day()
    plot.simulate_day()
    plot.simulate_day()
    plot.simulate_day()
    plot.simulate_day()
    plot.simulate_day()
    plot.simulate_day()
    plot.simulate_day()
    plot.simulate_day()
    plot.check_all_plants()
    plot.get_plant_statistics()
    plot.water_plant(2)
    print("Garden simulation is over")


test_garden_management()
