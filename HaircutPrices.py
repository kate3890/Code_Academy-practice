hairstyles = ["bouffant", "pixie", "dreadlocks", "crew", "bowl", "bob", "mohawk", "flattop"]

prices = [30, 25, 40, 20, 20, 35, 50, 35]

last_week = [2, 3, 5, 8, 4, 4, 6, 2]

total_price = 0
for price in prices:
  price + 1
  print(price)
  total_price +=price
print("Total price is:" + " "+str(total_price))

average_price = total_price/2
print("Average Haircut Price:" + " "+ str(average_price))

new_price = [num -5 for num in prices]
print(new_price)

#Add the product of prices[i] (
#the price of the haircut at position i) and last_week[i] 
# (the number of people who got the haircut at position i) to 
# total_revenue at each step.

total_revenue = 0
for i in range(len(hairstyles)):
  total_revenue += prices[i] * last_week[i]
  print("Total Revenue:"+" "+str(total_revenue))

average_daily_revenue = total_revenue/7
print("Average Daily Revenue is:"+ " "+str(average_daily_revenue))

#FInd and advertise all the prices under 30 

cuts_under_30 = [hairstyles[i] for i in range(len(prices)) if prices[i] < 30]
print(cuts_under_30)

