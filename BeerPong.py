import time

from BeerPong_classes import *


def bp_game_loop(username: str):
    display.set_caption("Efrarcade - Water Pong")
    scene = display.set_mode((700, 500), RESIZABLE)
    background = image.load("./assets/Bar background.jpg")  # Creates a surface for the background of the game
    background = transform.scale(background, (700, 500))
    is_active = True  # Elementary boolean that stays True until QUIT event is triggered.
    clock = time.Clock()
    game = Game()
    game.vector.graphical_rotation(0, 1, game.ball)  # Does the initial rotation of the arrow-vector representing
    print(game.ball.trajectory)  # Trajectory calculation test.
    # the trajectory's input.
    while is_active:
        clock.tick(1000)
        scene.blit(background, (0, 0))  # Draws background.
        game.game_sprites.update()
        game.game_sprites.draw(scene)
        display.flip()  # Draws every graphical element of the game.
        if game.launch == 1:
            # This condition verifies that the game is in the ball launching state.
            if not game.ball.launch():
                # If it is, triggers the launch method of the ball until it reaches its end point or collides with
                # Specific rectangles.
                game.launch = 0
        else:
            # If the launch mode is off, automatically puts back the ball to the top of the glass.
            game.ball.rect.center = game.player_glass.rect.midtop

        for thing in event.get():
            if thing.type == QUIT:
                # If quitting event detected, closes the windows
                is_active = False
                quit()
            if thing.type == KEYDOWN:
                # Before the launch of the ball, lets the player adjust the acceleration that the ball will have
                # as well as its angle to maximise the accuracy of the trajectory.
                if thing.key == K_LEFT and not game.launch:
                    game.vector.graphical_rotation(game.vector.angle + 1, game.vector.acceleration, game.ball)
                if thing.key == K_RIGHT and not game.launch:
                    game.vector.graphical_rotation(game.vector.angle - 1, game.vector.acceleration,
                                                   game.ball)
                if thing.key == K_UP and not game.launch:
                    game.vector.graphical_rotation(game.vector.angle, game.vector.acceleration + 1,
                                                   game.ball)
                if thing.key == K_DOWN and not game.launch:
                    game.vector.graphical_rotation(game.vector.angle, game.vector.acceleration - 1,
                                                   game.ball)
                if thing.key == K_SPACE and not game.launch:
                    # If the game hasn't launched the ball and space is pressed, launches the ball.
                    game.ball.trajectory_calculation(game.vector.angle, game.vector.acceleration)
                    # Interessant tuple of values to get into glass (72, 17), (67,16)
                    game.launch = 1

bp_game_loop("Test")
