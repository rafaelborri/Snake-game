import turtle
import random

#window
window = turtle.Screen()
window.screensize(600, 600, "light green")

#snake
snake = turtle.Turtle()
snake.penup()
snake_size = 2
snake.color("dark green")
snake.shapesize(snake_size)

#Read high score
f = open("high_score.txt", "r")
high_score = f.read()
high_score = int(high_score)
f.close()

#Food
apple = turtle.Turtle()
apple.penup()
apple.shape("circle")
apple.color("red")

def right():
    snake.right(90)

def left():
    snake.left(90)

score = 0

def main(score):
    apple.goto(random.randint(-300, 300), random.randint(-300, 300))
    while True:
        snake.forward(2)
        window.onkeypress(right, "d")
        window.onkeypress(left, "a")
        window.listen()
        if snake.position() == apple.position():
            score += 1
            apple.goto(random.randint(-300, 300), random.randint(-300, 300))
            snake.shapesize(int(snake_size) + 1)

        if snake.ycor() >= 300:
            if score > high_score:
                print("You have a new high score!!!\nYour last high score is ", high_score, "\nYou new high score is ", score)
                f = open("high_score.txt", "w")
                f.write(str(score))
                f.close()
            else:
                print("Your high score is ", high_score, "\n Your score is ", score)
            break
        if snake.ycor() <= -300:
            if score > high_score:
                print("You have a new high score!!!\nYour last high score is ", high_score, "\nYou new high score is ",
                      score)
                f = open("high_score.txt", "w")
                f.write(str(score))
                f.close()
            else:
                print("Your high score is ", high_score, "\n Your score is ", score)
            break
        if snake.xcor() >= 300:
            if score > high_score:
                print("You have a new high score!!!\nYour last high score is ", high_score, "\nYou new high score is ",
                      score)
                f = open("high_score.txt", "w")
                f.write(str(score))
                f.close()
            else:
                print("Your high score is ", high_score, "\n Your score is ", score)
            break
        if snake.xcor() <= -300:
            if score > high_score:
                print("You have a new high score!!!\nYour last high score is ", high_score, "\nYou new high score is ",
                      score)
                f = open("high_score.txt", "w")
                f.write(str(score))
                f.close()
            else:
                print("Your high score is ", high_score, "\n Your score is ", score)
            break


if __name__ == '__main__':
    main(score)