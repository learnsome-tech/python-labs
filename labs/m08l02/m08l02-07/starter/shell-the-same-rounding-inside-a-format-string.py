# Shell session from the video, as a file you can run.
# Each line below was typed at the >>> prompt; the commented lines are
# what Python answered. Run it with:  python3 -i thisfile.py

x = 2.876543
y = 16.3591
'x long: {:.5f}, x short: {:.3f}, y: {:.2f}.'.format(x, x, y)
#   'x long: 2.87654, x short: 2.877, y: 16.36.'
'long: {x:.5f}, short: {x:.3f}.'.format(**locals())
#   'long: 2.87654, short: 2.877.'
'longer: {0:.5f}, shorter: {0:.3f}.'.format(x)
#   'longer: 2.87654, shorter: 2.877.'
