def water_jug_dfs(capacity_jug1, capacity_jug2, target):
    stack = [(0, 0)]  # Initial state with both jugs empty
    visited = set()

    while stack:
        current_state = stack.pop()

        if current_state[0] == target or current_state[1] == target:
            print("Solution found:", current_state)
            return

        print("Exploring:", current_state)
        visited.add(current_state)

        # Fill jug 1
        fill_jug1 = (capacity_jug1, current_state[1])
        if fill_jug1 not in visited:
            stack.append(fill_jug1)

        # Fill jug 2
        fill_jug2 = (current_state[0], capacity_jug2)
        if fill_jug2 not in visited:
            stack.append(fill_jug2)

        # Empty jug 1
        empty_jug1 = (0, current_state[1])
        if empty_jug1 not in visited:
            stack.append(empty_jug1)

        # Empty jug 2
        empty_jug2 = (current_state[0], 0)
        if empty_jug2 not in visited:
            stack.append(empty_jug2)

        # Pour water from jug 1 to jug 2
        pour_jug1_to_jug2 = (
            max(0, current_state[0] - (capacity_jug2 - current_state[1])),
            min(capacity_jug2, current_state[1] + current_state[0])
        )
        if pour_jug1_to_jug2 not in visited:
            stack.append(pour_jug1_to_jug2)

        # Pour water from jug 2 to jug 1
        pour_jug2_to_jug1 = (
            min(capacity_jug1, current_state[0] + current_state[1]),
            max(0, current_state[1] - (capacity_jug1 - current_state[0]))
        )
        if pour_jug2_to_jug1 not in visited:
            stack.append(pour_jug2_to_jug1)

    print("Solution not found.")

# Example usage
water_jug_dfs(4, 3, 2)
