# morphological-operations
This repository provides an overview of classic morphological operations, including erosion and dilation. Each operation is accompanied by a corresponding example to demonstrate its effects.

![erosion.jpg](images/erosion.jpg)
Image by <a href="https://pixabay.com/users/nginnhong-22953211/?utm_source=link-attribution&utm_medium=referral&utm_campaign=image&utm_content=9215914">Aaron Ng</a> from <a href="https://pixabay.com//?utm_source=link-attribution&utm_medium=referral&utm_campaign=image&utm_content=9215914">Pixabay</a>

## What is morphological operations
Morphology is a broad set of image processing operations that process images based on shapes. Morphological operations apply a structuring element to an input image, creating an output image of the same size. In a morphological operation, the value of each pixel in the output image is based on a comparison of the corresponding pixel in the input image with its neighbor.

## What is erosion
Erosion removes pixels on object boundaries.

## What is dilation
Dilation adds pixels to the boundaries of objects in an image.

## What is opening
The opening operation erodes an image and then dilates the eroded image, using the same structuring element for both operations.
Morphological opening is useful for removing small objects and thin lines from an image while preserving the shape and size of larger objects in the image. 


# What is closing
The closing operation dilates an image and then erodes the dilated image, using the same structuring element for both operations.
Morphological closing is useful for filling small holes in an image while preserving the shape and size of large holes and objects in the image.


