

def isPalindrome(num):
    listNum = list(str(num))
    listNum.reverse()
    return str(num) == "".join(listNum)

def getMaxPalindrome():
    products = {}
    for i in range(100,1000):
        for j in range(10,1000):
            product = i*j
            if (isPalindrome(product)):
                products[product]= (i,j)
    maxProduct = max(products, key=int)
    return (maxProduct, products[maxProduct])

print(getMaxPalindrome())