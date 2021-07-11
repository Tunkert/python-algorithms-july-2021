nums1 = [2]
nums2 = []

# output 2.00000

# append 2nd array onto first array (create function as well)
def median_two_arrays(nums1, nums2):
    for num2 in nums2:
        nums1.append(num2)
    nums1.sort()
    if len(nums1) % 2 == 0:
        x = int(len(nums1) / 2)
        return("{:.5f}".format((float((nums1[x - 1] + nums1[x]) / 2))))
    else:
        x = int((len(nums1) - 1) / 2)
        return("{:.5f}".format((float(nums1[x]))))

print(median_two_arrays(nums1, nums2))


