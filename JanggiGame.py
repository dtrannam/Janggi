# Name: David Trannam
# Description: Janggi Game - Portfolio project.

class JanggiGame:
    """
    This is the class set up for my Janggi Board. It does not take in any argument to create the board
    To see the board, print the instance of the Janggi Board
    The functions include creating a board, moving a piece, checking the game state, and to see if an item is in check
    More detailed description is attached to each function
    """

    def __init__(self):
        """
        The Janggi Board takes in no argument to create an instance of the board. It does have some attributes
        game_board is created from the create_board function within this class
        self._game_board creates the board instance of the game with all the pieces set up
        self._current_turn is used to track turn where B is starting
        self._red_g/self._blue_g is used to reference the blue/red general. This is needed out of scope for access
        self._red_check/self._blue_check is set to False to start - it's used to check if general is in check
        self._red_checkmate/self._blue_checkmate is set to False to start - it's used to check if general is in checkmate
        self._blue_piece/self._red_piece is set to an empty list. This stores pieces that has put the general in check
        """
        self._game_board = self.create_board()
        self._current_turn = 'B'  # B for Blue and R for Red
        self._red_g = self._game_board[1][4]
        self._blue_g = self._game_board[8][4]
        self._red_check = False
        self._blue_check = False
        self._red_checkmate = False
        self._blue_checkmate = False
        self._blue_piece = []
        self._red_piece = []

    def __str__(self):
        """
        __str__ returns the local variable string which is the board game created from self._game_board
        This includes formatting the X and Y axis to alphabet and numbers
        """
        string = '     A   B   C   D   E   F   G   H   I\n'
        for i in range(10):
            if i < 9:
                string += str(i + 1) + '  ' + str(self._game_board[i]) + '\n'
            else:
                string += str(i + 1) + ' ' + str(self._game_board[i]) + '\n'
        return string

    def general_check_move(self, capture):
        """
        This function checks to see if the current move general is in check and then return true/false
        If current in check general escapes, return True
        Else return False
        it takes in one possible value which is the "next" move which handles capturing piece that places general in check
        """
        if self._red_check is True and self._current_turn == 'R':
            if capture in self._blue_piece:
                self._blue_piece.remove(capture)
            for blue in self._blue_piece:
                if isinstance(self._game_board[blue[0]][blue[1]], Piece) and self._game_board[blue[0]][blue[1]].validate_move(blue[0], blue[1], self._red_g.get_x(), self._red_g.get_y(), self._game_board):
                    return False
            else:
                self._red_check = False
                return True
        elif self._blue_check is True and self._current_turn == 'B':
            if capture in self._red_piece:
                self._red_piece.remove(capture)
            for red in self._red_piece:
                if isinstance(self._game_board[red[0]][red[1]], Piece) and self._game_board[red[0]][red[1]].validate_move(red[0], red[1], self._blue_g.get_x(), self._blue_g.get_y(), self._game_board):
                    return False
            else:
                self._blue_check = False
                return True
        else:
            return True

    def update_check(self, next_x, next_y):
        """
        This function takes in a next_x, next_y which is used to take in the next move. This then checks to see if
        the next move can reach the general. If so, it would update the check function Example: Move A1 to A2 -> Our
        A2 is the next_x, next_y
        """
        if self._current_turn == 'B':  # handles blue's current turn and see if it can reach the red general
            if self._game_board[next_x][next_y] == self._game_board[self._blue_g.get_x()][self._blue_g.get_y()]:
                self._blue_check = False
            elif self._game_board[next_x][next_y].validate_move(next_x, next_y, self._red_g.get_x(),
                                                                self._red_g.get_y(),
                                                                self._game_board):
                self._red_check = True
                self._blue_piece.append([next_x, next_y])
        else:  # handles red's current turn and see if it can reach the blue general
            if self._game_board[next_x][next_y] == self._game_board[self._red_g.get_x()][self._red_g.get_y()]:
                self._red_check = False
            elif self._game_board[next_x][next_y].validate_move(next_x, next_y, self._blue_g.get_x(),
                                                                self._blue_g.get_y(),
                                                                self._game_board):
                self._blue_check = True
                self._red_piece.append([next_x, next_y])

    def create_board(self):
        """
        The create board is how we initialize the board. The row is represented by each list where as the columns are
        each nth position of the list. There is a total of 10. Each index position represent one space within the
        board. If the position is empty, it will be an empty string (''). Each piece will be represented by an instance
        of the class that will be further detailed within the file. The general format is 'XY' where x represents the
        color of the y represents the type of piece (General, Guard, Soldier.. etc)
        """
        x_board = []
        for x_axis in range(10):
            y_board = []
            for y_axis in range(9):
                y_board.append('')
            x_board.append(y_board)
        RedChariotL = Chariot(0, 0, 'R')
        RedChariotR = Chariot(0, 8, 'R')
        x_board[RedChariotL.get_x()][RedChariotL.get_y()] = RedChariotL
        x_board[RedChariotR.get_x()][RedChariotR.get_y()] = RedChariotR
        BlueChariotL = Chariot(9, 0, 'B')
        BlueChariotR = Chariot(9, 8, 'B')
        x_board[BlueChariotL.get_x()][BlueChariotL.get_y()] = BlueChariotL
        x_board[BlueChariotR.get_x()][BlueChariotR.get_y()] = BlueChariotR
        RedElephantL = Elephant(0, 1, 'R')
        RedElephantR = Elephant(0, 6, 'R')
        x_board[RedElephantL.get_x()][RedElephantL.get_y()] = RedElephantL
        x_board[RedElephantR.get_x()][RedElephantR.get_y()] = RedElephantR
        BlueElephantL = Elephant(9, 1, 'B')
        BlueElephantR = Elephant(9, 6, 'B')
        x_board[BlueElephantL.get_x()][BlueElephantL.get_y()] = BlueElephantL
        x_board[BlueElephantR.get_x()][BlueElephantR.get_y()] = BlueElephantR
        RedHorseL = Horse(0, 2, 'R')
        RedHorseR = Horse(0, 7, 'R')
        x_board[RedHorseL.get_x()][RedHorseL.get_y()] = RedHorseL
        x_board[RedHorseR.get_x()][RedHorseR.get_y()] = RedHorseR
        BlueHorseL = Horse(9, 2, 'B')
        BlueHorseR = Horse(9, 7, 'B')
        x_board[BlueHorseL.get_x()][BlueHorseL.get_y()] = BlueHorseL
        x_board[BlueHorseR.get_x()][BlueHorseR.get_y()] = BlueHorseR
        RedGuardL = Guard(0, 3, 'R')
        RedGuardR = Guard(0, 5, 'R')
        x_board[RedGuardL.get_x()][RedGuardL.get_y()] = RedGuardL
        x_board[RedGuardR.get_x()][RedGuardR.get_y()] = RedGuardR
        BlueGuardL = Guard(9, 3, 'B')
        BlueGuardR = Guard(9, 5, 'B')
        x_board[BlueGuardL.get_x()][BlueGuardL.get_y()] = BlueGuardL
        x_board[BlueGuardR.get_x()][BlueGuardR.get_y()] = BlueGuardR
        RedGeneral = General(1, 4, 'R')
        BlueGeneral = General(8, 4, 'B')
        x_board[RedGeneral.get_x()][RedGeneral.get_y()] = RedGeneral
        x_board[BlueGeneral.get_x()][BlueGeneral.get_y()] = BlueGeneral
        RedCannonL = Cannon(2, 1, 'R')
        RedCannonR = Cannon(2, 7, 'R')
        x_board[RedCannonL.get_x()][RedCannonL.get_y()] = RedCannonL
        x_board[RedCannonR.get_x()][RedCannonR.get_y()] = RedCannonR
        BlueCannonL = Cannon(7, 1, 'B')
        BlueCannonR = Cannon(7, 7, 'B')
        x_board[BlueCannonL.get_x()][BlueCannonL.get_y()] = BlueCannonL
        x_board[BlueCannonR.get_x()][BlueCannonR.get_y()] = BlueCannonR
        RedSoldierL1 = Soldier(3, 0, 'R')
        RedSoldierR1 = Soldier(3, 2, 'R')
        x_board[RedSoldierL1.get_x()][RedSoldierL1.get_y()] = RedSoldierL1
        x_board[RedSoldierR1.get_x()][RedSoldierR1.get_y()] = RedSoldierR1
        RedSoldierL2 = Soldier(3, 6, 'R')
        RedSoldierR2 = Soldier(3, 8, 'R')
        x_board[RedSoldierL2.get_x()][RedSoldierL2.get_y()] = RedSoldierL2
        x_board[RedSoldierR2.get_x()][RedSoldierR2.get_y()] = RedSoldierR2
        RedSoldierM = Soldier(3, 4, 'R')
        BlueSoldierM = Soldier(6, 4, 'B')
        x_board[RedSoldierM.get_x()][RedSoldierM.get_y()] = RedSoldierM
        x_board[BlueSoldierM.get_x()][BlueSoldierM.get_y()] = BlueSoldierM
        BlueSoldierL1 = Soldier(6, 0, 'B')
        BlueSoldierR1 = Soldier(6, 2, 'B')
        x_board[BlueSoldierL1.get_x()][BlueSoldierL1.get_y()] = BlueSoldierL1
        x_board[BlueSoldierR1.get_x()][BlueSoldierR1.get_y()] = BlueSoldierR1
        BlueSoldierL2 = Soldier(6, 6, 'B')
        BlueSoldierR2 = Soldier(6, 8, 'B')
        x_board[BlueSoldierL2.get_x()][BlueSoldierL2.get_y()] = BlueSoldierL2
        x_board[BlueSoldierR2.get_x()][BlueSoldierR2.get_y()] = BlueSoldierR2
        return x_board

    def make_move(self, ab, cd):
        """
        The make moves takes in two possible option - ab, cd which refers to the current and next position
        The positions are then modified and formatted to numbers for indexing(our board game is a 2d array)
        Make moves check the following item:
        If the player is able to make a move after checkmate
        If the letter is "higher" than I or larger than 10 (out of board position)
        If the two positions are the same, we skip a turn
        If the start piece actually exist
        If the current move captures the same color pieces
        If the current move is validate (example: soldier ab can move to cb)
        Within the validate method option - if the item returns True, I have a another function that is ran:
        That extra function does a general_check_move which checks to see if the current turn general is in check
            if the move does leaves the general out of check or if he was never in check, the move is successful and
            does the following:
                Update Turn
                Update to see if the position cd can reach the opposite general
                Update the old position ab to '' which is considered "empty"
                Update the pieces x and y location of the piece moving to the cd option
            Else return False as the move did not escape check
        """
        start_1 = int(ab[1:]) - 1  # start refers to the starting position
        start_2 = alphabet(ab[0])  # alphabet is a function that converts
        move_1 = int(cd[1:]) - 1  # move refers to the next position
        move_2 = alphabet(cd[0])
        if self._red_checkmate is True or self._blue_checkmate is True:
            return False  # cannot move after checkmate
        elif start_1 > 10 or move_1 > 10 or move_2 is False or start_2 is False:
            return False  # handles out of bounds
        elif ab == cd:  # handles the skip turn and update turn
            if self._current_turn == 'B':
                self._current_turn = 'R'
                return True
            elif self._current_turn == 'R':
                self._current_turn = 'B'
                return True
        elif self._game_board[start_1][start_2] == '':  # handles to see if start exist
            return False
        elif self._game_board[move_1][move_2] != '' and self._game_board[move_1][move_2].get_color() == \
                self._game_board[start_1][start_2].get_color():
            return False  # handles same color piece capture
        elif self._current_turn != self._game_board[start_1][start_2].get_color():
            return False  # handles same color
        elif self._game_board[start_1][start_2].validate_move(start_1, start_2, move_1, move_2, self._game_board):
            # stimulate board movement as if the move proceeds
            temp = self._game_board[start_1][start_2]
            check = self._game_board[move_1][move_2]
            self._game_board[move_1][move_2] = temp
            self._game_board[start_1][start_2] = ''
            temp.set_y(move_2)
            temp.set_x(move_1)
            if self.general_check_move([move_1, move_2]):      # see if the new move prevents general from being
                # checked or is not
                self.update_check(move_1, move_2)
                self.update_turn()
                return True
            else:                             # If the move does not fix the general from being checked, revert actions
                temp.set_y(start_2)
                temp.set_x(start_1)
                self._game_board[move_1][move_2] = check
                self._game_board[start_1][start_2] = temp
                return False
        else:
            return False  # probably not needed

    def update_turn(self):
        """
        Used within the make_move function of this class, it updates the turn when needed
        """
        if self._current_turn == 'B':  # Update turn
            self._current_turn = 'R'
        elif self._current_turn == 'R':
            self._current_turn = 'B'

    def get_game_state(self):
        """
        This function determines the current state of the game. If both the generals are not checkmate (false),
        then the game is not finished If a general is checkmate, it will return the current
        state
        """
        if self._red_checkmate is False and self._blue_checkmate is False:
            return 'UNFINISHED'
        elif self._red_checkmate:
            return 'BLUE_WON'
        else:
            return 'RED_WON'

    def is_in_check(self, turn):
        """
        The is_in_check will check the attributes to determine if its in fact in check
        """
        if turn == 'blue' and self._blue_check is True:
            return True
        elif turn == 'red' and self._red_check is True:
            return True
        else:
            return False


