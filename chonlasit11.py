def calculator():
    print("=== เครื่องคิดเลขง่ายๆ ===")
    
    try:
        num1 = float(input("กรอกตัวเลขตัวแรก: "))
        operator = input("เลือกเครื่องหมาย ( + - * / ): ")
        num2 = float(input("กรอกตัวเลขตัวที่สอง: "))

        if operator == '+':
            result = num1 + num2
        elif operator == '-':
            result = num1 - num2
        elif operator == '*':
            result = num1 * num2
        elif operator == '/':
            if num2 == 0:
                print("❌ ไม่สามารถหารด้วยศูนย์ได้")
                return
            result = num1 / num2
        else:
            print("❌ เครื่องหมายไม่ถูกต้อง")
            return

        print(f"ผลลัพธ์: {num1} {operator} {num2} = {result}")

    except ValueError:
        print("❌ กรุณากรอกตัวเลขให้ถูกต้อง")

# เรียกใช้งานฟังก์ชัน
calculator()
