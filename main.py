class Lists:
    def __init__(self, list1, list2):
        self.list1 = list1
        self.list2 = list2

    def get_averages(self):
        avg1 = 0
        if self.list1:
            avg1 = sum(self.list1) / len(self.list1)
        avg2 = 0
        if self.list2:
            avg2 = sum(self.list2) / len(self.list2)
        return avg1, avg2

    def compare(self):
        avg1, avg2 = self.get_averages()
        if avg1 > avg2:
            print('Avg list 1 > avg list2')
        elif avg1 < avg2:
            print('Avg list 1 < avg list2')
        else:
            print('Avg list 1 = avg list2')
