	
def recMC(coinValueList,change):
   minCoins = change
   if change in coinValueList:
     return 1
   else:
       coinlist = []
       for c in coinValueList:
          if c <= change:
              coinlist.append(c)

       for i in coinlist:
           numCoins = 1 + recMC(coinValueList,change-i)
           if numCoins < minCoins:
               minCoins = numCoins
   return minCoins

print(recMC([1,5,10,25],6))
