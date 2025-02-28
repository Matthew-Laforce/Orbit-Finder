# Orbit-Finder
When applying the multiplier theorem to an (n, k, λ)-difference set, one may wish to find the orbits which result given some multiplier. This python script finds and prints those orbits, given that 'n' is set to the number of elements, and given that 'q' is the multiplier.

Example: setting n=21 and q=2, the script prints the following:
"Orbits found: [[0], [1, 2, 4, 8, 16, 11], [3, 6, 12], [5, 10, 20, 19, 17, 13], [7, 14], [9, 18, 15]]"

This matches the orbits one would expect when using repeated multiplication on Z_{21} in the form 2x, 2^2x, etc.. 
