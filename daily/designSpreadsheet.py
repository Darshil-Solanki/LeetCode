class Spreadsheet:

    def __init__(self, rows: int):
        self.sheet = defaultdict(int)

    def setCell(self, cell: str, value: int) -> None:
        self.sheet[cell] = value

    def resetCell(self, cell: str) -> None:
        self.sheet[cell] = 0

    def getValue(self, formula: str) -> int:
        a, b = formula[1:].split("+")
        if a[0].isdigit():
            a = int(a)
        else:
            a = self.sheet[a]
        if b[0].isdigit():
            b = int(b)
        else:
            b = self.sheet[b]
        return a+b


# Your Spreadsheet object will be instantiated and called as such:
# obj = Spreadsheet(rows)
# obj.setCell(cell,value)
# obj.resetCell(cell)
# param_3 = obj.getValue(formula)
