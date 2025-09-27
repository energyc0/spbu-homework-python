## Complexity of queen permutation solutions

### Brute force solution

To generate a permutation we need: $$ O(n) $$
at the next step we need: $$ O(n-1) $$
to check if it is a good permutation we need: $$ Θ(n*n/2) $$
the number of permutations: $$ n! $$

As a **result**: $$ O(n! * n^2) $$

### Recursive solution

To choose a new position for queen we need: $$ O(n) $$
at the next step we need: $$ O(n-1) $$
to go through the possible permutations we need: $$ O(n!) $$
to check if it is a good position for a new permutation we need $$ O(n) $$

As a **result**: $$ O(n! * n) $$

### Bitset solution

To go through all possible positions at one step we need: $$ O(n) $$
to go through all possible positions at the next step we need: $$ O(n-1) $$
to check if it is a good permutation we need: $$ O(1) $$

As a **result**: $$ O(n!) $$