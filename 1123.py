class Test:
    def __init__(self, number_list) -> None:
        self.nl = number_list
   
    @classmethod
    def bubble_sorted(cls, number_list):
        for i in range(len(number_list)-1):
            for j in range(len(number_list)-1-i):
                if number_list[j] > number_list[j+1]:
                    number_list[j], number_list[j+1] = number_list[j+1], number_list[j]
        return cls(number_list)
    
    def see_nl(self):
        print(self.nl)

a = [1,2,3,4,5,6,1,2,3,4,6,7]

test = Test.bubble_sorted(a)
print(f'{test.nl=}')
test.see_nl()
