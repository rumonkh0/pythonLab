def calculate_tax(income):
  total_tax = 0

  if income <= 10000:
    total_tax = income * 0.05
  elif income <= 50000:
    total_tax = 10000 * 0.05 + (income - 10000) * 0.1
  elif income <= 100000:
    total_tax = 10000 * 0.05 + 40000 * 0.1 + (income - 50000) * 0.2
  else:
    total_tax = 10000 * 0.05 + 40000 * 0.1 + 50000 * 0.2 + (income - 100000) * 0.3

  return total_tax

if __name__ == "__main__":
  income = float(input("Enter your annual income: "))
  tax = calculate_tax(income)
  print("Total tax amount:", tax)