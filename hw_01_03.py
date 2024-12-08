# input format %d, %d, %d
width, height, size = map(int, input().split(sep=','))

size_in = lambda h, w: not size % w and h >= (size / w)
print(size_in(width, height) or size_in(height, width))
