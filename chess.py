import pygame
 
pygame.init()
WIDTH = 640
HEIGHT = 640
SQUARESIZE  = 80
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("CHESS")
running = True
sqaures_list = []
def chess_board():
   for row in range(8):
        for col in range(8):
          if (col + row) % 2 == 0:
               pygame.draw.rect(screen, (155, 155, 155), (col*80, row*80, 80, 80))
          else:
               pygame.draw.rect(screen, (116, 116, 98), (col*80, row*80, 80, 80))
class Bishop:
    def __init__(self, colour, row, col):
        self.friendlies = []
        self.row = row
        self.col = col
        self.colour = colour
        self.legal_moves = []
        self.movement = [(1, 1), (1, -1), (-1, 1), (-1, -1)]
        self.in_control = False
        self.attacked_list = []
    def draw(self):
        if flipped:
      
            draw_x = (7 - self.col)*SQUARESIZE + SQUARESIZE//2
            draw_y = (7 - self.row)*SQUARESIZE + SQUARESIZE//2
        else:
            draw_x = self.col*SQUARESIZE + SQUARESIZE//2
            draw_y = self.row*SQUARESIZE + SQUARESIZE//2
        if self.colour == 0:
            screen.blit(piece_images["white_bishop"], (draw_x - 40, draw_y - 40))
        else:
            screen.blit(piece_images["black_bishop"], (draw_x - 40, draw_y - 40))
    def check_legal_moves(self):
        self.friendlies = []
        self.legal_moves = []
        for offset_x, offset_y in self.movement:
            legal_x = self.col
            legal_y = self.row
            
            stop = True
            while stop:
              
                legal_x += offset_x
                legal_y += offset_y
                if 0 <= legal_x <= 7 and 0 <= legal_y <= 7:
                    target = get_target(legal_x, legal_y, pieces_list, self)
                    if target == None:
                       self.legal_moves.append((legal_x, legal_y))
                    elif target.colour != self.colour:
                      
                        self.legal_moves.append((legal_x, legal_y)) 
                        break
                    elif target.colour == self.colour:
                        self.friendlies.append((legal_x, legal_y))
                        break
                else:
                    stop = False
    def get_attacked_squares_local(self):
        self.attacked_list = get_attacked_sqaures(self.movement, self.col, self.row, self)
    def movements(self, pos, turn):
        
        if self.in_control and pos:
            x, y = pos
            if self.colour == turn and (x,y) in self.legal_moves:
             
                if (x, y) in self.legal_moves:
                    self.col = x
                    self.row = y
                    self.in_control = False
                 
                    return 1 if turn == 0 else 0, True
            elif (x, y) not in self.legal_moves:
               if x != self.col or y != self.row:
                 self.in_control = False
        return None, False            
           
class Rook:
    def __init__(self, row, col, colour):
        self.row = row
        self.col = col
        self.colour = colour
        self.legal_moves = []
        self.movement = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        self.in_control = False   
        self.moves = 0 
        self.friendlies = []
        self.attacked_list = []
    def check_legal_moves(self):
        self.friendlies = []
        self.legal_moves = []
        for offset_x, offset_y in self.movement:
            legal_x = self.col
            legal_y = self.row
            
            stop = True
            while stop:
              
                legal_x += offset_x
                legal_y += offset_y
                if 0 <= legal_x <= 7 and 0 <= legal_y <= 7:
                    target = get_target(legal_x, legal_y, pieces_list, self)
                    if target == None:
                       self.legal_moves.append((legal_x, legal_y))
                    elif target.colour != self.colour:
                        self.legal_moves.append((legal_x, legal_y)) 
                        break
                    elif target.colour == self.colour:
                        self.friendlies.append((legal_x, legal_y))
                        break
                else:
                    stop = False
    def get_attacked_squares_local(self):
        self.attacked_list = get_attacked_sqaures(self.movement, self.col, self.row,self )

     
    def draw(self):
      
        if flipped:
      
            draw_x = (7 - self.col)*SQUARESIZE + SQUARESIZE//2
            draw_y = (7 - self.row)*SQUARESIZE + SQUARESIZE//2
        else:
            draw_x = self.col*SQUARESIZE + SQUARESIZE//2
            draw_y = self.row*SQUARESIZE + SQUARESIZE//2
        if self.colour == 0:
            screen.blit(piece_images["white_rook"], (draw_x - 40, draw_y - 40))
        else:
            screen.blit(piece_images["black_rook"], (draw_x - 40, draw_y - 40))
    def movements(self, pos, turn):
        if self.in_control and pos:
            x, y = pos
            if self.colour == turn and (x,y) in self.legal_moves:
              
                if (x, y) in self.legal_moves:
                    self.col = x
                    self.row = y
                    self.in_control = False
                    self.moves += 1
           
                
                    return 1 if turn == 0 else 0, True
            elif (x, y) not in self.legal_moves:
              if x != self.col or y != self.row:
                self.in_control = False
        return None, False
