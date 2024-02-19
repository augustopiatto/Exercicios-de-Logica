# Ainda não entendi, então estou anotando

# We're trying to find the subset of numbers where the sum of any two of them is not divisible by k. Something like (s[i] + s[j]) % k != 0, where s is the original set and i and j are indices of any two distinct elements.
# We create an array with the count of remainders of the divisions between the set elements and k. So if we have a set {1, 2, 4} and k=2, the array will be [2, 1], as we have two elements with remainder 0 and one element with remainder 1. This will make sense in the next steps of the algorithm.
# We need to deal with two special cases before the main part of the algorithm: (1) A number is divisible by k: We can only have up to one number divisible by k in the final subset, as two would violate our requirement ((s[i] + s[j]) % k != 0). Therefore it must be either 1 (if there are any) or 0. (2) k is even: We can only have up to one number divisible by k/2 in the final subset, as two would violate our requirement ((s[i] + s[j]) % k != 0). Therefore it must be either 1 (if there are any) or 0.
# After that we deal with the complementary remainders. Since we're dealing with an array of remainders, if we iterate through the array, i will be the complementary remainder of k - i. If we keep both complementary remainders, it would violate our requirement (since their sum is divisible by k), so we keep only the one with the largest count (remember we want to return the largest subset that satisfies the requirement).
# As for your questions:
# If i % k == 0, then i is divisible by k;
# See the special case (2) above;
# We actually iterate through the entire array, but comparing two elements on each step (so we need half the steps): notice on each step we're comparing i and k-i (the complementary remainders), and the array with the remainders is always of length k. E.g.: if k is 4, the array is [w, x, y, z] (where w, x, y, z are natural numbers); on the first step you compare w and z, then x and y.

def non_divisible_subset(k, s):
    remainderArr = [0] * k
    for i in s:
        remainderArr[i % k] += 1

    maxLength = 0
    maxLength += min(remainderArr[0], 1)

    if k % 2 == 0:
        maxLength += min(remainderArr[k//2], 1)

    for i in range(1, k//2 + 1):
        if i != k - i:
            maxLength += max(remainderArr[i], remainderArr[k - i])

    return maxLength


def test_non_divisible_subset():
    result = non_divisible_subset(
        7, [278, 576, 496, 727, 410, 124, 338, 149, 209, 702, 282, 718, 771, 575, 436])

    assert result == 11
