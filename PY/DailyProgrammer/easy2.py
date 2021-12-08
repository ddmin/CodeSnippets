# [Easy] Challenge 2

print("== Newton's Second Law Calculator ==")
print("Omit the variable to solve for.")
print()

print("Force:")
f = input("> ")
print()

print("Mass:")
m = input("> ")
print()

print("Acceleration:")
a = input("> ")
print()

if not f:
    print('f = ' + str(float(m) * float(a)))

elif not m:
    print('m = ' + str(float(f) / float(a)))

elif not a:
    print('a = ' + str(float(f) / float(m)))
