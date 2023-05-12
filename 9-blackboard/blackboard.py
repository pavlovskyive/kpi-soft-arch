class Blackboard:
    def __init__(self):
        self.knowledge = []

    def add_knowledge(self, knowledge):
        self.knowledge.append(knowledge)

    def get_knowledge(self):
        return self.knowledge


class KnowledgeSource:
    def __init__(self, blackboard):
        self.blackboard = blackboard

    def update_knowledge(self, knowledge):
        self.blackboard.add_knowledge(knowledge)


class Monitor:
    def __init__(self, blackboard):
        self.blackboard = blackboard

    def display_knowledge(self):
        knowledge = self.blackboard.get_knowledge()
        print("Displaying knowledge:", knowledge)


if __name__ == '__main__':
    # Create instances of the Blackboard, KnowledgeSource, and Monitor
    blackboard = Blackboard()
    knowledge_source = KnowledgeSource(blackboard)
    monitor = Monitor(blackboard)

    # Update knowledge and display
    print("Adding Knowledge 1")
    knowledge_source.update_knowledge("Knowledge 1")
    monitor.display_knowledge()
    print()

    print("Adding Knowledge 2")
    knowledge_source.update_knowledge("Knowledge 2")
    monitor.display_knowledge()
    print()

    print("Adding Knowledge 3")
    knowledge_source.update_knowledge("Knowledge 3")
    monitor.display_knowledge()
    print()
