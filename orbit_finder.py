""" ============================================================================

MATH 322 -- Assignment 3 -- Q5 Orbit Finder
Matthew Laforce
Created Jan 28, 2025

============================================================================ """

# Set the desired number of values (n), multiplier (q)
n = 21
q = 2

# Populate the first value set
unused = []
orbits = []
index = 0
while (index < n):
    unused.append(index)
    index += 1
    
# Sort the values from 'unused_1' into orbits
while (len(unused) != 0):
    current_val = unused.pop(0)
    new_orbit = [current_val]
    exponent = 1
    # Loop through possible values until reaching a repetition point 
    while (current_val != ((q**exponent)*current_val)%n and 
           ((q**exponent)*current_val)%n in unused):
        if (((q**exponent)*current_val)%n) in unused:
            unused.remove(((q**exponent)*current_val)%n)
            new_orbit.append(((q**exponent)*current_val)%n)
        exponent += 1
    orbits.append(new_orbit)
print(f"Orbits found: {orbits}")
