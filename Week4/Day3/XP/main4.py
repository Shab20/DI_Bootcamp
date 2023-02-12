users = ["Mickey","Minnie","Donald","Ariel","Pluto"]

# Solution for 1.
disney_users_A = {}
for i, user in enumerate(users):
    disney_users_A[user] = i
print(disney_users_A)

# Solution for 2.
disney_users_B = {}
for i, user in enumerate(users):
    disney_users_B[i] = user
print(disney_users_B)

# Solution for 3.
disney_users_C = {}
sorted_users = sorted(users)
for i, user in enumerate(sorted_users):
    disney_users_C[user] = i
print(disney_users_C)

# Solution for 4.1.
disney_users_D = {}
for i, user in enumerate(users):
    if "i" in user:
        disney_users_D[user] = i
print(disney_users_D)

# Solution for 4.2.
disney_users_E = {}
for i, user in enumerate(users):
    if user.startswith("m") or user.startswith("p"):
        disney_users_E[user] = i
print(disney_users_E)