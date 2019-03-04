def minimax_decision(gameState, depth):

    best_score = float("-inf")
    best_move = None
    for m in gameState.get_legal_moves():

        # call has been updated with a depth limit
        v = min_value(gameState.forecast_move(m), depth - 1)
        if v > best_score:
            best_score = v
            best_move = m
    return best_move


def min_value(gameState, depth):

    if terminal_test(gameState):
        return 1  # by Assumption 2

    # New conditional depth limit cutoff
    if depth <= 0:  # "==" could be used, but "<=" is safer
        return 0

    v = float("inf")
    for m in gameState.get_legal_moves():
        # the depth should be decremented by 1 on each call
        v = min(v, max_value(gameState.forecast_move(m), depth - 1))
    return v


def max_value(gameState, depth):

    if terminal_test(gameState):
        return -1  # by assumption 2

    # New conditional depth limit cutoff
    if depth <= 0:  # "==" could be used, but "<=" is safer
        return 0

    v = float("-inf")
    for m in gameState.get_legal_moves():
        # the depth should be decremented by 1 on each call
        v = max(v, min_value(gameState.forecast_move(m), depth - 1))
    return v

call_counter = 0
def terminal_test(gameState):

    global call_counter
    call_counter += 1
    moves_available = bool(gameState.get_legal_moves())  # by Assumption 1
    return not moves_available
