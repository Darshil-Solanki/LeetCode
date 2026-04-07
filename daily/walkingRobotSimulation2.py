class Robot:

    def __init__(self, width: int, height: int):
        self._width, self._height = width-1, height-1
        self._circum = 2*(width+height-2)
        self._mod_steps = 0
        self._is_start = True

    def step(self, num: int) -> None:
        if num>0:
            self._is_start = False
        self._mod_steps = (self._mod_steps+num) % self._circum

    def getPos(self) -> List[int]:
        if self._mod_steps <= self._width:
            return [self._mod_steps, 0]
        elif self._mod_steps <= self._width+self._height:
            return [self._width, self._mod_steps-self._width]
        elif self._mod_steps <= 2*self._width + self._height:
            return [2*self._width+self._height - self._mod_steps, self._height]
        else:
            return [0, self._circum-self._mod_steps]

    def getDir(self) -> str:
        if self._is_start:
            return "East"
        if self._mod_steps == 0:
            return "South"
        elif self._mod_steps <= self._width:
            return "East"
        elif self._mod_steps <= self._width + self._height:
            return "North"
        elif self._mod_steps <= 2 * self._width + self._height:
            return "West"
        else:
            return "South"


# Your Robot object will be instantiated and called as such:
# obj = Robot(width, height)
# obj.step(num)
# param_2 = obj.getPos()
# param_3 = obj.getDir()
