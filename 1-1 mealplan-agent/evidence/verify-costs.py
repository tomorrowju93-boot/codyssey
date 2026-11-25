# Offline verification of recorded estimated purchase row costs, KRW.
# Separate evaluator-side verification; not a tool used by Gemini.
rows = {
    'zero_shot': [15000,2500,3500,2000,3000,13000,11000,18000,7500,5500,4000,4500,2000,7500,1800,3000,3500,4000,2000,1500,1500,3500,3000,2000,1500,1500,8000,5500,6500,2000,7500,5500],
    'v1_initial': [16000,3500,4500,19500,19800,7500,9900,6000,7500,5200,3800,3500,3000,3500,2500,4500,5800,2500,6500,5500,4500,3500,8000],
    'v1_changed': [16000,3500,4500,14300,19800,7500,9900,6000,7500,5200,3800,3500,3000,2200,4500,5800,2500,6500,5500,6500,6000],
    'v2_initial': [9000,2500,2000,3000,8500,22000,4500,18000,7500,2800,2500,3500,1500,3500,2500,2800,2500,1800,1200,1500,7500,1800,2000,7500,6500,2800,2500,4000,2000,5500],
}
rows['v2_changed'] = rows['v2_initial'][:8] + rows['v2_initial'][9:]
reported = [163000,156900,139900,132400,124900]
budgets = [200000,200000,150000,200000,150000]
reserves = [0,20000,10000,30000,15000]
for (name, values), ai, budget, reserve in zip(rows.items(), reported, budgets, reserves):
    total = sum(values)
    print(name, 'rows:', len(values), 'AI:', ai, 'sum:', total, 'absolute error:', abs(ai-total), 'available:', budget-total-reserve)