class Queen:
    def __init__(self, colour, col, row):
        self.row = row
        self.col = col
        self.colour = colour
        self.legal_moves = []
        self.movement = [(1, 0), (-1, 0), (0, 1), (0, -1),(1, 1), (1, -1), (-1, 1), (-1, -1) ]
        self.in_control = False
        self.friendlies = []
        self.attacked_list = []
    def check_legal_moves(self):
        self.friendlies = []
        self.legal_moves = []
        for offset_x, offset_y in self.movement:
            legal_x = self.col
            legal_y = self.row
            
            stop = True
            while stop:
              
                legal_x += offset_x
                legal_y += offset_y
                if 0 <= legal_x <= 7 and 0 <= legal_y <= 7:
                    target = get_target(legal_x, legal_y, pieces_list, self)
                    if target == None:
                       self.legal_moves.append((legal_x, legal_y))
                    elif target.colour != self.colour:
                        self.legal_moves.append((legal_x, legal_y)) 
                        break
                    elif target.colour == self.colour:
                        self.friendlies.append((legal_x, legal_y))
                        break
                else:
                    stop = False
    def get_attacked_squares_local(self):
        self.attacked_list = get_attacked_sqaures(self.movement, self.col, self.row,self )


    def movements(self, pos, turn):     
        if self.in_control and pos:
            x, y = pos
            if self.colour == turn and (x,y) in self.legal_moves:
              
                if (x, y) in self.legal_moves:
                    self.col = x
                    self.row = y
                    self.in_control = False
               
                  
                    return 1 if turn == 0 else 0, True
            elif (x, y) not in self.legal_moves:
               if x != self.col or y != self.row:
                 self.in_control = False
        return None, False
    def draw(self):
      
        if flipped:
      
            draw_x = (7 - self.col)*SQUARESIZE + SQUARESIZE//2
            draw_y = (7 - self.row)*SQUARESIZE + SQUARESIZE//2
        else:
            draw_x = self.col*SQUARESIZE + SQUARESIZE//2
            draw_y = self.row*SQUARESIZE + SQUARESIZE//2
        if self.colour == 0:
            screen.blit(piece_images["white_queen"], (draw_x - 40, draw_y - 40))
        else:
            screen.blit(piece_images["black_queen"], (draw_x - 40, draw_y - 40))
