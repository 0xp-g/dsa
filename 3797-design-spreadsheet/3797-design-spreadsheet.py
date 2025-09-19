class Spreadsheet():

    def __init__(self, rows):
        self.hmap = {}

    def setCell(self, cell, value):
        self.hmap[cell] = value

    def resetCell(self, cell):
        self.hmap[cell] = 0

    def getValue(self, formula):
        formula = formula[1:]
        for i in range(len(formula)):
            if formula[i] == '+':
                s1, s2 = formula[:i], formula[i+1:]
                left = self.hmap.get(s1, 0) if s1[0].isupper() else int(s1)
                right = self.hmap.get(s2, 0) if s2[0].isupper() else int(s2)
                return left + right
        return 0

# Your Spreadsheet  will be instantiated and called as such:
# obj = Spreadsheet(rows)
# obj.setCell(cell,value)
# obj.resetCell(cell)
# param_3 = obj.getValue(formula)