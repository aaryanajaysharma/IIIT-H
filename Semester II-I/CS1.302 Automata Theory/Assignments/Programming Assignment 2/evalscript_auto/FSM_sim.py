win_pairs = set([('R', 'S'), ('P', 'R'), ('S', 'P')])


class State:
    def __init__(self, id, out, r, p, s):
        self.id = id
        self.out = out
        self.trans = {'R': r, 'P': p, 'S': s}


class FST:

    def __init__(self):
        self.states = []

    def addState(self, out, r, p, s):
        if out not in ['R', 'P', 'S']:
            raise ValueError('output char should be R P or S')
        if min(r, p, s) <= 0:
            raise ValueError('R, P, S transition IDs must be >=0')

        self.states.append(State(len(self.states) + 1, out, r, p, s))

    def checkValid(self):
        for curr in self.states:
            if max(curr.trans['R'], curr.trans['P'], curr.trans['S']) > len(self.states):
                return False
        return True


def eval(A: FST, B: FST, s_A, s_B, rounds=10000):
    status=1
    if not A.checkValid():
        status=0
        raise ValueError('A is not a valid FST')
    if not B.checkValid():
        status=0
        raise ValueError('B is not a valid FST')
    if s_A > len(A.states):
        status=0
        raise ValueError(
            f'FST A start state must be in the range [1, {len(A.states)}]')
    if s_B > len(B.states):
        status=0
        raise ValueError(
            f'FST B start state must be in the range [1, {len(B.states)}]')

    win_A, loss_A, draw = 0, 0, 0
    curr_A, curr_B = A.states[s_A-1], B.states[s_B-1]
    for i in range(rounds):
        out_A, out_B = curr_A.out, curr_B.out
        if out_A == out_B:
            draw += 1
        elif (out_A, out_B) in win_pairs:
            win_A += 1
        else:
            loss_A += 1
        curr_A = A.states[curr_A.trans[out_B] - 1]
        curr_B = B.states[curr_B.trans[out_A] - 1]

    return (win_A, loss_A, draw, status)


if __name__ == '__main__':
    A, B = FST(), FST()
    A.addState('R', 1, 2, 1)
    A.addState('S', 3, 2, 2)
    A.addState('P', 3, 3, 1)

    B.addState('R', 2, 3, 3)
    B.addState('P', 4, 1, 1)
    B.addState('S', 1, 2, 1)
    B.addState('R', 1, 1, 3)

    print(eval(A, B, 3, 1, rounds=5))