class Knight:
    def __init__(self, colour, col, row):
        self.col = col
        self.row = row
        self.colour = colour
        self.legal_moves = []
        self.movement = [(2, 1), (1, 2), (-2, 1), (-1, 2), (1, -2), (-1, -2), (2, -1), (-2, -1)]
        self.in_control = False
        self.friendlies = []
        self.attacked_list = []
    def check_legal_moves(self):
        self.friendlies = []
        self.legal_moves = []
        for offset_x, offset_y in self.movement:
            legal_x = self.col
            legal_y =self.row
            legal_x += offset_x
            legal_y += offset_y
            if 0 <= legal_x <= 7 and 0 <= legal_y <= 7:
                target = get_target(legal_x, legal_y, pieces_list, self)
                if target == None:
                   self.legal_moves.append((legal_x, legal_y))
                elif target.colour != self.colour:
                    self.legal_moves.append((legal_x, legal_y))
                    continue
                else:
                    self.friendlies.append((legal_x, legal_y))
                    continue
    def get_attacked_squares_local(self):
          self.attacked_list = []
          for offset_x, offset_y in self.movement:
            legal_x = self.col
            legal_y =self.row
            legal_x += offset_x
            legal_y += offset_y
            if 0 <= legal_x <= 7 and 0 <= legal_y <= 7:
                target = get_target(legal_x, legal_y, pieces_list, self)
                if target == None:
                   self.attacked_list.append((legal_x, legal_y))
                elif target.colour != self.colour:
                    self.attacked_list.append((legal_x, legal_y))
                    continue
                else:
                   
                    continue
    def movements(self, pos, turn):     
        if self.in_control and pos:
            x, y = pos
            if self.colour == turn and (x,y) in self.legal_moves:
            
              
                if (x, y) in self.legal_moves:
                
                    self.col = x
                    self.row = y
                    self.in_control = False
               
                    if turn == 0:
                        turn = 1
                       
                        return turn, True
                    else:
                        turn = 0
                     
                        return turn, True
            elif (x, y) not in self.legal_moves:
              if x != self.col or y != self.row:
                self.in_control = False
      
        return None, False

    def draw(self):
      
        if flipped:
      
            draw_x = (7 - self.col)*SQUARESIZE + SQUARESIZE//2
            draw_y = (7 - self.row)*SQUARESIZE + SQUARESIZE//2
        else:
            draw_x = self.col*SQUARESIZE + SQUARESIZE//2
            draw_y = self.row*SQUARESIZE + SQUARESIZE//2
        if self.colour == 0:
            screen.blit(piece_images["white_knight"], (draw_x - 40, draw_y - 40))
        else:
            screen.blit(piece_images["black_knight"], (draw_x - 40, draw_y - 40))

