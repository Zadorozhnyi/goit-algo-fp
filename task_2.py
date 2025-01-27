import turtle
import math

def draw_branch(t, length, depth):
    if depth == 0:
        return
    
    # Малюємо стовбур
    t.forward(length)
    
    # Зберігаємо позицію та напрямок
    position = t.pos()
    heading = t.heading()
    
    # Ліва гілка
    t.left(30)
    draw_branch(t, length * 0.7, depth - 1)
    
    # Відновлюємо позицію та напрямок
    t.penup()
    t.goto(position)
    t.setheading(heading)
    t.pendown()
    
    # Права гілка
    t.right(30)
    draw_branch(t, length * 0.7, depth - 1)

def main():
    recursion_depth = int(input("Введіть рівень рекурсії: "))
    screen = turtle.Screen()
    screen.setup(width=900, height=900)
    screen.bgcolor("white")
    
    t = turtle.Turtle()
    t.speed(0)
    t.color("brown")
    t.penup()
    t.goto(0, -300)
    t.pendown()
    t.left(90)
    
    # Малюємо фрактальне дерево
    draw_branch(t, 150, recursion_depth)
    
    screen.mainloop()

if __name__ == "__main__":
    main()
