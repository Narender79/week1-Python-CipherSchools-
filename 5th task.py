win=27
num=int(input("Enter the no.: "))
if num==win:
	print("YOU WIN!!!")
else:
	if num>win:
		print("Entered no. is too high")
	else:
		print("Entered no. is too low")