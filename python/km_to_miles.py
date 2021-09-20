#This will accept user input, convert KM to miles, then round the answer before returning it to the user

print("How many kilometers did you run today?")
kms = input()
miles = float(kms)/1.60934
miles = round(miles, 2)
print(f"That is equal to {miles} miles")


