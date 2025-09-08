# เขียนฟังก์ชันที่รับค่าเป็นลิสต์ของจำนวนเต็ม nums และจำนวนเต็ม target ให้หา ดัชนี (index) ของตัวเลข 2 ตัวในลิสต์ที่บวกกันแล้วได้เท่ากับ target พอดี และคืนค่าเป็นลิสต์ของดัชนีทั้งสอง

# เงื่อนไข:
# สมมติว่าในแต่ละ input จะมีคำตอบที่ถูกต้องเพียงหนึ่งเดียวเสมอ
# ห้ามใช้ตัวเลขในตำแหน่งเดียวกันซ้ำสองครั้ง

# ตัวอย่าง:
# two_sum(nums=[2, 7, 11, 15], target=9) ควรคืนค่า [0, 1] เพราะ nums[0] + nums[1] == 9


def two_sum(nums, target):
    count_index = 0
    for i in range(len(nums)):
        for j in range(count_index + 1, len(nums)):
            # print(i, nums[j])
            if nums[i] + nums[j] == target:
                # print(f"{nums[i]} + {nums[j]} = {target}")
                return [i, j]
        count_index += 1

# print(two_sum([2, 7, 11, 15], 9))

# ตัวอย่าง
# ตัวอย่างที่ 1
nums1 = [2, 7, 11, 15]
target1 = 9
print(f"จากลิสต์ {nums1} และ target {target1}")
print(f"ผลลัพธ์คือ: {two_sum(nums1, target1)}")  # ผลที่คาดหวัง: [0, 1]

print("-" * 20)

# ตัวอย่างที่ 2
nums2 = [3, 2, 4]
target2 = 6
print(f"จากลิสต์ {nums2} และ target {target2}")
print(f"ผลลัพธ์คือ: {two_sum(nums2, target2)}")  # ผลที่คาดหวัง: [1, 2]

print("-" * 20)

# ตัวอย่างที่ 3
nums3 = [3, 3]
target3 = 6
print(f"จากลิสต์ {nums3} และ target {target3}")
print(f"ผลลัพธ์คือ: {two_sum(nums3, target3)}")  # ผลที่คาดหวัง: [0, 1]