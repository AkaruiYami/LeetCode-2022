"""
Koko loves to eat bananas. There are n piles of bananas, the ith pile has piles[i] bananas. The guards have gone and will come back in h hours.

Koko can decide her bananas-per-hour eating speed of k. Each hour, she chooses some pile of bananas and eats k bananas from that pile. If the pile has less than k bananas, she eats all of them instead and will not eat any more bananas during this hour.

Koko likes to eat slowly but still wants to finish eating all the bananas before the guards return.

Return the minimum integer k such that she can eat all the bananas within h hours.
"""
import math


def min_eating_speed(piles: list[int], h: int) -> int:
    if len(piles) >= h:
        return max(piles)
    elif len(piles) == 1:
        return math.ceil(piles[0] / h)

    speed = 1
    while True:
        hour_taken = 0
        for e in piles:
            hour_taken += math.ceil(e / speed)
            if hour_taken > h:
                break
        if hour_taken <= h:
            return speed
        else:
            speed += 1


r1 = min_eating_speed(piles=[3, 6, 7, 11], h=8)
r2 = min_eating_speed(piles=[30, 11, 23, 4, 20], h=5)
r3 = min_eating_speed(piles=[30, 11, 23, 4, 20], h=6)
r4 = min_eating_speed(piles=[312884470], h=312884469)
r5 = min_eating_speed(
    piles=[
        332484035,
        524908576,
        855865114,
        632922376,
        222257295,
        690155293,
        112677673,
        679580077,
        337406589,
        290818316,
        877337160,
        901728858,
        679284947,
        688210097,
        692137887,
        718203285,
        629455728,
        941802184,
    ],
    h=823855818,
)
