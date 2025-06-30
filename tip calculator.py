total_bill = float(input(f"Enter Total Bill Amount : "))
tip_percent = int(input("Enter the tip percentage from the bill : "))
n = int(input("Enter number of persons to share bill between : "))

tip = (tippercent*totalbill)/100

totalbill = totalbill + tip

if n ==0:
	print("Number of persons cannot be 0")
else:
	division = total_bill/n
	
print(f"\n💰Amount to be paid by {n} persons is ${division:.2f}")