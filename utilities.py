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
            if abs(x - y) > 1:
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
            total_cars = x + y
            flag = True  # If true -> print red car, else white car
            if x >= y:
                string = red_icon
                flag = False
            else:
                string = white_icon
            for _ in range(1, total_cars, 1):
                if flag:
                    string += red_icon
                    flag = False
                else:
                    string += white_icon
                    flag = True
            if print_output:
                print(string)
            return string
        except Exception as e:
            error(e)
