nums=[56,67,98,45,24]
first=second=None
if len(nums)<2:
    print(-1)
for i in range(len(nums)):
    if first is None or nums[i]>first:
        second=first
        first=nums[i]
    elif second is None or nums[i]>second:
        second=nums[i]
print(second)