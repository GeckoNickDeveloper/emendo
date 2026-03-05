# Imports
from datetime import datetime
from enum import Enum, auto
from . import Color



# LogLevel definitions
class LogLevel(Enum):
    DEBUG    = auto()
    INFO     = auto()
    WARNING  = auto()
    ERROR    = auto()
    CRITICAL = auto()



# Logger definition
class Logger:
    # Extern MACROs without complicating readability
    DEBUG    = LogLevel.DEBUG
    INFO     = LogLevel.INFO
    WARNING  = LogLevel.WARNING
    ERROR    = LogLevel.ERROR
    CRITICAL = LogLevel.CRITICAL
    
    # Constructor
    def __init__(self, level = LogLevel.INFO, file: str = None):
        self.level = level
        self.file = file
        
        # Colors
        self.__colors = {
            LogLevel.DEBUG:     Color.hex("#747474"),
            LogLevel.INFO:      Color.hex("#3693d1"),
            LogLevel.WARNING:   Color.hex("#ffb04f"),
            LogLevel.ERROR:     Color.hex("#ff614f"),
            LogLevel.CRITICAL:  Color.hex("#ca4fff"),
        }

    # Log primitive
    def _log(self, level: LogLevel, msg: str):
        if level.value >= self.level.value:
            # Log string building
            ts = datetime.now().strftime("%H:%M:%S.%f")
            
            color = self.__colors[level]
            reset = '\033[0m'
            color_string = f"\033[38;2;{color.r};{color.g};{color.b}m"
            
            log = f"[{ts}] [{level.name[0]}] - {msg}"
            
            # Write on file
            if self.file != None:
                try:
                    with open(self.file, "a") as f:
                        f.write(f"{log}\n")
                except:
                    raise FileNotFoundError
            
            # Actual colored log
            print(f"{color_string}{log}{reset}")



    # Logging Methods
    def debug(self, msg):
        self._log(LogLevel.DEBUG, msg)

    def info(self, msg):
        self._log(LogLevel.INFO, msg)

    def warning(self, msg):
        self._log(LogLevel.WARNING, msg)

    def error(self, msg):
        self._log(LogLevel.ERROR, msg)
    
    def critical(self, msg):
        self._log(LogLevel.CRITICAL, msg)
        
    
    
    # Customization Methods
    def set_color(self, level: LogLevel, color: Color):
        self.__colors[level] = color
        
    def show_colors(self):
        reset = '\033[0m'
        
        msg = ''
        msg += 'Logger colors:\n'
        
        lcolor = f"\033[38;2;{self.__colors[self.DEBUG].r};{self.__colors[self.DEBUG].g};{self.__colors[self.DEBUG].b}m"
        msg += f'  {lcolor}DEBUG:    {self.__colors[self.DEBUG].stringify()}{reset}\n'
        
        lcolor = f"\033[38;2;{self.__colors[self.INFO].r};{self.__colors[self.INFO].g};{self.__colors[self.INFO].b}m"
        msg += f'  {lcolor}INFO:     {self.__colors[self.INFO].stringify()}{reset}\n'
        
        lcolor = f"\033[38;2;{self.__colors[self.WARNING].r};{self.__colors[self.WARNING].g};{self.__colors[self.WARNING].b}m"
        msg += f'  {lcolor}WARNING:  {self.__colors[self.WARNING].stringify()}{reset}\n'
        
        lcolor = f"\033[38;2;{self.__colors[self.ERROR].r};{self.__colors[self.ERROR].g};{self.__colors[self.ERROR].b}m"
        msg += f'  {lcolor}ERROR:    {self.__colors[self.ERROR].stringify()}{reset}\n'
        
        lcolor = f"\033[38;2;{self.__colors[self.CRITICAL].r};{self.__colors[self.CRITICAL].g};{self.__colors[self.CRITICAL].b}m"
        msg += f'  {lcolor}CRITICAL: {self.__colors[self.CRITICAL].stringify()}{reset}'
        
        print(msg)