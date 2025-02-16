#https://serpapi.com/blog/scrape-google-play-store-app-in-python/


n = 3
numbers = list(range(n ** 2))

diagRL = [num for num in numbers if num % (n - 1) == 0 and num != 0]
print(diagRL)