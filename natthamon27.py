import turtle

# ตั้งค่าหน้าจอ
screen = turtle.Screen()
screen.bgcolor("white")

# สร้างเต่า (Turtle) ที่ใช้วาด
pen = turtle.Turtle()
pen.shape("turtle")
pen.color("red")
pen.speed(2)

# วาดรูปหัวใจ
pen.begin_fill()
pen.left(50)
pen.forward(133)
pen.circle(50, 200)
pen.right(140)
pen.circle(50, 200)
pen.forward(133)
pen.end_fill()

# ปิดหน้าต่างเมื่อคลิก