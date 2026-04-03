import numpy as np
from matplotlib import pyplot as plt


def imshow(image: np.ndarray):
    """Show the image with matplotlib."""
    fig = plt.figure(frameon=False)

    # Add an axes that fills the whole figure
    ax = plt.Axes(fig, [0, 0, 1, 1])
    ax.set_axis_off()
    fig.add_axes(ax)

    ax.imshow(image, cmap='gray')
    plt.show()