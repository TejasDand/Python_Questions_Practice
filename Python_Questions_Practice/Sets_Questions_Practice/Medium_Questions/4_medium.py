# Find the symmetric difference between two sets.

states_1 = {"Gujarat", "Maharashtra", "Odisha", "Mizoram", "Bengal"}
states_2 = {"Gujarat", "Bengal", "Assam", "Goa", "Punjab"}

symmetric_difference = states_1.symmetric_difference(states_2)
print(symmetric_difference)