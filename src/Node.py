

class Node:

    def __init__(self, n_id: int, pos: tuple):

        self.n_id = n_id
        self.pos = pos

    def __repr__(self):
        return f"{self.n_id}: |edges out| {'00'} |edges in| {'00'}"  # TODO: 0: |edges out| 1 |edges in| 1