nums=[3,4,6,5,7]
sort=True
for i in range(len(nums)-1):
    if nums[i]>nums[i+1]:
        sort=False
print(sort)