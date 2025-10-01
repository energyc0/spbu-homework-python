## Complexity of queen permutation solutions

### Brute force solution

To generate a permutation we need: $\mathbb{O}(n) $,
at the next step we need: $ \mathbb{O}(n-1) $,
to check if it is a good permutation we need: $ \Theta(\frac{n^2}{2}) $,
the number of permutations: $ n! $.

As a **result**: $ \mathbb{O}(n! * n^2) $.

### Recursive solution

To choose a new position for queen we need: $ \mathbb{O}(n) $,
at the next step we need: $ \mathbb{O}(n-1) $,
to go through the possible permutations we need: $ \mathbb{O}(n!) $,
to check if it is a good position for a new permutation we need $ \mathbb{O}(n) $.

As a **result**: $ \mathbb{O}(n! * n) $.

### Bitset solution

To go through all possible positions at one step we need: $ \mathbb{O}(n) $,
to go through all possible positions at the next step we need: $ \mathbb{O}(n-1) $,
to check if it is a good permutation we need: $ \mathbb{O}(1) $.

As a **result**: $ \mathbb{O}(n!) $.