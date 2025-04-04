total_hight=0
hight=input("Enter List of hight seperated by commas ',': ")
hight_list=hight.split(',')
list_length= len(hight_list)
for i in range(list_length):
    hight_list[i]=int(hight_list[i])
    total_hight+=hight_list[i]
ave_hight=round(total_hight/list_length)
print("Average Hight of list is",ave_hight)

