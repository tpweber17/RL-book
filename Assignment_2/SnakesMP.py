from rl.markov_process import *


@dataclass(frozen=True)
class GameState:
	position: int


class SnakesAndLaddersMPFinite(FiniteMarkovProcess[GameState]):
	numStates: int = 100
	possible_rolls = [1, 2, 3, 4, 5, 7, 8, 9, 10, 11, 12]

	def __init__(self, SnakesLadders, Movement):
		self.SnakesLadders = SnakesLadders
		self.Movement = Movement
		super().__init__(self.get_transition_map())

	def get_transition_map(self) -> \
			Mapping[GameState, FiniteDistribution[GameState]]:
		d: Dict[GameState, Categorical[GameState]] = {}

		for i in range(self.numStates):
			state = GameState(i+1)

			if (i+1) in SnakesLadders:
				state_probs_map: Mapping[GameState, float] = {
					GameState(self.Movement[self.SnakesLadders.index(i+1)]): 1.0
				}
			else:
				state_probs_map: Mapping[GameState, float] = {
					GameState(i+1+self.possible_rolls[j]): 
					(1/6 if (j+1) < 6 else
					1/36)
					for j in range(len(self.possible_rolls))
				}

			d[GameState(i+1)] = Categorical(state_probs_map)

		return d



SnakesLadders = [5, 10, 20, 25, 30, 35, 40, 50, 55, 60, 70, 80, 90, 97]
Movement =      [3, 17,  2, 37, 49, 12, 51, 63, 24, 19, 98, 85, 76, 88]
a = SnakesAndLaddersMPFinite(SnakesLadders, Movement)

print(a)
