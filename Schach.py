#https://www.youtube.com/watch?v=dQw4w9WgXcQ&list=RDdQw4w9WgXcQ 

import pygame 
pygame.init()

scale_factor = 8
screen_width = 1920
screen_lenght = 1080
board_size = 128
piece_size = 16
tile_size = 16 * scale_factor


screen = pygame.display.set_mode((screen_width, screen_lenght))             
pygame.display.set_caption("Schach")                       
clock = pygame.time.Clock()



#------------------Hier befinden sich alle meine Classes---------------------------------------------

class Chess_Board:

    def __init__(self):
        self.colour = self.get_opponent_colour()
        self.board = self.get_standartaufstellung(self.colour)
       
        self.board_img = pygame.image.load("Board.png")
        self.board_img = pygame.transform.scale(self.board_img, (128 * scale_factor, 128 * scale_factor))

        self.board_pos = [(screen_width - board_size * scale_factor) / 2, (screen_lenght - board_size * scale_factor) / 2] 
        
        self.indicator_visible = False
        self.moves = []

        self.bounce = -15
        self.bounce_factor = 0.2

    def finish_setup(self):
        self.board = self.create_piece_objects(self.board)

    def return_pos(self):
        return self.board_pos
    
    def return_board(self):
        return self.board

    def blit_board(self):
        screen.blit(self.board_img, (self.board_pos[0], self.board_pos[1]))

    def blit_pieces(self):
        for row in self.board:
            for piece in row:
                if piece != 0:
                    piece.blit_piece()
    
    def get_opponent_colour(self):
        colour = "white"
        return colour

    def get_standartaufstellung(self, colour):
        board = []

        if colour == "white":
            board = [
                ["b_rook", "b_knight", "b_bishop", "b_queen", "b_king", "b_bishop", "b_knight", "b_rook"],
                ["b_pawn", "b_pawn", "b_pawn", "b_pawn", "b_pawn", "b_pawn", "b_pawn", "b_pawn"],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                ["w_pawn", "w_pawn", "w_pawn", "w_pawn", "w_pawn", "w_pawn", "w_pawn", "w_pawn"],
                ["w_rook", "w_knight", "w_bishop", "w_queen", "w_king", "w_bishop", "w_knight", "w_rook"]
            ]
        elif colour == "black":
            board = [

                ["w_rook", "w_knight", "w_bishop", "w_king", "w_queen", "w_bishop", "w_knight", "w_rook"],
                ["w_pawn", "w_pawn", "w_pawn", "w_pawn", "w_pawn", "w_pawn", "w_pawn", "w_pawn"],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                ["b_pawn", "b_pawn", "b_pawn", "b_pawn", "b_pawn", "b_pawn", "b_pawn", "b_pawn"],
                ["b_rook", "b_knight", "b_bishop", "b_king", "b_queen", "b_bishop", "b_knight", "b_rook"],

            ]
        else:
            print("fehler weil keine gültige Farbe eingegeben wurde. Gültig sind black oder white")
        return board

    def create_piece_objects(self, board):
        for y, row in enumerate(board):
            for x, square in enumerate(row):
                if square == 0:
                    pass
                else:
                    relative_pos = [x, y]
                    name = str(square)
                    board[y][x] = Piece(name, relative_pos)
        return board

    def get_and_show_moves(self, events, mouse_pos):
        self.get_moves(events, mouse_pos)
        self.show_moves()

    def get_moves(self, events, mouse_pos):
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_relative_pos = self.get_relative_mouse_pos(mouse_pos)
                actual_field = self.check_if_this_is_a_field(mouse_relative_pos)
                if not actual_field:
                    self.moves = []
                    self.toggle_indicator_visibility()
                    break
                piece_in_field = self.check_if_there_is_a_piece_there(mouse_relative_pos)
                if not piece_in_field:
                    self.moves = []
                    self.toggle_indicator_visibility()
                    break
                self.toggle_indicator_visibility()
                self.moves = []
                self.moves = self.board[mouse_relative_pos[1]][mouse_relative_pos[0]].get_possible_moves()

    def show_moves(self):
        if self.indicator_visible:
            for i in range(len(self.moves)):
                yposition = self.moves[i][0]
                xposition = self.moves[i][1]
                possible_move_indicator = dekomanager.return_possible_move_indicator()
                xposition, yposition = self.calculate_actual_pos(xposition, yposition)
                self.bounce_indicator()
                screen.blit(possible_move_indicator, (xposition , yposition + self.bounce))

    def bounce_indicator(self):
        self.bounce -= self.bounce_factor
        if self.bounce < -40 or self.bounce > -10:
            self.bounce_factor *= -1

    def get_relative_mouse_pos(self, mouse_pos_tuple):
        mouse_pos = []
        mouse_pos.append(mouse_pos_tuple[0])
        mouse_pos.append(mouse_pos_tuple[1])
        mouse_pos[0] -= self.board_pos[0]
        mouse_pos[1] -= self.board_pos[1]
        mouse_pos[0] = int(mouse_pos[0] / (scale_factor * 16))
        mouse_pos[1] = int(mouse_pos[1] / (scale_factor * 16))
        return mouse_pos
 
    def calculate_actual_pos(self, xposition, yposition):
        xposition, yposition = self.board_pos[0] + (xposition * tile_size), self.board_pos[1] + (yposition * tile_size) 
        return xposition, yposition
    
    def toggle_indicator_visibility(self):
        if not self.indicator_visible:
            self.indicator_visible = True
        elif self.indicator_visible:
            self.indicator_visible = False 

    def check_if_this_is_a_field(self, relative_mouse_pos):
        if relative_mouse_pos[0] <= 7 and relative_mouse_pos[0] >= 0:
            if relative_mouse_pos[1] <= 7 and relative_mouse_pos[1] >= 0:
                return True
        return False
    
    def check_if_there_is_a_piece_there(self, mouse_relative_pos):
        if self.board[mouse_relative_pos[1]][mouse_relative_pos[0]] == 0:
            return False
        return True

