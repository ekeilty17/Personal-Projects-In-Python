import cv2
import numpy as np
import cmath

class ComplexFunction(object):

    colors = {
            'red':          (0, 0, 255),
            'orange':       (0, 128, 255),
            'yellow':       (0, 255, 255),
            'green':        (0, 255, 0),
            'cyan':         (255, 255, 0),
            'blue':         (255, 128, 0),
            'dark blue':    (128, 0, 0),
            'purple':       (255, 0, 128),
            'magenta':      (255, 0, 255),
            'pink':         (128, 0, 255),
            'white':        (255, 255, 255),
            'light grey':   (224, 224, 224),
            'grey':         (128, 128, 128),
            'black':        (0, 0, 0)
        }
    color_names = ['red', 'orange', 'yellow', 'green', 'cyan', 'blue', 'purple', 'magenta', 'pink']

    def __init__(self, f, X=512, Y=512, x_scale=(-10,10), y_scale=(-10,10), grid=True):
        
        self.drawing = False
        self.b = 4          # boarder
        self.c = 0          # color index
        
        self.X, self.Y = X, Y
        self.x_scale = x_scale
        self.y_scale = y_scale
        self.f = f
        
        # Creating input plane image
        cv2.namedWindow('Input Plane')
        cv2.moveWindow('Input Plane', 50, 100);
        cv2.setMouseCallback('Input Plane', self.draw_input)
        self.input = np.zeros((self.Y, self.X, 3), np.uint8)

        # Creating output plane image
        cv2.namedWindow('Output Plane')
        cv2.setMouseCallback('Output Plane', self.place_holder)
        cv2.moveWindow('Output Plane', 50+self.X+10, 100);
        self.output = np.zeros((self.Y, self.X, 3), np.uint8) 
        
        self.reset_display(grid)

    def reset_display(self, grid=True):
        
        # Input Plane
        self.input = np.zeros((self.Y, self.X, 3), np.uint8)
        # Grid lines
        if grid:
            #   Verticle
            for i in range(self.x_scale[0], self.x_scale[1]):
                x_pos = i*self.X//(self.x_scale[1] - self.x_scale[0]) + self.X//2
                cv2.line(self.input, (x_pos, 0), (x_pos, self.Y), self.colors['dark blue'], 1)
            #   Horizontal
            for i in range(self.y_scale[0], self.y_scale[1]):
                y_pos = i*self.Y//(self.y_scale[1] - self.y_scale[0]) + self.Y//2
                cv2.line(self.input, (0, y_pos), (self.X, y_pos), self.colors['dark blue'], 1)
        # Axes
        cv2.line(self.input, (self.X//2, 0), (self.X//2, self.Y), self.colors['light grey'], 3)
        cv2.line(self.input, (0, self.Y//2), (self.X, self.Y//2), self.colors['light grey'], 3)
        
        # Output Plane
        self.output = np.zeros((self.Y, self.X, 3), np.uint8)
        # Grid lines
        if grid:
            # output plane
            #   Verticle
            for i in range(self.x_scale[0], self.x_scale[1]):
                x_pos = i*self.X//(self.x_scale[1] - self.x_scale[0]) + self.X//2
                cv2.line(self.output, (x_pos, 0), (x_pos, self.Y), self.colors['grey'], 1)
            #   Horizontal
            for i in range(self.y_scale[0], self.y_scale[1]):
                y_pos = i*self.Y//(self.y_scale[1] - self.y_scale[0]) + self.Y//2
                cv2.line(self.output, (0, y_pos), (self.X, y_pos), self.colors['grey'], 1)
            
            # tranformed from input plane
            #   Vertical
            for i in range(self.x_scale[0], self.x_scale[1]):
                x_pos = i*self.X//(self.x_scale[1] - self.x_scale[0]) + self.X//2
                y_pos = np.linspace(0, self.Y, 50)
                
                points = np.array( [self.complex_to_cv( self.f(self.cv_to_complex(x_pos, y)) ) for y in y_pos] )
                points = np.array( [[p[0], p[1]] for p in points] )
                cv2.polylines(self.output, np.int32([points]), True, self.colors['dark blue'])
            #   Horizontal
            for i in range(self.y_scale[0], self.y_scale[1]):
                x_pos = np.linspace(0, self.X, 50)
                y_pos = i*self.Y//(self.y_scale[1] - self.y_scale[0]) + self.Y//2
                
                points = np.array( [self.complex_to_cv( self.f(self.cv_to_complex(x, y_pos)) ) for x in x_pos] )
                points = np.array( [[p[0], p[1]] for p in points] )
                cv2.polylines(self.output, np.int32([points]), True, self.colors['dark blue'])
                
        
        # Axes
        cv2.line(self.output, (self.X//2, 0), (self.X//2, self.Y), self.colors['light grey'], 3)
        cv2.line(self.output, (0, self.Y//2), (self.X, self.Y//2), self.colors['light grey'], 3)

    def cv_to_complex(self, x, y):
        # x, y = 0, 0 is in the top left of the display
        r = (x - self.X//2) / (self.x_scale[1] - self.x_scale[0])
        i = (- y + self.Y//2) / (self.y_scale[1] - self.y_scale[0])
        return complex(r, i)

    def complex_to_cv(self, z):
        # x, y = 0, 0 is in the top left of the display
        r = z.real * (self.x_scale[1] - self.x_scale[0])
        i = z.imag * (self.y_scale[1] - self.y_scale[0])
        return (int(r) + self.X//2, - int(i) + self.Y//2)
    
    def draw_input(self, event, x, y, flags, param):
        if event == cv2.EVENT_LBUTTONDOWN:
            if self.b < x < self.X - self.b:
                self.drawing = True

        elif event == cv2.EVENT_MOUSEMOVE:
            if self.drawing:
                # Drawing input plane
                if self.b < x < self.X - self.b:
                    cv2.circle(self.input, (x,y), 2, self.colors[self.color_names[self.c]], -1)

                # Drawing output plane
                u, v = self.complex_to_cv( self.f(self.cv_to_complex(x, y)) )
                if self.b < u < self.X - self.b:
                    cv2.circle(self.output, (u,v), 2, self.colors[self.color_names[self.c]], -1)

        elif event == cv2.EVENT_LBUTTONUP:
            self.drawing = False
            self.c += 1
            self.c %= len(self.color_names)
    
    def place_holder(self, event, x, y, flags, param):
        pass
    
    def display(self):
        
        while True:
            cv2.imshow('Input Plane', self.input)
            cv2.imshow('Output Plane', self.output)
            k = cv2.waitKey(1) & 0xFF
            if k == ord('c'):
                self.reset_display()
            elif k == ord('q') or k == 27:
                # I think k=27 is the esc key
                break

        cv2.destroyAllWindows()

def f(z):
    return z**2

if __name__ == "__main__":
    #F = ComplexFunction(f, x_scale=(-25, 25), y_scale=(-25, 25))
    F = ComplexFunction(f)
    F.display()
