class Person(object):

    def __init__(self, name, age, number_arms):
        self.name = name
        self.age = age
        self.number_arms = number_arms
    def print_arm1(self):
        template = '{} has {} arm.'
        plural = '' if self.number_arms == 1 else 's'
        message = template.format(self.name, self.number_arms, plural)
        print(message)

    def print_arm2(self):
        template = "{} has {} arm"
        if self.number_arms == 1:
            plural = ''
        else:
            plural = 's'
       message = template.format(self.name, self.number_arms,plural)
       print(message)

    def print_arms(self):
        template = '{} has {} arms'
        message = template.format(self.name, self.number_arms)
        if self.number_arms >= 2:
            print(message)
        else:
            template = '{} has {} arm'
            message1 = template.format(self.name, self.number_arms)
            print(message1)

paul = Person('paul',20,2)
mary = Person('mary', 35,2)
joe = Person('joe', 22, 3)
patchy = Person( 'patchy', 35, 1)

paul.print_arms()
patchy.print_arms()


