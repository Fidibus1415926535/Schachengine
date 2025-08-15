#https://www.youtube.com/watch?v=dQw4w9WgXcQ&list=RDdQw4w9WgXcQ 

import pygame 
pygame.init()
screen_width = 1920
screen_lenght = 1080
board_size = 128
scale_factor = 8
zwei = 2

screen = pygame.display.set_mode((screen_width, screen_lenght))             
pygame.display.set_caption("Schach")                       
clock = pygame.time.Clock()
board_pos = [(screen_width - board_size * scale_factor) / zwei, (screen_lenght - board_size * scale_factor) / zwei] 


#Hier befinden sich alle meine Classes

class Chess_Board:

    def __init__(self):
        self.colour = self.get_opponent_colour()
        self.board = self.get_standartaufstellung(self.colour)
        self.board = self.create_piece_objects(self.board)
       
        self.board_img = pygame.image.load("Board.png")
        self.board_img = pygame.transform.scale(self.board_img, (128 * scale_factor, 128 * scale_factor))
        

    def blit_board(self):
        screen.blit(self.board_img, (board_pos[0], board_pos[1]))
        

#---------------------------Funktionen, die nur von anderen Funktionen der Klasse benutzt werden------------------
    def get_opponent_colour(self):
        colour = "black"
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
                ["w_pawn", "w_pawn", "w_pawn", "w_pawn", "w_pawn", "w_pawn", "w_pawn", "w_pawn"],
                ["w_rook", "w_knight", "w_bishop", "w_queen", "w_king", "w_bishop", "w_knight", "w_rook"],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                ["b_rook", "b_knight", "b_bishop", "b_queen", "b_king", "b_bishop", "b_knight", "b_rook"],
                ["b_pawn", "b_pawn", "b_pawn", "b_pawn", "b_pawn", "b_pawn", "b_pawn", "b_pawn"]
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
                    coords = [x, y]
                    type = str(square)
                    board[y][x] = Piece(type)
        return board

       
class Piece:
    
    def __init__(self, type):
        self.type = type
    
    def blit_piece(self):
        pass
        
    
Board = Chess_Board()


running = True
while running:   
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            running = False
         

    keys = pygame.key.get_pressed()
    if keys == pygame.K_q:
        running = False

    mouse_pos = pygame.mouse.get_pos()


    screen.fill("black")
    Board.blit_board()


    pygame.display.flip()


pygame.quit()       