class MyHashMap:

    def __init__(self):
        self.map = [-1]*(10**6 + 1)

    def put(self, key: int, value: int) -> None:
        self.map[key] = value

    def get(self, key: int) -> int:
        return self.map[key]

    def remove(self, key: int) -> None:
        self.map[key] = -1


if __name__ == "__main__":
    obj = MyHashMap()
    obj.put(1, 10)
    obj.put(2, 20)
    print(obj.get(1))   # Output 10
    print(obj.get(3))   # Output -1 (kyunki key 3 exist nahi karti)
    obj.put(2, 30)
    print(obj.get(2))   # Output 30
    obj.remove(2)
    print(obj.get(2))