def alphabet(letter):
    """
    Since our board used an indexing and the character that is used to make move, we need a converter to translate a to
    the first position, b to the second position etc. Since our board goes up to I, anything else will return false for
    our check
    """
    if letter == 'a':
        return 0
    elif letter == 'b':
        return 1
    elif letter == 'c':
        return 2
    elif letter == 'd':
        return 3
    elif letter == 'e':
        return 4
    elif letter == 'f':
        return 5
    elif letter == 'g':
        return 6
    elif letter == 'h':
        return 7
    elif letter == 'i':
        return 8
    else:
        return False


class Piece:
    """This is the super class of Pieces. It provides the templates for each sub class. Each class has more specific
    details if needed, but this should cover most of the pieces.
    """

    def __init__(self, x, y, color):
        """X/Y is the current position of the piece. Color represents the team. Name is set to none for now"""
        self._name = None
        self._x = x
        self._y = y
        self._color = color

    def get_x(self):
        """Returns the x position"""
        return self._x

    def get_y(self):
        """Returns the y position"""
        return self._y

    def set_y(self, new_y):
        """Updates the y position"""
        self._y = new_y

    def set_x(self, new_x):
        """Updates the x position"""
        self._x = new_x

    def get_color(self):
        """Returns the color of the piece"""
        return self._color

    def validate_move(self, x1, y1, x2, y2, board):
        """
        Each piece will have a variations of their moves.
        x1/y1 and x2/y2 represents the current and new positions. The validations first will check to see if the move is
        in fact valid. Next it will then check to see if the movement it can move to will put the general in check. If
        the current move puts the general in check, we will use the instance of the general to make the next move.
        """
        return True

    def __repr__(self):
        """Returns the name of the piece when printing"""
        return self._name


