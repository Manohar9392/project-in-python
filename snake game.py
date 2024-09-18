from turtle import Turtle,Screen
from snake_class import Snake
from food import Food
from scoreboard import Scoreboard

import time
screen=Screen()
screen.setup(600,600)
screen.tracer(0)#it will stop animation
snake=Snake()
food=Food()
scoreboard=Scoreboard()
screen.listen()
screen.onkey(snake.up,"Up" )
# screen.onkey(snake.up,"w" )
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")





#movement of snake
is_game_over=True
while is_game_over:
    screen.update()#it will show screen
    time.sleep(0.1)
    snake.move()
    if snake.segments[0].distance(food)< 20:
        food.refresh()
        scoreboard.increase_score()
        snake.add_segment()

    if snake.segments[0].xcor()>280 or snake.segments[0].xcor() <-280 or snake.segments[0].ycor()>280 or snake.segments[0].ycor()<-280:
        is_game_over=False
        scoreboard.game_over()

#detect collision with tail
    for i in snake.segments:
        if i== snake.segments[0]:
            pass

        elif snake.segments[0].distance(i) <10:
                is_game_over = False
                scoreboard.game_over()


















screen.exitonclick()