class Piece:
    
    def __init__(self, name, relative_pos):
        
        self.name = name
        self.piece_img = pygame.image.load(name + ".png")
        self.piece_img = pygame.transform.scale(self.piece_img, (piece_size * scale_factor, piece_size * scale_factor))
        self.colour = name[0]
    
        self.relative_pos = relative_pos
        self.pos = self.calculate_actual_pos()
    
    def blit_piece(self):
        screen.blit(self.piece_img, (self.pos[0], self.pos[1]))

    def return_name(self):
        return str(self.name)  

    def get_board_coords(self):
        board_pos = board.return_pos() 
        return board_pos 

    def calculate_actual_pos(self):
        board_pos = self.get_board_coords()
        position = [0, 0]
        position[0] = self.relative_pos[0]
        position[1] = self.relative_pos[1]
        position[0], position[1] = board_pos[0] + (position[0] * tile_size), board_pos[1] + (position[1] * tile_size) 
        return position
    
    def get_possible_moves(self):
        moves = []
        local_board = board.return_board()
        y = int(self.relative_pos[1]) 
        x = int(self.relative_pos[0]) 

        if self.name == "w_rook" or self.name == "b_rook":
            up = True
            left = True
            right = True
            down = True
            for i in range(1, 8):
                if up:  
                    empty = True                  
                    target_field = [y - i, x]
                    existant = self.check_if_field_exists(target_field)
                    if not existant:
                        up = False
                    if existant:
                        empty = self.check_if_field_empty(target_field, local_board)
                    if empty and existant:
                        moves.append([y - i, x])
                    if not empty and existant:
                        colour = self.get_colour(target_field, local_board)
                        if colour == self.colour:
                            up = False
                        if colour != self.colour: 
                            up = False
                            moves.append([y - i, x])
                            print(moves, "up")

            for i in range(1, 8):
                if left:
                    empty = True
                    target_field = [y, x - i]
                    existant = self.check_if_field_exists(target_field)
                    if not existant:
                        left = False
                    if existant:    
                        empty = self.check_if_field_empty(target_field, local_board)
                    if empty and existant:
                        moves.append([y, x - i])
                    if not empty and existant:
                        colour = self.get_colour(target_field, local_board)
                        if colour == self.colour:
                            up = False
                        if colour != self.colour: 
                            up = False
                            moves.append([y, x - i])
                            print(moves, "left")

            for i in range(1, 8):
                if down: 
                    empty = True  
                    target_field = [y + i, x]
                    existant = self.check_if_field_exists(target_field)
                    if not existant:
                        down = False
                    if existant:
                        empty = self.check_if_field_empty(target_field, local_board)
                    if empty and existant:
                        moves.append([y + i, x])
                    if not empty and existant:
                        colour = self.get_colour(target_field, local_board)
                        if colour == self.colour:
                            down = False
                        if colour != self.colour: 
                            down = False
                            moves.append([y + i, x])
                            print(moves, "down")

            for i in range(1, 8):
                if right:
                    empty = True
                    target_field = [y, x + i]
                    existant = self.check_if_field_exists(target_field)
                    if not existant:
                        right = False
                    if existant:    
                        empty = self.check_if_field_empty(target_field, local_board)
                    if empty and existant:
                        moves.append([y, x + i])
                    if not empty and existant:
                        colour = self.get_colour(target_field, local_board)
                        if colour == self.colour:
                            up = False
                        if colour != self.colour: 
                            up = False
                            moves.append([y, x + i])
                            print(moves, "right")
            return(moves)
        

    def check_if_field_exists(self, field): 
        if field[0] <= 7 and field[0] >= 0:
            if field[1] <= 7 and field[1] >= 0:
                return True
        return False
        
    def check_if_field_empty(self, field, board):
        y = field[0]
        x = field[1]
        if board[y][x] == 0:
            return True
        else:
            return False

    def get_colour(self, field, local_board):
        y = field[0]
        x = field[1]
        local_board_copy = local_board
        name = local_board_copy[y][x].return_name()
        return str(name[0])

