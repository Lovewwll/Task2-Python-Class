import matplotlib.pyplot as plt


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def translate(self, dx, dy):
        self.x += dx
        self.y += dy

def read_coordinates_from_file(filename):
    points = []
    with open(filename, 'r') as file:
        # Skip the header line
        next(file)
        for line in file:
            x, y = map(float, line.strip().split(','))  # Split by comma
            points.append(Point(x, y))
    return points


def plot_points(original_points, translated_points, original_color='blue', translated_color='red'):
    x_values_original = [point.x for point in original_points]
    y_values_original = [point.y for point in original_points]

    x_values_translated = [point.x for point in translated_points]
    y_values_translated = [point.y for point in translated_points]

    plt.scatter(x_values_original, y_values_original, color=original_color, label='Original')
    plt.scatter(x_values_translated, y_values_translated, color=translated_color, label='Translated')

    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Combined Scatter Plot of Points')
    plt.grid(True)
    plt.legend()
    plt.show()


if __name__ == "__main__":
    filename = "data.csv"
    original_points = read_coordinates_from_file(filename)

    # Make a copy of original points for translation
    translated_points = [Point(point.x, point.y) for point in original_points]

    # Move the points
    dx = 5
    dy = 5
    for point in translated_points:
        point.translate(dx, dy)

    # Plot both original and translated points on the same graph
    plot_points(original_points, translated_points)

