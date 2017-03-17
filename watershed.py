import numpy as np
import copy


def getRegionalMinima(img):
    h, w = img.shape
    out = np.zeros(img.shape, np.int32)
    for i in range(h):
        for j in range(w):
            # Get the minimal neighbor's location
            loc = findMinNeighborLocation(i, j, img)
            if img[i][j] <= img[loc[0]][loc[1]]:
                out[i][j] = 1
    val = 1
    for m in range(h):
        for n in range(w):
            if out[m][n] == 1:
                out[m][n] = val
                val += 1
    return out


def iterativeMinFollowing(img, markers):
    h, w = img.shape
    label = copy.deepcopy(markers)
    count = h * w
    for m in range(h):
        for n in range(w):
            if label[m][n] != 0:
                count -= 1
    while count > 0:
        for i in range(h):
            for j in range(w):
                if label[i][j] == 0:
                    loc = findMinNeighborLocation(i, j, img)
                    if label[loc[0]][loc[1]] != 0:
                        label[i][j] = label[loc[0]][loc[1]]
                        count -= 1
    return label


def findMinNeighborLocation(i, j, img):
    h, w = img.shape
    neighborPixel = {}
    if 0 < i < h - 1 and 0 < j < w - 1:
        # Create neighboring pixels list
        neighborPixel[(i-1, j-1)] = img[i - 1][j - 1]
        neighborPixel[(i-1, j)] = img[i - 1][j]
        neighborPixel[(i-1, j+1)] = img[i - 1][j + 1]
        neighborPixel[(i, j-1)] = img[i][j - 1]
        neighborPixel[(i, j + 1)] = img[i][j + 1]
        neighborPixel[(i+1, j-1)] = img[i + 1][j - 1]
        neighborPixel[(i+1, j)] = img[i + 1][j]
        neighborPixel[(i+1, j+1)] = img[i + 1][j + 1]
    # Left border
    elif 0 < i < h - 1 and j == 0:
        neighborPixel[(i - 1, j)] = img[i - 1][j]
        neighborPixel[(i - 1, j + 1)] = img[i - 1][j+1]
        neighborPixel[(i, j + 1)] = img[i][j + 1]
        neighborPixel[(i + 1, j)] = img[i + 1][j]
        neighborPixel[(i + 1, j + 1)] = img[i + 1][j + 1]
    # Right border
    elif 0 < i < h - 1 and j == w - 1:
        neighborPixel[(i - 1, j - 1)] = img[i - 1][j - 1]
        neighborPixel[(i - 1, j)] = img[i - 1][j]
        neighborPixel[(i, j - 1)] = img[i][j - 1]
        neighborPixel[(i + 1, j - 1)] = img[i + 1][j - 1]
        neighborPixel[(i + 1, j)] = img[i + 1][j]
    # Top border
    elif i == 0 and 1 <= j < w - 1:
        neighborPixel[(i, j - 1)] = img[i][j - 1]
        neighborPixel[(i, j + 1)] = img[i][j + 1]
        neighborPixel[(i + 1, j - 1)] = img[i + 1][j - 1]
        neighborPixel[(i + 1, j)] = img[i + 1][j]
        neighborPixel[(i + 1, j + 1)] = img[i + 1][j + 1]
    # Bottom border
    elif i == h - 1 and 1 <= j < w - 1:
        neighborPixel[(i - 1, j - 1)] = img[i - 1][j - 1]
        neighborPixel[(i - 1, j)] = img[i - 1][j]
        neighborPixel[(i - 1, j + 1)] = img[i - 1][j + 1]
        neighborPixel[(i, j - 1)] = img[i][j - 1]
        neighborPixel[(i, j + 1)] = img[i][j + 1]
    # Top left corner
    elif i == 0 and j == 0:
        neighborPixel[(i, j + 1)] = img[i][j + 1]
        neighborPixel[(i + 1, j)] = img[i + 1][j]
        neighborPixel[(i + 1, j + 1)] = img[i + 1][j + 1]
    # Top right corner
    elif i == 0 and j == w - 1:
        neighborPixel[(i, j - 1)] = img[i][j - 1]
        neighborPixel[(i + 1, j - 1)] = img[i + 1][j - 1]
        neighborPixel[(i + 1, j)] = img[i + 1][j]
    # Bottom left corner
    elif i == h - 1 and j == 0:
        neighborPixel[(i - 1, j)] = img[i - 1][j]
        neighborPixel[(i - 1, j + 1)] = img[i - 1][j + 1]
        neighborPixel[(i, j + 1)] = img[i][j + 1]
    # Bottom right corner
    elif i == h - 1 and j == w - 1:
        neighborPixel[(i - 1, j - 1)] = img[i - 1][j - 1]
        neighborPixel[(i - 1, j)] = img[i - 1][j]
        neighborPixel[(i, j - 1)] = img[i][j - 1]

    MIN = min(neighborPixel.values())
    for k in neighborPixel:
        if neighborPixel[k] == MIN:
            #neighborPixel.clear()
            return k