import minimax
import gamestate as game

depth_limit = 1
expected_node_count = 5
rootNode = game.GameState()
_ = minimax.minimax_decision(rootNode, depth_limit)

print("Expected node count: {}".format(expected_node_count))
print("Your node count: {}".format(minimax.call_counter))

if minimax.call_counter == expected_node_count:
    print("That's right! Looks like your depth limit is working!")
else:
    print("Uh oh...looks like there may be a problem.")