class Chariot(Piece):
    """
    Chariot is a sub class of Pieces
    Two per side of board
    """

    def __init__(self, x, y, color):
        """Chariot is represented by C and will print [color here]C on board"""
        Piece.__init__(self, x, y, color)
        self._name = self._color + 'C'

    def validate_move(self, x1, y1, x2, y2, board):
        """
        Chariot can move up/down and left/right a board, but can not jump over any pieces
        It can move diagonal within the palace
        """
        if x1 == x2:  # checks to see if its a valid side movement
            if y1 < y2:  # checks for unit obstruction if board is going right
                counter = y1 + 1
                current = board[x1][counter]
                while counter != y2:
                    if current != '':
                        return False
                    counter += 1
                    current = board[x1][counter]
                return True
            if y1 > y2:  # checks for unit obstruction if board is going left
                counter = y1 - 1
                current = board[x1][counter]
                while counter != y2:
                    if current != '':
                        return False
                    counter -= 1
                    current = board[x1][counter]
            return True
        elif y1 == y2:  # check to see if its a valid movement up/down movement
            if x1 > x2:  # checks for unit obstruction if board is up
                counter = x1 - 1
                current = board[counter][y1]
                while counter != x2:
                    if current != '':
                        return False
                    counter -= 1
                    current = board[counter][y1]
            if x1 < x2:  # checks for unit obstruction if board is down
                counter = x1 + 1
                current = board[counter][y1]
                while counter != x2:
                    if current != '':
                        return False
                    counter += 1
                    current = board[counter][y1]
            return True
        elif y2 in [4, 5, 6] and y1 in [4, 5, 6] and x2 in [0, 1, 2, 9, 8, 7] and x1 in [0, 1, 2, 9, 8, 7]:
            if y2 - y1 in [-1 or 1] and y2 - y1 in [1 or -1]:
                return True  # checks to see if current location in palace and if diagonal movement can be made
            else:
                return False
        else:
            return False