class Pawn:
    def __init__(self, colour, col, row):
        self.col = col
        self.row = row
        self.colour = colour
        self.in_control = False
        self.legal_moves = []
        self.movement_white = (0, -1)
        self.movement_black = (0, 1)
        self.capture_white = [(1, -1), (-1, -1)]
        self.capture_black = [(1, 1), (-1, 1)]
        self.black_two = (0, 2)
        self.white_two = (0, -2)
        self.move = 0
        self.friendlies = []
        self.attacked_list = []
        self.can_be_ep = False
        self.en_passent_enemies = []
        self.ep_number = 0
    def check_legal_moves(self):
        self.en_passent_enemies = []
        self.friendlies = []
        self.legal_moves = []
        if self.colour == 0:
            offset_x, offset_y = self.movement_white
            legal_x = self.col
            legal_y =self.row
            legal_x += offset_x
            legal_y += offset_y
            if 0 <= legal_x <= 7 and 0 <= legal_y <= 7:
                target = get_target(legal_x, legal_y, pieces_list, self)
                if target == None:
                    self.legal_moves.append((legal_x, legal_y))
            
            if self.move == 0:
                march_x, march_y = self.white_two
                legal_x_march = self.col
                legal_y_march = self.row
                legal_x_march += march_x
                legal_y_march += march_y
                if 0 <= legal_x_march <= 7 and 0 <= legal_y_march <= 7:
                    target_march = get_target(legal_x_march, legal_y_march, pieces_list, self)
                    if target_march == None:
                        self.legal_moves.append((legal_x_march, legal_y_march)) 
            for (offset_x, offset_y) in self.capture_white:  
                capture_x = self.col
                capture_y =self.row
                capture_x += offset_x
                capture_y += offset_y   
            
                target_capture = get_target(capture_x, capture_y, pieces_list, self)
                if target_capture:
                  if target_capture.colour != self.colour:
                    self.legal_moves.append((capture_x, capture_y))
                    continue
                else:
                    self.friendlies.append((capture_x, capture_y))
                    continue
            
        else:
           
            offset_x, offset_y = self.movement_black
            legal_x = self.col
            legal_y =self.row
            legal_x += offset_x
            legal_y += offset_y
            if 0 <= legal_x <= 7 and 0 <= legal_y <= 7:
                target = get_target(legal_x, legal_y, pieces_list, self)
                if target == None:
                    self.legal_moves.append((legal_x, legal_y))
            if self.move == 0:
                march_x, march_y = self.black_two
                legal_x_march = self.col
                legal_y_march = self.row
                legal_x_march += march_x
                legal_y_march += march_y
                if 0 <= legal_x_march <= 7 and 0 <= legal_y_march <= 7:
                    target_march = get_target(legal_x_march, legal_y_march, pieces_list, self)
                    if target_march == None:
                        self.legal_moves.append((legal_x_march, legal_y_march)) 
            for (offset_x, offset_y) in self.capture_black:  
                capture_x = self.col
                capture_y =self.row
                capture_x += offset_x
                capture_y += offset_y   
            
                target_capture = get_target(capture_x, capture_y, pieces_list, self)
                if target_capture:
                 if target_capture.colour != self.colour:
                    self.legal_moves.append((capture_x, capture_y))
                     
                    continue
                else:
                    self.friendlies.append((capture_x, capture_y))
                    continue
     
       
        self.en_passent_enemies = check_en_passent(self.col, self.row, self.colour, self)
        for piece in self.en_passent_enemies:
            print(piece.col, piece.row)
        self.legal_moves = add_en_passent(self.col, self.row, self.legal_moves, self.en_passent_enemies, self.colour)   
       
    def get_attacked_squares_local(self):
        self.attacked_list = []
        if self.colour == 0:
            for offset_x, offset_y in self.capture_white:
                capture_x = self.col
                capture_y =self.row
                capture_x += offset_x
                capture_y += offset_y   
                self.attacked_list.append((capture_x, capture_y))
        else:
            for offset_x, offset_y in self.capture_black:
                capture_x = self.col
                capture_y =self.row
                capture_x += offset_x
                capture_y += offset_y   
                self.attacked_list.append((capture_x, capture_y))
    def movements(self,pos,  turn):
       
        if self.in_control and pos:
            x, y = pos
            if self.colour == turn and (x,y) in self.legal_moves:
              
                if (x, y) in self.legal_moves:
                    self.move += 1
                    if is_marched(self.row, self.colour, y) and self.move == 1:
                        print("CAN BE EN PASSENT")
                        
                        self.ep_number = number_terms
                    else:
                        self.can_be_ep = False
                        print("NO EN PASSENT")
                    
                    if is_en_passent(self.col, self.row, self.colour, x, y):
                        en_passent(x, y, self.colour, self)

                    self.col = x
                    self.row = y
                    self.in_control = False
             
                 
                    
                    return 1 if turn == 0 else 0, True
            elif (x, y) not in self.legal_moves:
               if x != self.col or y != self.row:
                 self.in_control = False
        return None, False
    def draw(self):
     
        if flipped:
      
            draw_x = (7 - self.col)*SQUARESIZE + SQUARESIZE//2
            draw_y = (7 - self.row)*SQUARESIZE + SQUARESIZE//2
        else:
            draw_x = self.col*SQUARESIZE + SQUARESIZE//2
            draw_y = self.row*SQUARESIZE + SQUARESIZE//2
        if self.colour == 0:
            screen.blit(piece_images["white_pawn"], (draw_x - 40, draw_y - 40))
        else:
            screen.blit(piece_images["black_pawn"], (draw_x - 40, draw_y - 40))
