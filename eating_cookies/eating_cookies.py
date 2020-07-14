'''
Input: an integer
Returns: an integer
'''
def eating_cookies(n):
    # Your code here
    if n == 0:
        return 1
    
    total_ways = 0
    if n >= 3:
        total_ways += eating_cookies(n-3)
    if n >= 2:
        total_ways += eating_cookies(n-2)
    if n >= 1:
        total_ways += eating_cookies(n-1)
    return total_ways


# print(eating_cookies(0))

if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 5

    print(f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to each {num_cookies} cookies")
