for x in range(1, 10):
  # Outer loop iterates through rows (multiplication factors)
  for y in range(1, 10):
    # Inner loop iterates through columns (other factors)
    product = x * y
    print(f"{x} x {y} = {product}", end="\t")  # Print with tabs for better formatting
  print()  # Move to a new line after each row
