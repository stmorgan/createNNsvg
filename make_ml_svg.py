class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

# Points


numberInputs = 4
numberHidden = 5
numberOutputs = 3
circlePitch = 100
circleRadius = 40
circleStrokeColour = 'black'
circleStrokeWidth = '3'
circleFillColour = '#88f'
lineStrokeColour = 'black'
lineStrokeWidth = '2'
inputStart = Point(50, 100)
inputCircleStart = Point(150, 100)
hiddenCircleStart = Point(300, 50)
outputCircleStart = Point(450, 150)
outputEnd = Point(550, 150)


# Preamble


with open("nn.svg", "w") as f:
    f.write('<?xml version="1.0" encoding="UTF-8" ?> \n \
    <svg \
        height="500" width="600" \
        xmlns="http://www.w3.org/2000/svg" version="1.1">')

    # Lines
    for row in range(numberInputs):
        # Lines to input notes
        f.write('<line \
        x1="' + str(inputStart.x) + '" \
        y1="' + str(inputStart.y + row * circlePitch) + '" \
        x2="' + str(inputCircleStart.x) + '" \
        y2="' + str(inputStart.y + row * circlePitch) + '" \
        style="stroke:' + lineStrokeColour + ';\
        stroke-width:' + lineStrokeWidth + '" />\
        ')

    # Lines from input to hidden layer
    for inputRow in range(numberInputs):
        for outputRow in range(numberHidden):
            f.write('<line \
            x1="' + str(inputCircleStart.x) + '" \
            y1="' + str(inputCircleStart.y + inputRow * circlePitch) + '" \
            x2="' + str(hiddenCircleStart.x) + '" \
            y2="' + str(hiddenCircleStart.y + outputRow * circlePitch) + '" \
            style="stroke:' + lineStrokeColour + ';\
            stroke-width:' + lineStrokeWidth + '" />\
            ')

    # Lines from hidden layer to output layer
    for inputRow in range(numberHidden):
        for outputRow in range(numberOutputs):
            f.write('<line \
            x1="' + str(hiddenCircleStart.x) + '" \
            y1="' + str(hiddenCircleStart.y + inputRow * circlePitch) + '" \
            x2="' + str(outputCircleStart.x) + '" \
            y2="' + str(outputCircleStart.y + outputRow * circlePitch) + '" \
            style="stroke:' + lineStrokeColour + ';\
            stroke-width:' + lineStrokeWidth + '" />\
            ')

    # Lines from Output layer
    for row in range(numberOutputs):
        # Lines to input notes
        f.write('<line \
        x1="' + str(outputCircleStart.x) + '" \
        y1="' + str(outputCircleStart.y + row * circlePitch) + '" \
        x2="' + str(outputEnd.x) + '" \
        y2="' + str(outputEnd.y + row * circlePitch) + '" \
        style="stroke:' + lineStrokeColour + ';\
        stroke-width:' + lineStrokeWidth + '" />\
        ')

    # Input Circles
    for row in range(numberInputs):
        f.write("<circle cx='" + str(inputCircleStart.x) + \
        "' cy='" + str(inputCircleStart.y + row*circlePitch) + \
        "' r='" + str(circleRadius) +  \
        "' stroke='" + circleStrokeColour + "' \
        stroke-width='" + str(circleStrokeWidth) + "' \
        fill='" + circleFillColour + "' />")

    # Hidden circles
    for row in range(numberHidden):
        f.write("<circle cx='" + str(hiddenCircleStart.x) + \
        "' cy='" + str(hiddenCircleStart.y + row*circlePitch) + \
        "' r='" + str(circleRadius) +  \
        "' stroke='" + circleStrokeColour + "' \
        stroke-width='" + str(circleStrokeWidth) + "' \
        fill='" + circleFillColour + "' />")

    # Output Circles
    for row in range(numberOutputs):
        f.write("<circle cx='" + str(outputCircleStart.x) + \
        "' cy='" + str(outputCircleStart.y + row*circlePitch) + \
        "' r='" + str(circleRadius) +  \
        "' stroke='" + circleStrokeColour + "' \
        stroke-width='" + str(circleStrokeWidth) + "' \
        fill='" + circleFillColour + "' />")

    f.write("</svg>")
