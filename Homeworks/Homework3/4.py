

years = [
    [2020, 2.3, 2.2, 1.8, 3.1],
    [2021, 2.4, 2.0, 1.7, 3.0],
    [2022, 1.7, 1.2, 1.0, 1.8],
    [2023, 1.9, 1.0, 0.7, 2.0],
    [2024, 2.0, 2.4, 2.0, 3.2]
    ]
print("4a.")
for x in years:
    sum_of_year = sum(x[1:])
    print("Sum of year " + str(x[0]) + " is: " + str(sum_of_year) + " million")

q1 = []
q2 = []
q3 = []
q4 = []

for x in years:
    quarter1 = x[1]
    q1.append(quarter1)
    quarter2 = x[2]
    q2.append(quarter2)
    quarter3 = x[3]
    q3.append(quarter3)
    quarter4 = x[4]
    q4.append(quarter4)

averageq1 = sum(q1) / len(q1)
averageq2 = sum(q2) / len(q2)
averageq3 = sum(q3) / len(q3)
averageq4 = sum(q4) / len(q4)
print("4b.")
print("Average sales per quarters are: " + str(averageq1) + " million in the 1st quarter, " + str(averageq2) + " million in the 2nd quarter, " + str(averageq3) + " million in the 3rd quarter, and " + str(averageq4) + " million in the 4th quarter.")

print("4c.")
for x in years:
    max_sales = max(x[1:])
    min_sales = min(x[1:])
    print("In " + str(x[0]) + " max sales are " + str(max_sales) + " million, and the min sales are: " + str(min_sales) + " million.")