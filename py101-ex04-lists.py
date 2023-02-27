# Lists - Exercise - selling lemonade
# - you sell lemonade over 2 weeks, the list shows number of lemonade sold per week
# - Profit for each lemonade sold is 1.5$
# + Add another day to week 2 list by capturing a number as input
# + Combine the two lists into the list called 'sales'
# + Calculate / Print how much you have earned on :
#   - Best Day
#   - Worst Day
#   - Separately and in total
# (hint: 3 prints in total)

sales_w1 = [7,3,42,19,15,35,9]
sales_w2 = [12,4,26,10,7,28]
sales = []
new_day = input('Enter #of lemonades for new day: ')
sales_w2.append(int(new_day))
#sales.extend(sales_w1)
#sales.extend(sales_w2)
sales = sales_w1 + sales_w2
#sales.sort()
worst_day_prof = min(sales) * 1.5
best_day_prof = max(sales) * 1.5
print(f'Worst day profit:$ {worst_day_prof}')
print(f'Best day profit:$ {best_day_prof}')
print(f'Combined profit:$ {worst_day_prof + best_day_prof}')