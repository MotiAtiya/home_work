prices = [20, 75, 120, 45, 90]

expensive = list(filter(lambda n: n > 50, prices))
raised = list(map(lambda n: n+10, expensive))
print(raised)
