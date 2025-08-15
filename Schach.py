#https://www.youtube.com/watch?v=dQw4w9WgXcQ&list=RDdQw4w9WgXcQ 

import pygame 
pygame.init()
screen_width = 1920
screen_lenght = 1080
board_size = 128
piece_size = 16
tile_size = 16
scale_factor = 8
zwei = 2

screen = pygame.display.set_mode((screen_width, screen_lenght))             
pygame.display.set_caption("Schach")                       
clock = pygame.time.Clock()



#Hier befinden sich alle meine Classes

class Chess_Board:

    def __init__(self):
        self.colour = self.get_opponent_colour()
        self.board = self.get_standartaufstellung(self.colour)
        self.board = self.create_piece_objects(self.board)
       
        self.board_img = pygame.image.load("Board.png")
        self.board_img = pygame.transform.scale(self.board_img, (128 * scale_factor, 128 * scale_factor))

        self.board_pos = [(screen_width - board_size * scale_factor) / zwei, (screen_lenght - board_size * scale_factor) / zwei] 
        

    def blit_board(self):
        screen.blit(self.board_img, (self.board_pos[0], self.board_pos[1]))

    def blit_pieces(self):
        for row in self.board:
            for piece in row:
                piece.blit_piece()

        

#---------------------------Funktionen, die nur von anderen Funktionen der Klasse "Chess_Board" benutzt werden---------------------------------
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
                    pos = [x, y]
                    name = str(square)
                    board[y][x] = Piece(name, pos)
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
        board_pos = board.board_pos #Ist es unnötig hierfür eine eigene Funktion zu machen? Oder ist das lesbarer?
        return board_pos 

    def calculate_actual_pos(self):
        board_pos = self.get_board_coords()
        self.pos[0] = board_pos[0] + self.pos[1] * tile_size  # X Coordinate der Figur relativ zum Brett
        self.pos[1] = board_pos[1] + self.pos[0] * tile_size  # Das gleiche für Y


#------------------------Hier sind globale Objekte-------------------------------------------------
board = Chess_Board()    


running = True
while running:   
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            running = False
         

    keys = pygame.key.get_pressed()
    if keys[pygame.K_q]:
        running = False
    mouse_pos = pygame.mouse.get_pos()


    screen.fill("black")
    board.blit_board()


    pygame.display.flip()


pygame.quit()       