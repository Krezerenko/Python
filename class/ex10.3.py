class Hashtable:
    def __init__(self, capacity):
        self.capacity = capacity
        self.pair_chains = [[] for _ in range(capacity)]

    def put(self, key, value):
        index, chain_index = self.__get_position__(key)
        if chain_index == -1:
            self.pair_chains[index].append((key, value))
        else:
            self.pair_chains[index][chain_index] = (key, value)

    def __get_position__(self, key):
        index = hash(key) % self.capacity
        for i in range(len(self.pair_chains[index])):
            k, _ = self.pair_chains[index][i]
            if k == key:
                return index, i
        return index, -1

    def get(self, key):
        index, chain_index = self.__get_position__(key)
        if chain_index == -1:
            return None
        return self.pair_chains[index][chain_index][1]

    def size(self):
        return sum(len(chain) for chain in self.pair_chains)


def main():
    hashtable = Hashtable(capacity=10)
    hashtable.put("huh", 2)
    hashtable.put("hmm", 3)
    hashtable.put("uhm", 4)
    hashtable.put("hoo", 5)
    hashtable.put("huh", 6)
    print(hashtable.get("huh"))
    print(hashtable.get("hmm"))
    print(hashtable.get("uhm"))
    print(hashtable.get("hoo"))
    print(hashtable.size())
    print(hashtable.pair_chains)


if __name__ == '__main__':
    main()
