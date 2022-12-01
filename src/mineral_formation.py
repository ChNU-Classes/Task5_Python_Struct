def mineral_formation(stones):
    if sum(stones[0]) == 0 and sum(stones[len(stones)-1]) != 0:
        return "stalagmites"
    if sum(stones[0]) != 0 and sum(stones[len(stones) - 1]) == 0:
        return "stalactites"
    if sum(stones[0]) != 0 and sum(stones[len(stones) - 1]) != 0:
        return "both"

