from pulp import LpProblem, LpStatus


def solve_display_model(model: LpProblem):
    # model.solve()
    print(f"status: {model.status}, {LpStatus[model.status]}")
    print(f"objective: {model.objective.value()}")

    print("variables values")
    for var in model.variables():
        print(f"{var.name}: {var.value()}")

    print("coeficients")
    for var in model.coefficients():
        print(var)

    print("constraints")
    for name, constraint in model.constraints.items():
        print(f"{name}: {constraint.value()}")
