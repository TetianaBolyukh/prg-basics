results = [37,51,44,23,78,92,39,84,83,51]

def min_pts(limit):
   return lambda pts: pts>=limit

sev_result = list(filter(min_pts(70),results))
four_result = list(filter(min_pts(40),results))
thr_result = list(filter(min_pts(30),results))

print(f"""Min 70 pts: {sev_result} 
Min 40 pts: {four_result} 
Min 30 pts:  {thr_result}""")