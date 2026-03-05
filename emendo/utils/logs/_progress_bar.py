# Imports
from . import Color
import os


# ProgressBar definition
class ProgressBar():
    def __init__(self, total: int = 1000, length: int = 80, fill: str = '▬', void: str = ' ', color: Color = None):
        self.available_tsize = False
        
        # Check if 'get_terminal_size' is available
        if 'get_terminal_size' in os.__all__:
            try:
                os.get_terminal_size()
                self.available_tsize = True
            except:
                self.available_tsize = False
        else:
            self.available_tsize = False
        
        self.reset(total, length, fill, void, color)
        # self.total      = total
        # self.length     = length
        # self.fill       = fill
        # self.void       = void
        # self.current    = 0
        # self.color      = color
        
        # self.__init()

    def update(self, step = 1):
        self.current += step
        
        # Compute percentage string
        percentage = 100.0 * (self.current / float(self.total))
        percent = ('{0:.2f}').format(percentage)

        # Compute progress bar string
        filled_len = int(self.length * self.current // self.total)
        if self.color != None:
            bar = f'\x1B[38;2;{self.color.r};{self.color.g};{self.color.b}m'
        bar += self.fill * filled_len
        if self.color != None:
            bar += '\x1B[0m'
        bar += self.void * (self.length - filled_len)
        

        # Progress Bar
        ## Save cursor position
        self.__save_cursor()
        # Move the cursor to the bottom line
        self.__move_cursor_to_bottom()

        print(f'\r[{self.current}/{self.total}] [{bar}] {percent}%', end = '')

        ## Restore cursor position
        self.__restore_cursor()
        
        if self.current >= self.total:
            self.__deinit()

    def reset(self, total: int, length: int = 80, fill: str = '▬', void: str = ' ', color: Color = Color.hex('#FF00FF')):
        self.total      = total
        self.length     = length
        self.fill       = fill
        self.void       = void
        self.current    = 0
        self.color      = color
        
        self.__init()

    # Cursor operations
    ## Init bottom progressbar
    def __init(self):
        if self.available_tsize:
            # Ensure the last line is available
            print('\n', end = '')
            
            # Save cursor position
            self.__save_cursor()
            # Set the scrollable region
            self.__set_scroll_region()
            # Restore the cursor position
            self.__restore_cursor()
            # Move up one line
            self.__move_cursor_up()

    ## Deinit bottom progressbar
    def __deinit(self):
        if self.available_tsize:
            # Save cursor position
            self.__save_cursor()
            # Reset the scrollable region
            self.__reset_scroll_region()
            # Move the cursor to the bottom line
            self.__move_cursor_to_bottom()
            # Clear line
            self.__clear_line()
            # Restore the cursor position
            self.__restore_cursor()

    ## Save cursor position
    def __save_cursor(self):
        if self.available_tsize:
            print('\x1B7', end = '')
        
    ## Restore cursor position
    def __restore_cursor(self):
        if self.available_tsize:
            print('\x1B8', end = '')

    ## Clear line
    def __clear_line(self):
        if self.available_tsize:
            print('\x1B[2K', end = '')
        
    ## Set scroll region
    def __set_scroll_region(self):
        if self.available_tsize:
            print(f'\x1B[{0};{os.get_terminal_size().lines - 1}r', end = '')
    
    ## Reset scroll region
    def __reset_scroll_region(self):
        if self.available_tsize:
            print(f'\x1B[{0};{os.get_terminal_size().lines}r', end = '')
    
    ## Move the cursor to the bottom line
    def __move_cursor_to_bottom(self):
        if self.available_tsize:
            print(f'\x1B[{os.get_terminal_size().lines};{0}H', end = '')
    
    ## Move up cursor
    def __move_cursor_up(self):
        if self.available_tsize:
            print('\x1B[1A', end = '')