class King:
    def __init__(self, colour, col, row):
        self.col = col
        self.row = row
        self.colour = colour
        self.legal_moves = []
        self.movement = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]
        self.castle = [(2, 0), (-2, 0)]
        self.in_control = False
        self.move = 0
        self.friendlies = []
        self.attacked_list = []
       
    def check_legal_moves(self):
        self.friendlies = []
        self.legal_moves = []
        check_legal_moves_list = []
        for offset_x, offset_y in self.movement:
            legal_x = self.col
            legal_y= self.row
            legal_x += offset_x
            legal_y += offset_y
          
            if 0 <= legal_x <= 7 and 0 <= legal_y <= 7:
                
                target = get_target(legal_x, legal_y, pieces_list, self)
                if target:
                 if target.colour == self.colour:
                     self.friendlies.append((legal_x, legal_y))
                     continue 
             
                for piece in pieces_list:
                     if piece.colour != turn:
                        for cords_friends in piece.friendlies:
                           check_legal_moves_list.append(cords_friends)
                        for cords in piece.attacked_list:
                            check_legal_moves_list.append(cords)
            if (legal_x, legal_y) not in check_legal_moves_list:
                self.legal_moves.append((legal_x, legal_y))
      
        
      
        if can_castle(self.move, pieces_list, self.col, self.row):
           
        
       
            for (castle_x, castle_y) in self.castle:
             
                if rook_can_castle((castle_x, castle_y),pieces_list, self.col, self.row, self ) :
                
                  if no_pieces((castle_x, castle_y), pieces_list, self.col, self.row, self):
                    org_col = self.col
                    org_row = self.row
                    org_col += castle_x
                    org_row += castle_y
                    piece_check = get_target(org_col, org_row, pieces_list, self)
                    if piece_check:
                     continue
                    else:
                      self.legal_moves.append((org_col, org_row))
                  else:
                      continue
                else:
                    continue
    def get_attacked_squares_local(self):
        self.attacked_list = []
        for offset_x, offset_y in self.movement:
            legal_x = self.col
            legal_y= self.row
            legal_x += offset_x
            legal_y += offset_y
          
            if 0 <= legal_x <= 7 and 0 <= legal_y <= 7:
                self.attacked_list.append((legal_x, legal_y))
    def movements(self, pos, turn):
        if self.in_control and pos:
            x, y = pos
            if self.colour == turn and (x,y) in self.legal_moves:
              
                if (x, y) in self.legal_moves:
                    past_x = self.col
                    past_y =self.row
                    if past_x == 4 and x == past_x + 2:
                        castle(pieces_list, (2, 0), past_x, past_y, self) 
                    elif past_x == 4 and x == past_x - 2:
                        castle(pieces_list, (-2, 0), past_x, past_y, self) 
                    self.col = x
                    self.row = y
                   
                    self.in_control = False
                   
               
                    self.move += 1
                    return 1 if turn == 0 else 0, True
            elif (x, y) not in self.legal_moves:
               if x != self.col or y != self.row:
                 self.in_control = False
        return None, False
    def draw(self):
     
        
        if flipped:
      
            draw_x = (7 - self.col)*SQUARESIZE + SQUARESIZE//2
            draw_y = (7 - self.row)*SQUARESIZE + SQUARESIZE//2
        else:
            draw_x = self.col*SQUARESIZE + SQUARESIZE//2
            draw_y = self.row*SQUARESIZE + SQUARESIZE//2
        if self.colour == 0:
            screen.blit(piece_images["white_king"], (draw_x - 40, draw_y - 40))
        else:
            screen.blit(piece_images["black_king"], (draw_x - 40, draw_y - 40))
def get_attacked_sqaures(movement, org_col, org_row, current_piece):
    attacked_sqaures = []
    for offset_x, offset_y in movement:
        orginal_x = org_col
        original_y = org_row
        while True:
           
            orginal_x += offset_x
            original_y += offset_y
            if 0 <= orginal_x <= 7 and 0 <= original_y <= 7:
                target = get_target(orginal_x, original_y, pieces_list, current_piece)
                if target == None:
                    attacked_sqaures.append((orginal_x, original_y))
                elif target.colour != current_piece.colour:
                    attacked_sqaures.append((orginal_x, original_y))
                    break
                else:
                    break
            else:
                break
    return attacked_sqaures

