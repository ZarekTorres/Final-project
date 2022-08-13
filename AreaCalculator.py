from tkinter import *
import math_module


class GUI:
    def __init__(self, window):

        # Instance attribute values that need to be defined here
        self.value = None
        self.radius = None
        self.result = None
        self.side = None
        self.side1 = None
        self.side2 = None
        self.length = None
        self.width = None

        self.window = window

        # Sets up the gui layout using grid method
        self.frame1 = Frame(self.window)
        self.title = Label(self.frame1, text="Calculate Area of Different Shapes", font=("arial", 20, "bold"))
        self.title.grid(row=0, column=0)
        self.choice = Label(self.frame1, text="What shape do you have?", font=("arial", 10,))
        self.choice.grid(row=1, column=0, ipadx=200)
        self.frame1.pack(side=TOP, pady=10, padx=5, ipadx=5)

        # Creates the buttons for the GUI
        self.frame2 = Frame(self.window)
        self.circle = Button(self.frame2, font=("calibre", 15), text="Circle",
                             bg="snow3", command=self.circle_entry, padx=18)
        self.circle.grid(row=0, column=0, padx=2)
        self.square = Button(self.frame2, font=("calibre", 15), text="Square",
                             bg="snow3", command=self.square_entry, padx=12)
        self.square.grid(row=0, column=1, padx=2)
        self.rectangle = Button(self.frame2, font=("calibre", 15), text="Rectangle",
                                bg="snow3", command=self.rectangle_entry)
        self.rectangle.grid(row=0, column=2, padx=2)
        self.triangle = Button(self.frame2, font=("calibre", 15), text="Triangle",
                               bg="snow3", command=self.triangle_entry, padx=8)
        self.triangle.grid(row=0, column=3, padx=2)
        self.refresh = Button(self.frame2, text="Clear Text", fg="black", command=self.fresh, bg="brown1")
        self.refresh.grid(row=0, column=4, padx=2)
        self.frame2.pack(side=TOP)

        # Creates text area for output of calculations
        self.frame3 = Frame(self.window, bg="grey94")
        self.answer = Text(self.frame3, height=10, wrap=WORD)
        self.answer.grid(padx=20, ipadx=20, pady=20, ipady=20)
        self.frame3.pack(side=BOTTOM)

    # After button click, these functions create text entries for input
    def circle_entry(self):
        value_frame1 = Frame(self.window)
        self.value = Label(value_frame1, text="○   Enter radius of Circle :")
        self.value.grid(row=0, column=0, padx=5)
        self.radius = Entry(value_frame1)
        self.radius.grid(row=0, column=1, pady=5, ipadx=5, padx=5)
        value_frame1.pack(side=TOP, pady=5, padx=5, ipadx=5)
        self.result = Button(value_frame1, text="Calculate", bg="light green", command=self.circle_area)
        self.result.grid(row=0, column=2)
        self.circle.config(state=DISABLED)

    def square_entry(self):
        value_frame1 = Frame(self.window)
        self.value = Label(value_frame1, text="☐   Enter side of Square :")
        self.value.grid(row=0, column=0, padx=5)
        self.side = Entry(value_frame1)
        self.side.grid(row=0, column=1, pady=5, ipadx=5, padx=5)
        value_frame1.pack(side=TOP, pady=5, padx=5, ipadx=5)
        self.result = Button(value_frame1, text="Calculate", bg="light green", command=self.square_area)
        self.result.grid(row=0, column=2)
        self.square.config(state=DISABLED)

    def rectangle_entry(self):
        value_frame = Frame(self.window)
        self.value = Label(value_frame, text="▭   Length :  ")
        self.value.grid(row=0, column=0, padx=5)
        self.length = Entry(value_frame)
        self.length.grid(row=0, column=1, pady=5)
        self.value = Label(value_frame, text="▭   Width :  ")
        self.value.grid(row=0, column=2, padx=5)
        self.width = Entry(value_frame)
        self.width.grid(row=0, column=3, pady=5, padx=5)
        self.result = Button(value_frame, text="Calculate", bg="light green", command=self.rectangle_area)
        self.result.grid(row=0, column=4)
        value_frame.pack(side=TOP, pady=5, padx=5, ipadx=5)
        self.rectangle.config(state=DISABLED)

    def triangle_entry(self):
        value_frame = Frame(self.window)
        self.value = Label(value_frame, text="△   Height :")
        self.value.grid(row=0, column=0, padx=5)
        self.side1 = Entry(value_frame)
        self.side1.grid(row=0, column=1)
        self.value = Label(value_frame, text="△   Base :")
        self.value.grid(row=0, column=2, padx=5)
        self.side2 = Entry(value_frame)
        self.side2.grid(row=0, column=3)
        self.result = Button(value_frame, text="Calculate", bg="light green", command=self.triangle_area)
        self.result.grid(row=0, column=4)
        value_frame.pack(side=TOP, pady=5, padx=5, ipadx=5)
        self.triangle.config(state=DISABLED)

    # These functions calculate the areas of the chosen shape
    # Using a try and except method to account for invalid input
    # Only accepts positive numbers
    def circle_area(self):
        try:
            r = float(self.radius.get())

            # Uses math_module file to check if the number is positive and then calculates the area
            circle = math_module.area_of_circle(r)

            # For output layout
            self.answer.delete(1.0, END)
            self.answer.insert(INSERT, "Area of Circle = π*r^2\n => ")
            self.answer.insert(INSERT, "π")
            self.answer.insert(INSERT, " x ")
            self.answer.insert(INSERT, str(r))
            self.answer.insert(INSERT, "^")
            self.answer.insert(INSERT, "2")
            self.answer.insert(INSERT, " = ")
            self.answer.insert(INSERT, circle)
            self.answer.insert(INSERT, " Answer. ")
            self.radius.delete(0, END)
        except ValueError:
            self.radius.delete(0, END)
            self.answer.delete(1.0, END)
            self.answer.insert(INSERT, "Please enter a positive number")

    def square_area(self):
        try:
            a = float(self.side.get())

            # Uses math_module file to check if the number is positive and then calculates the area
            square = math_module.area_of_square(a)

            # For output layout
            self.answer.delete(1.0, END)
            self.answer.insert(INSERT, "Area of Square = a^2\n => ")
            self.answer.insert(INSERT, str(a))
            self.answer.insert(INSERT, "^")
            self.answer.insert(INSERT, "2")
            self.answer.insert(INSERT, " = ")
            self.answer.insert(INSERT, square)
            self.answer.insert(INSERT, " Answer. ")
            self.side.delete(0, END)
        except ValueError:
            self.side.delete(0, END)
            self.answer.delete(1.0, END)
            self.answer.insert(INSERT, "Please enter a positive number")

    def rectangle_area(self):
        try:
            length = float(self.length.get())
            width = float(self.width.get())

            # Uses math_module file to check if the number is positive and then calculates the area
            rectangle = math_module.area_of_rectangle(length, width)

            # For output layout
            self.answer.delete(1.0, END)
            self.answer.insert(INSERT, "Area of Rectangle = l*w \n => ")
            self.answer.insert(INSERT, str(length))
            self.answer.insert(INSERT, " x ")
            self.answer.insert(INSERT, str(width))
            self.answer.insert(INSERT, " = ")
            self.answer.insert(INSERT, rectangle)
            self.answer.insert(INSERT, " Answer. ")
            self.length.delete(0, END)
            self.width.delete(0, END)
        except ValueError:
            self.length.delete(0, END)
            self.width.delete(0, END)
            self.answer.delete(1.0, END)
            self.answer.insert(INSERT, "Please enter a positive number")

    def triangle_area(self):
        try:
            h = float(self.side1.get())
            b = float(self.side2.get())

            # Uses math_module file to check if the number is positive and then calculates the area
            triangle = math_module.area_of_triangle(h, b)

            # For output layout
            self.answer.delete(1.0, END)
            self.answer.insert(INSERT, "Area of Triangle = (h*b)/2 \n => ")
            self.answer.insert(INSERT, str(h))
            self.answer.insert(INSERT, " x ")
            self.answer.insert(INSERT, str(b))
            self.answer.insert(INSERT, " / ")
            self.answer.insert(INSERT, "2")
            self.answer.insert(INSERT, " = ")
            self.answer.insert(INSERT, triangle)
            self.answer.insert(INSERT, " Answer. ")
            self.side1.delete(0, END)
            self.side2.delete(0, END)
        except ValueError:
            self.side1.delete(0, END)
            self.side2.delete(0, END)
            self.answer.delete(1.0, END)
            self.answer.insert(INSERT, "Please enter a positive number")

    # This function is used for deleting/erasing the text area output
    def fresh(self):
        self.answer.delete(1.0, END)
