class Node:
    def __init__(self, id, node_type, has_traffic_light, rsu_ids=None, drone_ids=None):
        self.id = id
        self.node_type = node_type
        self.has_traffic_light = has_traffic_light
        self.rsu_ids = rsu_ids if rsu_ids is not None else []
        self.drone_ids = drone_ids if drone_ids is not None else []

    def get_attribute(self, attribute_name):
        if attribute_name == "id":
            return self.id
        elif attribute_name == "node_type":
            return self.node_type
        elif attribute_name == "has_traffic_light":
            return self.has_traffic_light
        elif attribute_name == "rsu_ids":
            return self.rsu_ids
        elif attribute_name == "drone_ids":
            return self.drone_ids
        else:
            raise ValueError("Invalid attribute name")

    def set_attribute(self, attribute_name, value):
        if attribute_name == "id":
            self.id = value
        elif attribute_name == "node_type":
            self.node_type = value
        elif attribute_name == "has_traffic_light":
            self.has_traffic_light = value
        elif attribute_name == "rsu_ids":
            self.rsu_ids = value
        elif attribute_name == "drone_ids":
            self.drone_ids = value
        else:
            raise ValueError("Invalid attribute name")


class TrafficLight:
    def __init__(self, id, current_state, remaining_time, durations):
        self.id = id
        self.current_state = current_state
        self.remaining_time = remaining_time
        self.durations = durations

    def get_attribute(self, attribute_name):
        if attribute_name == "id":
            return self.id
        elif attribute_name == "current_state":
            return self.current_state
        elif attribute_name == "remaining_time":
            return self.remaining_time
        elif attribute_name == "durations":
            return self.durations
        else:
            raise ValueError("Invalid attribute name")

    def set_attribute(self, attribute_name, value):
        if attribute_name == "id":
            self.id = value
        elif attribute_name == "current_state":
            self.current_state = value
        elif attribute_name == "remaining_time":
            self.remaining_time = value
        elif attribute_name == "durations":
            self.durations = value
        else:
            raise ValueError("Invalid attribute name")


class RSU:
    def __init__(self, id, computation_capacity, concurrency_capacity, position):
        self.id = id
        self.computation_capacity = computation_capacity
        self.concurrency_capacity = concurrency_capacity
        self.position = position

    def get_attribute(self, attribute_name):
        if attribute_name == "id":
            return self.id
        elif attribute_name == "computation_capacity":
            return self.computation_capacity
        elif attribute_name == "concurrency_capacity":
            return self.concurrency_capacity
        elif attribute_name == "position":
            return self.position
        else:
            raise ValueError("Invalid attribute name")

    def set_attribute(self, attribute_name, value):
        if attribute_name == "id":
            self.id = value
        elif attribute_name == "computation_capacity":
            self.computation_capacity = value
        elif attribute_name == "concurrency_capacity":
            self.concurrency_capacity = value
        elif attribute_name == "position":
            self.position = value
        else:
            raise ValueError("Invalid attribute name")


class Vehicle:
    def __init__(self, id, offload_probability, latency_requirement, position, speed, entry_node, exit_node, edge_id):
        self.id = id
        self.offload_probability = offload_probability
        self.latency_requirement = latency_requirement
        self.position = position
        self.speed = speed
        self.entry_node = entry_node
        self.exit_node = exit_node
        self.edge_id = edge_id

    def get_attribute(self, attribute_name):
        if attribute_name == "id":
            return self.id
        elif attribute_name == "offload_probability":
            return self.offload_probability
        elif attribute_name == "latency_requirement":
            return self.latency_requirement
        elif attribute_name == "position":
            return self.position
        elif attribute_name == "speed":
            return self.speed
        elif attribute_name == "entry_node":
            return self.entry_node
        elif attribute_name == "exit_node":
            return self.exit_node
        elif attribute_name == "edge_id":
            return self.edge_id
        else:
            raise ValueError("Invalid attribute name")

    def set_attribute(self, attribute_name, value):
        if attribute_name == "id":
            self.id = value
        elif attribute_name == "offload_probability":
            self.offload_probability = value
        elif attribute_name == "latency_requirement":
            self.latency_requirement = value
        elif attribute_name == "position":
            self.position = value
        elif attribute_name == "speed":
            self.speed = value
        elif attribute_name == "entry_node":
            self.entry_node = value
        elif attribute_name == "exit_node":
            self.exit_node = value
        elif attribute_name == "edge_id":
            self.edge_id = value
        else:
            raise ValueError("Invalid attribute name")


class Drone:
    def __init__(self, id, position, covered_nodes, computation_capacity, concurrency_capacity):
        self.id = id
        self.position = position
        self.covered_nodes = covered_nodes
        self.computation_capacity = computation_capacity
        self.concurrency_capacity = concurrency_capacity

    def get_attribute(self, attribute_name):
        if attribute_name == "id":
            return self.id
        elif attribute_name == "position":
            return self.position
        elif attribute_name == "covered_nodes":
            return self.covered_nodes
        elif attribute_name == "computation_capacity":
            return self.computation_capacity
        elif attribute_name == "concurrency_capacity":
            return self.concurrency_capacity
        else:
            raise ValueError("Invalid attribute name")

    def set_attribute(self, attribute_name, value):
        if attribute_name == "id":
            self.id = value
        elif attribute_name == "position":
            self.position = value
        elif attribute_name == "covered_nodes":
            self.covered_nodes = value
        elif attribute_name == "computation_capacity":
            self.computation_capacity = value
        elif attribute_name == "concurrency_capacity":
            self.concurrency_capacity = value
        else:
            raise ValueError("Invalid attribute name")


class Road:
    def __init__(self, id, node1, node2, length):
        self.id = id
        self.node1 = node1
        self.node2 = node2
        self.length = length

    def get_attribute(self, attribute_name):
        if attribute_name == "id":
            return self.id
        elif attribute_name == "node1":
            return self.node1
        elif attribute_name == "node2":
            return self.node2
        elif attribute_name == "length":
            return self.length
        else:
            raise ValueError("Invalid attribute name")

    def set_attribute(self, attribute_name, value):
        if attribute_name == "id":
            self.id = value
        elif attribute_name == "node1":
            self.node1 = value
        elif attribute_name == "node2":
            self.node2 = value
        elif attribute_name == "length":
            self.length = value
        else:
            raise ValueError("Invalid attribute name")