def en_passent(col, row, colour, current_piece):
    if colour == 0:
        y  = row + 1
        target = get_target(col, y, pieces_list, current_piece)
        if isinstance(target, Pawn) and target.colour != turn and target.can_be_ep == True:
           pieces_list.remove(target)
    else:
        y  = row - 1
        target = get_target(col, y, pieces_list, current_piece)
        if isinstance(target, Pawn) and target.colour != turn and target.can_be_ep == True:
           pieces_list.remove(target)
def add_en_passent(col, row, legal_list, en_passent_list, colour):
    legal_moves = legal_list
    for targets in en_passent_list:
        if targets.col == col - 1:
            print("in left")
            if colour == 0:
               en_passent_x = col - 1
               en_passent_y = row - 1
               legal_moves.append((en_passent_x, en_passent_y))
            else:
               en_passent_x = col - 1
               en_passent_y = row + 1
               legal_moves.append((en_passent_x, en_passent_y))
        elif targets.col == col + 1:
            print("IN RIGHT")
            if colour == 0:
               en_passent_x = col + 1
               en_passent_y = row - 1
               legal_moves.append((en_passent_x, en_passent_y))
            else:
                en_passent_x = col + 1
                en_passent_y = row + 1
                legal_moves.append((en_passent_x, en_passent_y))
    legal_list = legal_moves
    return legal_list
def check_en_passent(col, row, colour, current_piece) :
    en_passent_list = []
    offsets = [1, -1]
    for o in offsets:
        check_x = col + o
        target = get_target(check_x, row, pieces_list, current_piece)
        if isinstance(target, Pawn):
            print(target.can_be_ep, target.colour)
            if target.can_be_ep and target.colour != colour:
              
                en_passent_list.append(target)
    return en_passent_list
def is_marched(row, colour, choosed_row):
    if colour == 0:
        offset = -2
    else:
        offset = 2
    if choosed_row == row + offset:
      
        return True
    else:
        return False
def rook_can_castle(side, pieces_list, col, row, cuurent):
    if side == (-2, 0):
       
        col = col
        row = row
        col -= 4
        row -= 0
       
        rook = get_target(col, row, pieces_list, cuurent)
     
        if isinstance(rook, Rook) and rook.colour == turn:
            
            if rook.moves == 0:
                
                return True
            else:
                return False
        else:
            return False
    elif side == (2, 0):
        
        col = col
        row = row
        col += 3
        row += 0
        rook = get_target(col, row, pieces_list, cuurent)
        if isinstance(rook, Rook) and rook.colour == turn:
            if rook.moves == 0:
                return True
            else:
                return False
        else:
            return False

        
           
               
def is_en_passent(col, row, colour,x, y):
    if x == col- 1 or x == col + 1:
        if colour == 0:
            if y == row - 1:
                return True
        else:
            if y == row +1:
                return True

def castle(pieces_list, side, col, row, current):
    if side == (-2, 0):
        rook = get_target(col - 4, row, pieces_list,current)
        rook.col = 3
    elif side == (2, 0):
         rook = get_target(col + 3, row, pieces_list,current)
         rook.col = 5
def no_pieces(side, pieces_list, col, row, cuurrent):
    if side == (-2, 0):
       
        check_list = [(-1,0), (-2, 0), (-3, 0)]
        for offset_x, offset_y in check_list:
            check_col = col
            check_row = row
            check_col += offset_x
            check_row += offset_y
            piece_on_block = get_target(check_col, check_row, pieces_list,cuurrent)
            
            if piece_on_block:
                return False
        return True
    elif side == (2, 0):
      
        check_list = [(1,0), (2, 0)]
        for offset_x, offset_y in check_list:
            check_col = col
            check_row = row
            check_col += offset_x
            check_row += offset_y
            piece_on_block = get_target(check_col, check_row, pieces_list,cuurrent)
         
            if piece_on_block:
                return False
        return True

def can_castle(moves, pieces_list, col, row):
 
    
     
    for piece in pieces_list:
        if piece.colour != turn:
          
            if (col, row) in piece.attacked_list or moves > 0:
            
                
               
                return False
    return True



