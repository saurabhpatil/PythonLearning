import turtle
import re
import time

#todo: drawing robotic turtle
plant_colormap = ["#A1C846", "#8FBB48", "#7FAD4A", "#719F4A", "#659249", "#5A8447", "#507745", "#466941", "#3E5B3C"]

def apply_replacement_rules(s, rules, n):
    def replacement(s):
        result = ""
        for char in s:
            if char in rules:
                result += rules[char]
            else:
                result += char
        return result

    def nth_substitution(s, n):

        if n == 0:
            return s
        else:
            return nth_substitution(replacement(s), n-1)
    return nth_substitution(s, n)

def draw_lindenmayer(linden_turtle, s, moves):
    #pattern = re.compile(r"-?\d+")
    #float value pattern from: http://docs.python.org/2/library/re.html#simulating-scanf
    pattern = re.compile(r"[-+]?(\d+(\.\d*)?|\.\d+)([eE][-+]?\d+)?")
    x_stack = []
    y_stack = []
    heading_stack = []
    size_stack = []

    s_pos = 0
    while s_pos < len(s):
        cmd_string = moves[ s[s_pos] ]

        while len(cmd_string) > 0:
            cmd = cmd_string[0]
            next_cmd_start_pos = 1

            if cmd == 'f':
                match = pattern.match(cmd_string[1:])

                if match:
                    next_cmd_start_pos = 1 + match.end()

                    linden_turtle.forward( float( match.group() ) )
                else:
                    linden_turtle.forward(5)

            elif cmd == 'l':
                match = pattern.match(cmd_string[1:])

                if match:
                    next_cmd_start_pos = 1 + match.end()

                    linden_turtle.left( float( match.group() ) )
                else:
                    linden_turtle.left(90)

            elif cmd == 'r':
                match = pattern.match(cmd_string[1:])

                if match:
                    next_cmd_start_pos = 1 + match.end()

                    linden_turtle.right( float( match.group() ) )
                else:
                    linden_turtle.right(90)
            elif cmd == 's':
                match = pattern.match(cmd_string[1:])

                if match:
                    next_cmd_start_pos = 1 + match.end()

                    linden_turtle.pensize( max( linden_turtle.pensize() + float( match.group() ), 1) )
                    linden_turtle.color( plant_colormap[ int( linden_turtle.pensize() ) - 1] )
                else:
                    linden_turtle.pensize( linden_turtle.pensize() )               
            elif cmd == 'p':
                linden_turtle.penup()
                linden_turtle.setpos( x_stack.pop(), y_stack.pop() )
                linden_turtle.setheading( heading_stack.pop() )
                linden_turtle.pensize( size_stack.pop() )
                linden_turtle.pendown()
            elif cmd == 'a':
                x_stack.append( linden_turtle.xcor() )
                y_stack.append( linden_turtle.ycor() )
                heading_stack.append( linden_turtle.heading() )
                size_stack.append( linden_turtle.pensize() )

            cmd_string = cmd_string[next_cmd_start_pos:]        
        s_pos += 1

def draw_art():
    print ("drawing started at: " + time.ctime()) 
    window = turtle.Screen()
    window.bgcolor("#737762")

    window.tracer(512, 0) #speed up drawing
    window.colormode(255)

    linden = turtle.Turtle()
    linden.shape("classic")

    #fass curve
    fass_replacement_rules = { 'A':'A+B++B-A--AA-B+', 'B':'-A+BB++B+A--A-B' }
    fass_moves = { 'A':'f8', 'B':'f8', '+':'r60', '-':'l60' }

    linden_string = apply_replacement_rules("A", fass_replacement_rules, 5)
    linden.penup()
    linden.setpos(300, 400)
    linden.pendown()
    linden.hideturtle()
    linden.color( "orange" )    
    draw_lindenmayer(linden, linden_string, fass_moves)

    #plant
    plant_replacement_rules = { 'X':'F-[[X]+X]+F[+FX]-X', 'F':'FF'}
    plant_moves = { 'X':"", 'F':"f1.5", '+':"r25", '-':"l25", '[':"as-1", ']':"p", }

    linden.penup()
    linden.setpos(-450, -450)
    linden.pendown()
    linden.right(305)

    linden.pensize(9)
    linden.color( plant_colormap[linden.pensize() - 1] )

    linden_string = apply_replacement_rules("X", plant_replacement_rules, 8)
    #print linden_string
    linden.hideturtle()     
    draw_lindenmayer(linden, linden_string, plant_moves)

    print ("done drawing at: " + time.ctime())

    window.exitonclick()

draw_art()
