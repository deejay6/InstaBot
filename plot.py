import matplotlib.pyplot as plt
import csv
latitude = []
longitude = []
name = []
location = []
s = []

points_with_annotation = []
fig = plt.figure()
ax = fig.add_subplot(111)
# Reading csv file and getting data

with open('image.csv') as out:
    plots = csv.reader(out, delimiter=';')
    for row in plots:
        s.append(row)
    for i in range(1, len(s)):
        latitude.append(float(s[i][2]))
        longitude.append(float(s[i][1]))
        name.append(s[i][3])
        location.append(s[i][4])
for i, j, k , l in zip(latitude, longitude, name, location):
    point = plt.scatter(i, j)
    ax.annotate('%s' % k, xy=(i, j), xytext=(2, 2), textcoords='offset points')
    annotation1 = ax.annotate('%s' % l,  xy=(i, j), xytext=(0, 15), textcoords='offset points', bbox=dict(boxstyle="round", facecolor="w",
                                                                                                         edgecolor="0.5", alpha=0.9))
    annotation1.set_visible(False)
    points_with_annotation.append([point, annotation1])
plt.xlabel('Latitude')
plt.ylabel('Longitude')
plt.title('Showing Natural Calamites At Different Regions')


# Function To provide hover effect on graph

def on_move(event):
    visibility_changed = False
    for point, annotation1 in points_with_annotation:
        should_be_visible = (point.contains(event)[0] == True)

        if should_be_visible != annotation1.get_visible():
            visibility_changed = True
            annotation1.set_visible(should_be_visible)

    if visibility_changed:
        plt.draw()

on_move_id = fig.canvas.mpl_connect('motion_notify_event', on_move)

plt.show()