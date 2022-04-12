from cupcakes import per_day_income
cost_per_cupcake=25
made1=input("How many cupcakes were made on day 1? ")
made1=int(made1)
spoilt1=input("How many cupcakes were spoilt on day 1?")
spoilt1=int(spoilt1)
print("Day 1:")
per_day_income(made1,spoilt1,cost_per_cupcake)
made2=input("How many cupcakes were made on day 2? ")
made2=int(made2)
spoilt2=input("How many cupcakes were spoilt on day 2?")
spoilt2=int(spoilt2)
print("Day 2:")
per_day_income(made2,spoilt2,cost_per_cupcake)

