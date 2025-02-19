from pulp import LpMaximize, LpProblem, LpVariable

# Creating a model
model = LpProblem(name="maximize_drink_production", sense=LpMaximize)

# Decision variables: number of units of Lemonade (L) and Fruit Juice (F) produced
L = LpVariable(name="Lemonade", lowBound=0, cat="Integer")
F = LpVariable(name="Fruit_Juice", lowBound=0, cat="Integer")

# The objective function is to maximize the total number of products produced
model += L + F, "Total_Production"

# Resource limitations
model += (2 * L + 1 * F <= 100, "Water_Limit")
model += (1 * L <= 50, "Sugar_Limit")
model += (1 * L <= 30, "Lemon_Juice_Limit")
model += (2 * F <= 40, "Fruit_Puree_Limit")

model.solve()

if __name__ == "__main__":
    print(f"Optimal production:")
    print(f"Lemonade: {L.varValue}")
    print(f"Fruit Juice: {F.varValue}")