class Elephant(Piece):
    """
    Elephant is a sub class of Pieces.
    Two per sides of board
    """

    def __init__(self, x, y, color):
        """Elephant is represented by E and will print [color here]E on board"""
        Piece.__init__(self, x, y, color)
        self._name = self._color + 'E'

    def validate_move(self, x1, y1, x2, y2, board):
        """
        Elephant can move one position in a line and then two outwards diagonally.
        Movement can be blocked anywhere"""
        if x1 - x2 == 3:  # handles up movement
            if y1 - y2 == -2:  # handles right
                if board[x1 - 1][y1] != '' or board[x1 - 2][y1 + 1] != '':
                    return False
                else:
                    return True
            elif y1 - y2 == 2:  # handles left
                if board[x1 - 1][y1] != '' or board[x1 - 2][y1 - 1] != '':
                    return False
                else:
                    return True
            else:
                return False
        elif y1 - y2 == 3:  # handles left movement
            if x1 - x2 == 2:  # handles up movement
                if board[x1][y1 - 1] != '' or board[x1 - 1][y1 - 2] != '':
                    return False
                else:
                    return True
            elif x1 - x2 == -2:  # handles right movement
                if board[x1][y1 - 1] != '' or board[x1 + 1][y1 - 2] != '':
                    return False
                else:
                    True
        elif x1 - x2 == -3:  # handles down movement
            if y1 - y2 == -2:  # handles right movement
                if board[x1 + 1][y1] != '' or board[x1 + 2][y1 + 1] != '':
                    return False
                else:
                    return True
            elif y1 - y2 == 2:  # handles left movement
                if board[x1 + 1][y1] != '' or board[x1 + 2][y1 - 1] != '':
                    return False
                else:
                    return True
        elif y1 - y2 == -3:  # handles right movement
            if x1 - x2 == 2:  # handles up movement
                if board[x1][y1 + 1] != '' or board[x1 - 1][y1 + 2] != '':
                    return False
                else:
                    return True
            elif x1 - x2 == -1:  # handles down movement
                if board[x1][y1 + 1] != '' or board[x1 + 1][y1 + 2] != '':
                    return False
                else:
                    return True
        else:
            return False


