class Filter:
    def process(self, data):
        raise NotImplementedError("Subclasses must implement the 'process' method.")


class UppercaseFilter(Filter):
    def process(self, data):
        return data.upper()


class ReverseFilter(Filter):
    def process(self, data):
        return data[::-1]


class Pipe:
    def __init__(self, filters):
        self.filters = filters

    def process(self, data):
        for filter in self.filters:
            data = filter.process(data)
        return data


# Usage example
def main():
    data = "Hello, World!"

    filter1 = UppercaseFilter()
    filter2 = ReverseFilter()
    pipe = Pipe([filter1, filter2])

    result = pipe.process(data)
    print(result)


if __name__ == "__main__":
    main()
