import logging
import math
from logging import error, info


class Cars(object):
    def __init__(self):
        self.x = None  # num of red cars
        self.y = None  # num of white cars

    def take_input(self, warning=False):
        """
        Input from user ( X and Y)
        X = Red cars, Y = White cars
        :warning: Inform user if error occurred
        :return: None
        """

        try:
            if warning:
                print('Input should be numeric..')
            if not self.x:
                x = input('Enter number of red cars:')
                if not x.isdigit():
                    self.take_input(warning=True)
                    return
                else:
                    self.x = int(x)
            if not self.y:
                y = input('Enter number of white cars:')
                if not y.isdigit():
                    self.take_input(warning=True)
                    return
                else:
                    self.y = int(y)
            if not Cars.check_inputs(x=self.x, y=self.y):
                print('It is not possible to place {} red , {} white cars as expected'.format(self.x, self.y))
                self.x = None
                self.y = None
                self.take_input()
            else:
                self.form_string(print_output=True)
        except Exception as e:
            error(e)

    @staticmethod
    def check_inputs(x, y) -> bool:
        """
        Check if result can be reached with current x and y
        :param x:
        :param y:
        :return:
        """
        try:
            # We can allow twice more y cars in relation to x and vise-versa
            if x / y > 2 or y / x > 2:
                return False
            return True
        except Exception as e:
            error(e)

    def form_string(self, x=None, y=None, red_icon='R', white_icon='W', print_output=False):
        """
        Return string of x and y
        :x: Number of red cars
        :y: Number of white cars
        :red_icon:
        :white_icon:
        :print_output: Print string to terminal, if true
        :return: string
        """

        try:
            if not (x and y):
                if self.x and self.y:
                    x = self.x
                    y = self.y
                else:
                    print('x or y is not given..')
                    return
            else:
                if not Cars.check_inputs(x=x, y=y):
                    print('It is not possible to place {} red , {} white cars as expected'.format(x, y))
                    return
            a = x
            b = y
            c = 'x'
            d = 'y'
            if x < y:
                if x * 2 == y:
                    b -= 2
                a = x
                b = b
            if y < x:
                if y * 2 == x:
                    a -= 2
                b = a
                a = y
                c = 'y'
                d = 'x'
            total_cars = a + b
            string = ''
            flag = True # If true -> print x else y
            for i in range(0, total_cars, 1):

                if flag:
                    if a > 0:
                        string += c
                        a -= 1
                        flag = False
                else:
                    if b > 0:
                        if a == b:
                            string += d
                            b -= 1
                            flag = True
                        else:
                            if b >= 2:
                                string += d + d
                                b -= 2
                            else:
                                string += d
                                b -= 1
                            flag = True
            if x < y and x * 2 == y:
                string = 'y' + string + 'y'
            if y < x == y * 2:
                string = 'x' + string + 'x'

            if print_output:
                print(string)
            return string
        except Exception as e:
            error(e)
