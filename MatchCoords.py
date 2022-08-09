def Match(sets):
    class Intersection():
        def __init__ (self, sets):
            self.sets = sets
        def concArrays(self):
            self.sets = self.sets[0] + self.sets[1]
            return self.sets
        def sortList(self):
            self.sets = sorted(self.sets, key=lambda x: x[0])
            return sorted(self.sets, key=lambda x: x[1])
        def clash(self):
            return [self.sets[i] for i in range(0, len(self.sets)-1) if self.sets[i] == self.sets[i+1]]
    sets = [[(2,4),(5,3),(2,6),(6,2),(4,9)],[(4,9),(10,8),(9,3),(5,3),(1,7)]]
    inter = Intersection(sets)
    inter.concArrays()
    inter.sortList()
    print(inter.clash())
