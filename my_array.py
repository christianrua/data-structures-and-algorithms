class MyArray():
    
    def __init__(self) -> None:
        self.length = 0
        self.data = {}

    def _re_arrenge_index(self, index_to_be_drop):
        for index in range(len(self.data) - index_to_be_drop):
            self.data[index + index_to_be_drop] = self.data[index + index_to_be_drop + 1]
            del self.data[index + index_to_be_drop + 1] 
            

    def get(self, index):
        return self.data[index]

    def push(self, item):
        self.data[self.length] = item 
        self.length += 1
        return self.length   

    def pop(self):
        last_item = self.data[self.length - 1]
        del self.data[self.length - 1]    
        self.length -= 1
        return last_item

    def delete(self, index):
        #item = self.data[index]
        del self.data[index] 
        self.length -= 1
        self._re_arrenge_index(index)

    def get_internal_data(self):
        return self.data, self.length    

new_array = MyArray() 
print(new_array.push('hi'))
print(new_array.push('you'))
print(new_array.get(0))
print(new_array.get(1))  
print(new_array.push('!'))
print(new_array.pop()) 
print(new_array.push('you were there'))  
print(new_array.push('!'))  
print(new_array.get_internal_data())
print(new_array.delete(1))
print(new_array.get_internal_data())
