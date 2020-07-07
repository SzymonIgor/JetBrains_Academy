class Machine:
    SUPPLIES = {'water': 400,
                'milk': 540,
                'beans': 120,
                'cups': 9,
                'money': 550}

    COFFEE_TYPES = {'1': {'water': 250,
                          'milk': 0,
                          'beans': 16,
                          'cups': 1,
                          'money': -4},
                    '2': {'water': 350,
                          'milk': 75,
                          'beans': 20,
                          'cups': 1,
                          'money': -7},
                    '3': {'water': 200,
                          'milk': 100,
                          'beans': 12,
                          'cups': 1,
                          'money': -6}
                    }

    def __init__(self):
        self.supplies = self.SUPPLIES
        self.loop()

    def get_supplies(self):
        output = f'\nThe coffee machine has:\n'
        for text, key in zip([('', ''),  # water
                              ('', ''),  # milk
                              ('', 'coffee '),  # beans
                              ('', 'disposable '),  # cups
                              ('$', '')],  # money
                             self.supplies):
            output += f'{text[0]}{self.supplies[key]} of {text[1]}{key}\n'
        return output

    def produce_coffee(self, coffee_no):
        try:
            coffee = self.COFFEE_TYPES[coffee_no]
            for (k_s, v_s), (k_c, v_c) in zip(self.supplies.items(), coffee.items()):
                if v_s - v_c < 0:
                    print(f'Sorry, not enough {k_s}')
                    break
            else:
                print('I have enough resources, making you a coffee!')
                self.supplies = {key: self.supplies[key] - coffee[key] for key in self.SUPPLIES}
        except ValueError:
            raise Exception('Wrong type of coffee')

    def reaction(self, act):
        if act == 'buy':
            print('\nWhat do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:')
            bought = input()
            if bought == 'back':
                pass
            elif bought in self.COFFEE_TYPES:
                self.produce_coffee(bought)
            else:
                print('No such action. Please, try again.')

        elif act == 'fill':
            # in zip(...) there are enough tuples to connect them with everything but money
            for text, key in zip((('ml of', ''),  # water
                                  ('ml of', ''),  # milk
                                  ('grams of coffee', ''),  # beans
                                  ('disposable', 'of coffee ')),  # cups
                                 self.supplies):
                print(f'Write how many {text[0]} {key} {text[1]}do you want to add:')
                self.supplies[key] += int(input())
        elif act == 'take':
            print(f'\nI gave you ${self.supplies["money"]}')
            self.supplies["money"] = 0
        elif act == 'remaining':
            print(self.get_supplies())
        else:
            print('No such action. Please, try again.')

    def loop(self):
        while True:
            print('\nWrite action (buy, fill, take, remaining, exit):')
            action = input()
            if action == 'exit':
                break
            else:
                self.reaction(action)


my_machine = Machine()
