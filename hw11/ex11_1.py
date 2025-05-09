class MooreMachine:
    known_moves = "sway", "pull", "sort", "join", "jog", "loop"
    transitions = {
        "d0": {"sway": "d4"},
        "d1": {"sway": "d3"},
        "d2": {"pull": ["d0", "d1"]},
        "d3": {"sort": "d7"},
        "d4": {"sort": "d5"},
        "d5": {"join": "d1"},
        "d6": {"jog": "d2", "pull": "d4"},
        "d7": {"jog": "d4", "loop": "d6", "sway": "d7"}
    }

    outputs = {
        "d0": "j5",
        "d1": "j5",
        "d2": "j5",
        "d3": "j6",
        "d4": "j2",
        "d5": "j7",
        "d6": "j1",
        "d7": "j1"
    }

    def __init__(self):
        self.state = "d5"
        self._w = 0

    def move(self, word):
        if word not in self.known_moves:
            return "unknown"
        if word not in self.transitions[self.state]:
            return "unsupported"
        new_state = MooreMachine.transitions[self.state][word]
        if self.state == "d2":
            new_state = new_state[self._w]
        self.state = new_state

    @staticmethod
    def part_of_loop():
        return True

    def w(self, new_value):
        self._w = new_value

    def has_max_in_edges(self):
        return self.state == "d4"

    def get_output(self):
        return self.outputs[self.state]


def main():
    return MooreMachine()


def test():
    obj = main()
    assert (obj.get_output() == "j7")
    assert (obj.move("LOUD INCORRECT BUZZ NOISE") == "unknown")
    assert (obj.move("jog") == "unsupported")
    assert (obj.move("join") is None)
    obj.state = "d2"
    assert (obj.w(1) is None)
    assert (obj.move("pull") is None)
    obj.state = "d2"
    assert (obj.w(0) is None)
    assert (obj.move("pull") is None)
    assert (not obj.has_max_in_edges())
    assert (obj.part_of_loop())