def capture_piece(pos, pieces_list):
 
    x, y = pos
    for pieces in pieces_list[:]:
        if pieces.colour != turn:
         if pieces.col == x and pieces.row == y:
              pieces_list.remove(pieces)
    return pieces_list
def get_target(x, y, pieces_list, current_piece):
   
    for p in pieces_list:
        
        if p is current_piece:
         continue
        if p.col == x and p.row == y:
            return p
    return None

def sqaures(sqaures_list):
    for row in range(8):
       for col in range(8):   
            
            sqares_info = {
               "HITBOX": pygame.Rect(col*SQUARESIZE, row*SQUARESIZE, SQUARESIZE, SQUARESIZE),
               "CENTRE": (col, row)
            }
            sqaures_list.append(sqares_info)
    return sqaures_list


def on_mouse(sqaures_list, event, slected_piece):
    in_control = False
    mx, my = pygame.mouse.get_pos()
    mouse_rect = pygame.Rect(mx, my, 5, 5)
 
    if event.type == pygame.MOUSEBUTTONDOWN:
        
        for sqaures in sqaures_list:
            if sqaures["HITBOX"].colliderect(mouse_rect):
                choosed_col, choosed_row = sqaures["CENTRE"]
                if flipped:
                    choosed_col = 7 - choosed_col
                    choosed_row = 7 - choosed_row
               
                for p in pieces_list:
                 
                    if p.col == choosed_col and p.row == choosed_row:
                        for piece in pieces_list:
                            piece.check_legal_moves()
                        simulate_to_checK(pieces_list)
                       
                           
 
                      
                        for checks in pieces_list:
                            if checks.colour == turn:
                              if checks.in_control == True:
                                in_control = True
                                break
                            else:
                                in_control = False
                        if not in_control:
                            
                            p.in_control = True
                     
        if event.type == pygame.MOUSEBUTTONDOWN:
         
          
          for sqaures in sqaures_list:
            if sqaures["HITBOX"].colliderect(mouse_rect):
                if flipped:
                    col, row = sqaures["CENTRE"]
                    flipped_col = 7 - col
                    flipped_row = 7- row
                    return (flipped_col, flipped_row)
              
               
                return sqaures["CENTRE"]
def simulate_to_checK(pieces_list):
    for piece in pieces_list[:]:
        if piece.colour != turn:
            continue 
        org_x = piece.col
        org_y =piece.row
        filtered_move = []
        for cords in piece.legal_moves:
            
            captured_piece = None
            move_x, move_y =cords
            target = get_target(move_x, move_y, pieces_list, piece)
            piece.col = move_x
            piece.row = move_y
           
            if target:
                captured_piece = target
                pieces_list.remove(target)
            for i in pieces_list:
                i.get_attacked_squares_local()
            enemy_colour = 1 -turn
            enemy_attacked = compute_attacked_list(pieces_list, enemy_colour)
          
            king_pos = None
            for p in pieces_list:
                if isinstance(p, King) and p.colour == turn:
                  
                    king_pos = (p.col, p.row)
                   
                  
                    if king_pos and king_pos not in enemy_attacked:
                  
                      filtered_move.append((move_x, move_y))
        
            if captured_piece:
               pieces_list.append(captured_piece)
        piece.col = org_x
        piece.row = org_y
       
        piece.legal_moves = filtered_move        
