def answer(heights):
    minLeft = [0] * len(heights)
    left = 0
    for idx, h in enumerate(heights):
        if left < h:
            left = h
        minLeft[idx] = left
    
    minRight = [0] * len(heights)
    right = 0
    for idx, h in enumerate(heights[::-1]):
        print(heights[::-1])
        if right < h:
            right = h
        minRight[len(heights) - 1 - idx] = right
    water = 0
    for h, l, r in zip(heights, minLeft, minRight):
        water += min([l, r]) - h
   
    return water

print(answer([4,1,3,1,5]))