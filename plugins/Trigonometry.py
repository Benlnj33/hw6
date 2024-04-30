from plugin_interface import Plugin
import math

class TrigonometryPlugin(Plugin):
    def get_name(self):
        return "Trigonometry Plugin"

    def get_commands(self):
        return {
            'sin': self.do_sin,
            'cos': self.do_cos,
            'tan': self.do_tan
        }

    def do_sin(self, arg):
        try:
            operand = float(arg)
            result = math.sin(operand)
            print('Result:', result)
        except ValueError:
            print('Invalid input. Please enter a valid number.')

    def do_cos(self, arg):
        try:
            operand = float(arg)
            result = math.cos(operand)
            print('Result:', result)
        except ValueError:
            print('Invalid input. Please enter a valid number.')

    def do_tan(self, arg):
        try:
            operand = float(arg)
            result = math.tan(operand)
            print('Result:', result)
        except ValueError:
            print('Invalid input. Please enter a valid number.')