class MyArrayList:
    # 默认初始容量1
    INIT_CAP = 1

    def __init__(self, init_capacity=None):
        selfdata = [None] *(init_capacity if init_capacity is not None else self.__class__.INIT_CAP)
        self.size = 0
    
    #增
    def add_last(self,e):
        cap = len(self.data)
        if self.size == cap:
            self.resize(cap*2)
        self.data[self.size] = e
        self.size += 1
    def add(self,index,e):
        # 先判断index是否合法
        self._check_position_index(index)
        # 判断是否需要扩容
        if self.size == len(self.data):
            self.resize(len(self.data)*2)
        # 从尾部开始移动元素
        for i in range(self.size-1,index-1,-1):
            self.data[i+1] = self.data[i]
        # 放入新元素
        self.data[index] = e
        self.size += 1
    def add_first(self,e):
        self.add(0,e)
    




    def _is_position_index(self, index):
        return index >= 0 and index < self.size
    def _check_position_index(self, index):
        if not self._is_position_index(index):
            raise IndexError(f"Index:{index},Size:{self.size}")

