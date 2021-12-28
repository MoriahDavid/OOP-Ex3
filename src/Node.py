

class Node:

    def __init__(self, n_id: int, pos: tuple):

        self.n_id = n_id
        self.pos = pos

    def __repr__(self):
        return f"(Node key: {self.n_id})"
