while True:

    x1, y1, x2, y2 = map(int, input().split())
    
    if x2 <= x1 or y2 <= y1:
        break

    area = (x2 - x1) * (y2 - y1)
    print(area)