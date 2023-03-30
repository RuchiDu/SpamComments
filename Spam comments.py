comment = input("Enter your comment")

if ("Make alot of money" in comment):
    spam = True
elif ("buy now" in comment):
    spam = True
elif("subscribe now"):
    spam = True
elif ("buy now" in comment):
    spam = True
else:
    spam = False
if(spam):
    print("This comment is spam")
else :
    print("This comment is not spam")