class Horse(Piece):
    """
    Horse is a sub class of Pieces.
    Two per sides of board
    """

    def __init__(self, x, y, color):
        """Horse is represented by H and will print [color here]H on board"""
        Piece.__init__(self, x, y, color)
        self._name = self._color + 'H'

    def validate_move(self, x1, y1, x2, y2, board):
        """Horse moves one position in a straight line and then one position diagonal. It can be blocked"""
        if x2 - x1 == -2:  # handles left movement
            if board[x1 - 1][y1] == '' and (y2 - y1 == 1 or y2 - y1 == -1):
                return True
            else:
                return False
        elif x2 - x1 == 2:  # handles right movement
            if board[x1 + 1][y1] == '' and (y2 - y1 == 1 or y2 - y1 == -1):
                return True
            else:
                return False
        elif y2 - y1 == 2:  # handles down movement
            if board[x1][y1 + 1] == '' and (x2 - x1 == 1 or x2 - x1 == -1):
                return True
            else:
                return False
        elif y2 - y1 == -2:  # handles up movement
            if board[x1][y1 - 1] == '' and (x2 - x1 == 1 or x2 - x1 == -1):
                return True
            else:
                return False
        else:
            return False


class Guard(Piece):
    """
    Guard is a sub class of Pieces.
    Two per sides of board
    """

    def __init__(self, x, y, color):
        """Guard is represented by G and will print [color here]G on board"""
        Piece.__init__(self, x, y, color)
        self._name = self._color + 'G'

    def validate_move(self, x1, y1, x2, y2, board):
        """Moves exactly one spot away within palace"""
        if y2 in [2, 6]:  # handles the y axis out of range
            return False
        elif self._color == 'B':
            if x2 == 6:  # handles the x axis out of range
                return False
            elif x2 - x1 in [-1, 0, 1] and y2 - y1 in [-1, 0, 1]:
                return True
            else:
                return False
        elif self._color == 'R':
            if x2 == 3:  # handles the x axis out of range
                return False
            elif x2 - x1 in [-1, 0, 1] and y2 - y1 in [-1, 0, 1]:
                return True
            else:
                return False


class General(Piece):
    """
    General is a sub class of Pieces.
    One per sides of board
    """

    def __init__(self, x, y, color):
        Piece.__init__(self, x, y, color)
        self._name = self._color + 'K'

    def validate_move(self, x1, y1, x2, y2, board):
        """General is represented by k and will print [color here]k on board"""
        if y2 in [2, 6]:  # handles the y axis out of range
            return False
        elif self._color == 'B':
            if x2 == 6:  # handles the x axis out of range
                return False
            elif x2 - x1 in [-1, 0, 1] and y2 - y1 in [-1, 0, 1]:
                return True
            else:
                return False
        elif self._color == 'R':
            if x2 == 3:  # handles the x axis out of range
                return False
            elif x2 - x1 in [-1, 0, 1] and y2 - y1 in [-1, 0, 1]:
                return True
            else:
                return False


