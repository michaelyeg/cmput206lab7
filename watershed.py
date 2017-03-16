import numpy as np


def getRegionalMinima(img):
    h, w = img.shape
    out = np.zeros(img.shape, np.int32)
    for i in range(h):
        for j in range(w):
            neighborPixel = []
            if 1 <= i < h - 1 and 1 <= j < w-1:
                # Create neighboring pixels list
                neighborPixel.append(img[i-1][j-1])
                neighborPixel.append(img[i-1][j])
                neighborPixel.append(img[i-1][j+1])
                neighborPixel.append(img[i][j-1])
                neighborPixel.append(img[i][j+1])
                neighborPixel.append(img[i+1][j-1])
                neighborPixel.append(img[i+1][j])
                neighborPixel.append(img[i+1][j+1])
                if img[i][j] < min(neighborPixel):
                    out[i][j] = 1
            # Left border
            elif 1 <= i < h - 1 and j == 0:
                neighborPixel.append(img[i-1][j])
                neighborPixel.append(img[i-1][j+1])
                neighborPixel.append(img[i][j+1])
                neighborPixel.append(img[i+1][j])
                neighborPixel.append(img[i+1][j+1])
                if img[i][j] < min(neighborPixel):
                    out[i][j] = 1
            # Right border
            elif 1 <= i < h - 1 and j == w - 1:
                neighborPixel.append(img[i-1][j-1])
                neighborPixel.append(img[i-1][j])
                neighborPixel.append(img[i][j-1])
                neighborPixel.append(img[i+1][j-1])
                neighborPixel.append(img[i+1][j])
                if img[i][j] < min(neighborPixel):
                    out[i][j] = 1
            # Top border
            elif i == 0 and 1 <= j < w - 1:
                neighborPixel.append(img[i][j-1])
                neighborPixel.append(img[i][j+1])
                neighborPixel.append(img[i+1][j-1])
                neighborPixel.append(img[i+1][j])
                neighborPixel.append(img[i+1][j+1])
                if img[i][j] < min(neighborPixel):
                    out[i][j] = 1
            # Bottom border
            elif i == h-1 and 1 <= j < w - 1:
                neighborPixel.append(img[i-1][j-1])
                neighborPixel.append(img[i-1][j])
                neighborPixel.append(img[i-1][j+1])
                neighborPixel.append(img[i][j-1])
                neighborPixel.append(img[i][j+1])
                if img[i][j] < min(neighborPixel):
                    out[i][j] = 1
            # Top left corner
            elif i == 0 and j == 0:
                neighborPixel.append(img[i][j+1])
                neighborPixel.append(img[i+1][j])
                neighborPixel.append(img[i+1][j+1])
                if img[i][j] < min(neighborPixel):
                    out[i][j] = 1
            # Top right corner
            elif i == 0 and j == w-1:
                neighborPixel.append(img[i][j-1])
                neighborPixel.append(img[i+1][j-1])
                neighborPixel.append(img[i+1][j])
                if img[i][j] < min(neighborPixel):
                    out[i][j] = 1
            # Bottom left corner
            elif i == h-1 and j == 0:
                neighborPixel.append(img[i-1][j])
                neighborPixel.append(img[i-1][j+1])
                neighborPixel.append(img[i][j+1])
                if img[i][j] < min(neighborPixel):
                    out[i][j] = 1
            # Bottom right corner
            elif i == h-1 and j == w-1:
                neighborPixel.append(img[i-1][j-1])
                neighborPixel.append(img[i-1][j])
                neighborPixel.append(img[i][j-1])
                if img[i][j] < min(neighborPixel):
                    out[i][j] = 1
    val = 1
    for m in range(h):
        for n in range(w):
            if out[m][n] == 1:
                out[m][n] = val
                val += 1

    return out


def iterativeMinFollowing(img, markers):
    # add your code here
    pass


