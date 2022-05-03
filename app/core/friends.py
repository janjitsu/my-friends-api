class Friends:
    def __init__(self, data = {}):
        self.data = data

    def all(self):
        return [k for (k,v) in self.data.items()]

    def of(self, name):
        name = name.title()
        if name not in self.data:
            raise Exception(name + " not found")
        return self.data[name]

    def add(self, name, friends):
        not_in_data = [x for x in friends if x not in self.data.keys()]
        if not_in_data:
            raise Exception ("friends "+ ",".join(not_in_data) + " are not registered")

        self.data[name.title()] = friends
        for f in friends:
            if name not in self.data[f]:
                self.data[f].append(name)

        return self.data[name]

    def related(self, name):
        name = name.title()
        if name not in self.data:
            raise Exception(name + " not found")
        related = []
        for friend in self.data[name]:
            friends_of_friend = [x for x in self.data[friend] if x not in self.data[name] and x != name]
            related = [*related, *friends_of_friend]

        return list(dict.fromkeys(related))