def load_images():
    white_pawn = pygame.image.load("white_pawn.png")
    black_pawn = pygame.image.load("black_pawn.png")
    white_rook = pygame.image.load("white_rook.png")
    black_rook = pygame.image.load("black_rook.png")
    white_knight = pygame.image.load("white_knight.png")
    black_knight = pygame.image.load("black_knight.png")
    white_bishop = pygame.image.load("white_bishops.png")
    black_bishop = pygame.image.load("black_bishops.png")
    white_queen = pygame.image.load("white_queen.png")
    black_queen = pygame.image.load("black_queen.png")
    white_king = pygame.image.load("white_king.png")
    black_king = pygame.image.load("black_king.png")


    white_pawn = pygame.transform.scale(white_pawn, (80, 80))
    black_pawn = pygame.transform.scale(black_pawn, (80, 80))
    white_rook = pygame.transform.scale(white_rook, (80, 80))
    black_rook = pygame.transform.scale(black_rook, (80, 80))
    white_knight = pygame.transform.scale(white_knight, (80, 80))
    black_knight = pygame.transform.scale(black_knight, (80, 80))
    white_bishop = pygame.transform.scale(white_bishop, (80, 80))
    black_bishop = pygame.transform.scale(black_bishop, (80, 80))
    white_queen = pygame.transform.scale(white_queen, (80, 80))
    black_queen = pygame.transform.scale(black_queen, (80, 80))
    white_king = pygame.transform.scale(white_king, (80, 80))
    black_king = pygame.transform.scale(black_king, (80, 80))
    return {
        "white_pawn": white_pawn,
        "black_pawn": black_pawn,
        "white_rook": white_rook,
        "black_rook": black_rook,
        "white_knight": white_knight,
        "black_knight": black_knight,
        "white_bishop": white_bishop,
        "black_bishop": black_bishop,
        "white_queen": white_queen,
        "black_queen": black_queen,
        "white_king": white_king,
        "black_king": black_king
    }
flipped = False
piece_images = load_images()
def check_promotion(pieces_list):
    for piece in pieces_list[:]:
        if isinstance(piece, Pawn):
            if (piece.colour == 0 and piece.row == 0) or (piece.colour == 1 and piece.row == 7):
                pieces_list.remove(piece)
                new_queen = Queen(piece.colour, piece.col, piece.row)
                pieces_list.append(new_queen)
              

def compute_attacked_list(pices_list, enemey_colour):
    global_attacked_list = []
    for piece in pices_list:
        if piece.colour == enemey_colour:
            for squares in piece.attacked_list:
                global_attacked_list.append(squares)
    return global_attacked_list

sqaures_list = sqaures(sqaures_list)
turn = 0
pieces_list = [King(1, 4, 0),
               King(0, 4, 7), 
               Rook(0 ,0, 1),
                Rook(0, 7, 1),
                Rook(7, 0, 0), 
                Rook(7, 7, 0), 
                Queen(1, 3, 0), 
                Queen(0, 3, 7), 
                Bishop(1, 0, 2),
                Bishop(1, 0, 5),
                Bishop(0, 7, 2),
                Bishop(0, 7, 5),
                Knight(1, 1, 0),
                Knight(1, 6, 0),
                Knight(0, 1, 7),
                Knight(0, 6, 7),
                Pawn(1, 0, 1),
                Pawn(1, 1, 1),
                Pawn(1, 2, 1),
                Pawn(1, 3, 1),
                Pawn(1, 4, 1),
                Pawn(1, 5, 1),
                Pawn(1, 6, 1),
                Pawn(1, 7, 1),
             



                Pawn(0, 0, 6),
                Pawn(0, 1, 6),
                Pawn(0, 2, 6),
                Pawn(0, 3, 6),
                Pawn(0, 4, 6),
                Pawn(0, 5, 6),
                Pawn(0, 6, 6),
                Pawn(0, 7, 6),
                ] 
clock = pygame.time.Clock()
selected_piece = None
number_terms = 0 
while running:
   
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        pos = on_mouse(sqaures_list, event, selected_piece)

    screen.fill((0, 0, 0))
    chess_board()
   
    for piece in pieces_list:
       
        piece.get_attacked_squares_local() 
        turn_tem, is_move = piece.movements(pos, turn)
        
        if is_move:
            pieces_list = capture_piece(pos, pieces_list)
            check_promotion(pieces_list)
            if flipped:
                flipped = False
            else:
                flipped = True
         
           
        if turn_tem != None:
            turn = turn_tem
            number_terms += 1
        if isinstance(piece, Pawn):
            if number_terms == piece.ep_number + 1:
                piece.can_be_ep = True
            else:
                piece.can_be_ep = False
        
        piece.draw()
       
    
    pygame.display.update() 