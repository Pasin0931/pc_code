# ตรวจสอบหาตัวเลขซ้ำในลิสต์ (Contains Duplicate)
# เขียนฟังก์ชันชื่อ contains_duplicate ที่รับ input เป็น ลิสต์ของจำนวนเต็ม nums และให้คืนค่าเป็น True หากมีตัวเลขใดๆ ในลิสต์ปรากฏขึ้นมาอย่างน้อยสองครั้ง (มีตัวซ้ำ) แต่ถ้าตัวเลขทุกตัวในลิสต์ไม่ซ้ำกันเลย ให้คืนค่าเป็น False

# ตัวอย่าง:

# contains_duplicate([1, 2, 3, 1]) ควรคืนค่า True (เพราะมีเลข 1 ซ้ำ)

# contains_duplicate([1, 2, 3, 4]) ควรคืนค่า False (เพราะไม่มีเลขซ้ำ)

# contains_duplicate([7, 3, 5, 9, 3, 8]) ควรคืนค่า True (เพราะมีเลข 3 ซ้ำ)

def contains_duplicate(input_temp):
    count_index = 0
    for i in input_temp:
        for j in range(count_index + 1, len(input_temp)):
            if input_temp[j] == i:
                # print(f"Same number {input_temp[j]}, {i}")
                return True
        count_index += 1
    return False
            
print(contains_duplicate([7, 3, 5, 9, 3, 8]))