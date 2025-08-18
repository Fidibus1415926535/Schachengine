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
        

    def finish_setup(self):
        self.board = self.create_piece_objects(self.board)

    def return_pos(self):
        return self.board_pos

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

class Piece:
    
    def __init__(self, name, relative_pos):
        
        self.piece_img = pygame.image.load(name + ".png")
        self.piece_img = pygame.transform.scale(self.piece_img, (piece_size * scale_factor, piece_size * scale_factor))
     
        self.pos = relative_pos
        self.pos = self.calculate_actual_pos()
    
    def blit_piece(self):
        screen.blit(self.piece_img, (self.pos[0], self.pos[1]))

        
    def get_board_coords(self):
        board_pos = board.return_pos() 
        return board_pos 

    def calculate_actual_pos(self):
        board_pos = self.get_board_coords()
        print(self.pos)
        print(board_pos)
        self.pos[0], self.pos[1] = board_pos[0] + (self.pos[0] * tile_size), board_pos[1] + (self.pos[1] * tile_size) 
 
        print(self.pos)
        return self.pos
    
class Dekomanager:
    def __init__(self):
        self.active_objects = []

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
            print(self.colour)
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


    pygame.display.flip()

    if keys[pygame.K_q]:
        running = False

pygame.quit()       
