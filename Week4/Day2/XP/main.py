# Step 1: Create a set called my_fav_numbers with all your favorites numbers.
my_fav_numbers = {1, 2, 3, 4, 5}

# Step 2: Add two new numbers to the set.
my_fav_numbers.add(6)
my_fav_numbers.add(7)

# Step 3: Remove the last number.
my_fav_numbers.remove(7)

# Step 4: Create a set called friend_fav_numbers with your friend’s favorites numbers.
friend_fav_numbers = {3, 4, 5, 6, 7, 8}

# Step 5: Concatenate my_fav_numbers and friend_fav_numbers to a new variable called our_fav_numbers.
our_fav_numbers = my_fav_numbers | friend_fav_numbers