class Cannon(Piece):
    """
    Cannon is a sub class of Pieces.
    Two per sides of board
    """

    def __init__(self, x, y, color):
        """Cannon is represented by N and will print [color here]N on board"""
        Piece.__init__(self, x, y, color)
        self._name = self._color + 'N'

    def validate_move(self, x1, y1, x2, y2, board):
        """
        Cannon can move in any straight line as long as it's at least/most 1 leap between the movement and current
        It can not jump or capture other cannons
        """
        count = 0
        if isinstance(board[x2][y2], Cannon):  # cannons can't capture other cannons
            return False
        elif y1 == y2:  # movement is up and down board:
            if x1 > x2:  # movement is up
                next = x1 - 1
                while x2 != next:
                    if board[next][y2] != '':
                        count += 1
                        if isinstance(board[next][y2], Cannon):  # can't jump over cannon
                            return False
                    next -= 1
                if next == x2 and count == 1:
                    return True
                else:
                    return False

            elif x1 < x2:  # movement is down
                next = x1 + 1
                while x2 != next:  # loop used to check what next item is
                    if board[next][y2] != '':
                        count += 1
                        if isinstance(board[next][y2], Cannon):  # can't jump over cannon
                            return False
                    next += 1
                if next == x2 and count == 1:
                    return True
                else:
                    return False
        elif x1 == x2:  # movement is left or right board:
            if y1 < y2:  # movement is up
                next = y1 + 1
                while y2 != next:
                    if board[x1][next] != '':
                        count += 1
                        if isinstance(board[x1][next], Cannon):  # can't jump over cannon
                            return False
                    next += 1
                if count == 1 and next == y2:
                    return True
                else:
                    return False
            elif y1 > y2:  # movement is up
                next = y1 - 1
                while y2 != next:
                    if board[x1][next] != '':
                        count += 1
                        if isinstance(board[x1][next], Cannon):  # can't jump over cannon
                            return False
                    next -= 1
                if next == y2 and count == 1:
                    return True
                else:
                    return False
        elif x2 - x1 == y1 - y2 and (y1 in [5, 3] and y2 in [5, 3]):  # goes down/left and up/right
            if board[x2 - 1][y1 - 1] != '':
                return True
            else:
                return False
        elif x2 - x1 == y2 - y1 and (y1 in [5, 3] and y2 in [5, 3]):  # goes down/right and up/left:
            if board[x2 - 1][y2 - 1] != '':
                return True
            else:
                return False
        else:
            return False


class Soldier(Piece):
    """
    Soldier is a sub class of Pieces.
    5 per sides of board
    """

    def __init__(self, x, y, color):
        """Soldier is represented by S and will print [color here]S on board"""
        Piece.__init__(self, x, y, color)
        self._name = self._color + 'S'

    def validate_move(self, x1, y1, x2, y2, board):
        """Can move forward or left/right. Can move diagonal in palace"""
        if self._color == 'B':
            if x1 in [0, 1, 2] and x2 in [0, 1, 2] and y2 in [3, 4, 5] and y1 in [3, 4, 5] and x1 - x2 in [-1,
                                                                                                           1] and y1 - y2 in [
                -1, 1]:
                return True  # handles diagonal
            elif x1 - x2 == 1 and y2 - y1 == 0:
                return True  # handles forward
            elif (y1 - y2 == 1 or y1 - y2 == -1) and (x1 - x2 == 0):
                return True  # handles left and right
            else:
                return False
        else:
            if x1 in [9, 7, 8] and x2 in [9, 7, 8] and y2 in [3, 4, 5] and y2 in [3, 4, 5] and x1 - x2 in [-1,
                                                                                                           1] and y1 - y2 in [
                -1, 1]:
                return True  # handles diagonal
            elif x1 - x2 == -1 and y2 - y1 == 0:
                return True  # handles forward
            elif (y1 - y2 == -1 or y1 - y2 == 1) and (x1 - x2 == 0):
                return True  # handles left and right
            else:
                return False


def main():
    game = JanggiGame()
    print(game)
    
if __name__ == '__main__':
    main()
