import random


class AlgUtils:
    def __init__(self):
        self.possible_moves = {
            "x": ["R", "L"],
            "y": ["U", "D"],
            "z": ["F", "B"]
        }
        self.alg = None

    def apply_alg(self, alg):
        self.alg = alg

    def _get_axis_by_face(self, face):
        for axis, faces in self.possible_moves.items():
            if face in faces:
                return axis

    def _get_possible_moves_without_one_face(self, face):
        return {k: [f for f in v if f != face] for k, v in \
                self.possible_moves.items()}

    def _select_face(self, last_faces):
        last_face = last_faces[-1] if last_faces else None
        axes = list(self.possible_moves.keys())
        possible_moves = self._get_possible_moves_without_one_face(last_face)
        if len(last_faces) > 1:
            ax1 = self._get_axis_by_face(last_faces[-1])
            ax2 = self._get_axis_by_face(last_faces[-2])
            if ax1 == ax2:
                axes = [ax for ax in axes if ax != ax1]
        #print(last_faces[-3:], '=>', [possible_moves[ax] for ax in axes])
        random_axis = random.choice(axes)
        random_face = random.choice(possible_moves[random_axis])
        return random_face

    def generate_scramble_alg(self, moves):
        alg = []
        last_faces = []
        for move in range(moves):
            current_face = self._select_face(last_faces)
            last_faces.append(current_face)
            current_direction = random.choice(["'", "2", ""])
            alg.append(current_face + current_direction)
        self.alg = ' '.join(alg)

    @property
    def reversed(self):
        if self.alg is None:
            return None
        processed_alg = self.alg.split()[::-1]
        final_alg = []
        for move in processed_alg:
            if "'" in move:
                final_alg.append(move.replace("'", ""))
            elif "2" in move:
                final_alg.append(move)
            else:
                final_alg.append(move + "'")
        return ' '.join(final_alg)


if __name__ == '__main__':
    au1 = AlgUtils()
    au1.generate_scramble_alg(25)
    print("Scramble:", au1.alg)
    print("Inverse:", au1.reversed)
