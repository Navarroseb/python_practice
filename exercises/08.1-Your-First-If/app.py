total = int(input('How much money do you have in your pocket\n'))

# ✅ ↓ YOUR CODE HERE ↓ ✅
if total <= 50:
    print("You are a poor guy, go away!")
elif total > 50 and total <= 100:
    print("Buy me some coffee you cheap!")  
elif total >= 101:
    print("Give me your money!")      