# ตรวจสอบว่าเป็นคำสลับอักษรหรือไม่ (Valid Anagram)
# เขียนฟังก์ชันชื่อ is_anagram ที่รับสายอักขระ (string) 2 เส้น คือ s และ t ฟังก์ชันนี้ต้องคืนค่า True หาก t เป็นการสลับตำแหน่งตัวอักษรของ s และคืนค่า False ในกรณีอื่นๆ
# Anagram คือ คำหรือวลีที่สร้างขึ้นจากการสลับตำแหน่งตัวอักษรทั้งหมดของคำหรือวลีอื่น เช่น "listen" เป็น anagram ของ "silent"

# เงื่อนไข:
# เราจะถือว่าตัวอักษรพิมพ์เล็กและพิมพ์ใหญ่เป็นคนละตัวกัน
# สตริงจะประกอบด้วยตัวอักษรภาษาอังกฤษเท่านั้น

# ตัวอย่าง:
# is_anagram(s="anagram", t="nagaram") ควรคืนค่า True
# is_anagram(s="rat", t="car") ควรคืนค่า False
# is_anagram(s="listen", t="silent") ควรคืนค่า True

def is_anagram(s, t):
    if len(s) != len(t):
        return True
    else:
        temp1 = []
        temp2 = []

        for i in s:
            temp1.append(i)
        for i in t:
            temp2.append(i)

        temp1.sort()
        temp2.sort()

        for i in range(len(temp1)):
            if temp1[i] != temp2[i]:
                return False
        
        return True

print(is_anagram("listen", "silent"))