class Dekomanager:
    def __init__(self):
        self.active_objects = []

        self.possible_move_indicator = pygame.image.load("Move_arrow.png")
        self.possible_move_indicator = pygame.transform.scale(self.possible_move_indicator, (16 * scale_factor, 16 * scale_factor))       

    def return_possible_move_indicator(self):
        return self.possible_move_indicator

    def do_your_job(self, events, mouse_pos, starting_colour):
        self.check_if_new_decoobject(events, mouse_pos, starting_colour)
        self.show_deco_object()

    def check_if_new_decoobject(self, events, mouse_pos, starting_colour):
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
               self.active_objects.append(Deko_Object("rainbowcircle", mouse_pos, starting_colour))

    def show_deco_object(self):
        for Object in self.active_objects:
            Object.do_object()
            stage = Object.get_stage()
            if stage > 2000: 
                self.active_objects.remove(Object)


class Deko_Object:
    def __init__(self, name, coords, starting_colour):
        self.name = name
        self.stage = 0
        self.coords = coords
        self.colour = starting_colour
        self.rgb_speed = [15, 20, 12]
        self.animation_speed = 20

    def do_object(self):
        if self.name == "rainbowcircle":
            self.get_rainbow_color()
            pygame.draw.circle(screen, (self.colour[0], self.colour[1], self.colour[2]), self.coords, self.stage, 10)
            self.stage += self.animation_speed
            

    def get_rainbow_color(self):
        for i in range(3):
            self.colour[i] += self.rgb_speed[i]
            if self.colour[i] > 234:
                self.rgb_speed[i] *= - 1
            if self.colour[i] < 21: 
                self.rgb_speed[i] *= - 1
    
    def get_stage(self):
        return self.stage

#------------------------Hier sind globale Objekte-------------------------------------------------
board = Chess_Board()    
board.finish_setup()

dekomanager = Dekomanager()

#------------------------------Main Loop-----------------------------------------------------------

running = True
while running:   
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            running = False
         

    keys = pygame.key.get_pressed()
    mouse_pos = pygame.mouse.get_pos()
    
    screen.fill("black")

    dekomanager.do_your_job(events, mouse_pos, [230, 21, 127])

    board.blit_board()
    board.blit_pieces()
    board.get_and_show_moves(events, mouse_pos)


    pygame.display.flip()

    if keys[pygame.K_q]:
        running = False

pygame.quit()       
