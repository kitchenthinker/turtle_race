import random
from turtle import Turtle, Screen


class TurtleRacer:

    def __init__(self, v_name, v_colour):
        self.player = Turtle(shape="turtle")
        self.player.color(v_colour)
        self.player_name = v_name
        self.player_colour = v_colour
        self.player.penup()


screen = Screen()
screen.setup(width=500, height=400)
turtle_names = ['Timmy', 'Jimmy', 'Barry', 'Harry', 'Molly', 'Dolly']
turtle_colours = ["red", "blue", "yellow", "green", "orange", "purple"]

players_list = []
for x in range(len(turtle_names)):
    colour = turtle_colours[x]
    name = turtle_names[x]
    new_player = TurtleRacer(name, colour)
    players_list.append(new_player)


def start_game():
    user_bet = screen.textinput(title="Make your bet.", prompt="Which turtle will win the race? Enter a colour: ")
    start_position_x = - (screen.window_width() / 2) + 10
    start_position_y = -10 * (len(players_list) + 1)
    for x_player in players_list:
        x_player.player.setposition(start_position_x, start_position_y)
        start_position_y += 25

    is_race_on = False
    winner = None

    if user_bet:
        is_race_on = True
    screen_end_position = screen.window_width() / 2

    while is_race_on:
        x_item = random.choice(players_list)
        x_item.player.forward(random.randint(0, 10))
        x_pos_player = x_item.player.position()[0]
        if x_pos_player > screen_end_position:
            is_race_on = False
            winner = x_item
            break

    game_end_str = f"turtle '{winner.player_name}', colour:'{winner.player_colour}' won the race"
    if user_bet == winner.player_colour:
        screen.title("You win! " + game_end_str)
    else:
        screen.title("You lose! " + game_end_str)


screen.listen()
screen.onkey(fun=start_game, key="s")
screen.exitonclick()
