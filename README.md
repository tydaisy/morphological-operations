# morphological-operations
This repository provides an overview of classic morphological operations, including erosion and dilation. Each operation is accompanied by a corresponding example to demonstrate its effects.

![erosion.jpg](assets/images/erosion.jpg)
Image by <a href="https://pixabay.com/users/nginnhong-22953211/?utm_source=link-attribution&utm_medium=referral&utm_campaign=image&utm_content=9215914">Aaron Ng</a> from <a href="https://pixabay.com//?utm_source=link-attribution&utm_medium=referral&utm_campaign=image&utm_content=9215914">Pixabay</a>

## What is structural element?
Structural element in image processing is also called kernel. It is essentially a small matrix of numbers used as a sliding window to scan the image. It scans the iamge and determines how a pixel should be updated based on its neighbors. The kernel is usually a small, square matrix with odd dimensions (e.g., $3 \times 3$, $5 \times 5$, or $7 \times 7$). This ensures there is a clear "center pixel" that acts as the anchor point. The dimensions of the kernel directly define the neighborhood of influence. The larger the kernel, the more neighbors are consulted to decide the fate of the center pixel.\
Mathematically, an erosion and dilation kernel is a matrix of ones. For a standard $3 \times 3$ kernel, it looks like this:
```math
K = \begin{bmatrix} 
1 & 1 & 1 \\ 
1 & 1 & 1 \\ 
1 & 1 & 1 
\end{bmatrix}
```

## What is morphological operations?
Morphology is a broad set of image processing operations that process images based on shapes. Morphological operations apply a structuring element to an input image, creating an output image of the same size. In a morphological operation, the value of each pixel in the output image is based on a comparison of the corresponding pixel in the input image with its neighbor.

## What is erosion?
Erosion removes pixels on object boundaries. It is a "shrinker". \
**The Equation working with binary images:**\
```math
A \ominus B = \{ z \mid (B)_z \subseteq A \}
```
* $z$: The pixel coordinate being evaluated.
* $(B)_z$: The kernel $B$ shifted so its origin is at coordinate $z$.
* $\subseteq A$: This is the "subset" symbol. It means the shifted kernel must be completely contained within the foreground pixels of image $A$.

The center pixel only survives if the kernel is "fully submerged" in white pixels. If any part of the kernel hangs over the edge into the black background, the center pixel is deleted (set to 0).

**The Equation working with grayscale images:**\
```math
(f \ominus b)(x) = \inf_{y \in B} \{ f(x + y) - b(y) \}
```
Erosion is a Local Minimum. Essentially, it picks the darkest pixel in the neighborhood.

## What is dilation?
Dilation adds pixels to the boundaries of objects in an image. It is an "expander".
Dilation is mathematically defined as the Minkowski Addition of the image set and the kernel set.\
**The Equation working with binary images:**\
```math
A \oplus B = \{ z \mid (\hat{B})_z \cap A \neq \emptyset \}
```
* $A$: The input image.
* $B$: The structuring element (kernel).
* $(\hat{B})_z$: This represents the reflection of the kernel $B$ about its origin, shifted to location $z$.
* $\cap A \neq \emptyset$: This means the intersection of the shifted kernel and the image is not empty.

As the kernel moves across the image, if at least one pixel of the kernel overlaps with a foreground pixel of the image, the pixel at the current center position ($z$) is set to 1 (white). This causes the boundaries to grow.

**The Equation working with grayscale images:**\
```math
(f \oplus b)(x) = \sup_{y \in B} \{ f(x - y) + b(y) \}
```
Dilation is a Local Maximum. Essentially, it picks the brightest pixel in the neighborhood.

## What is opening?
The opening operation erodes an image and then dilates the eroded image, using the same structuring element for both operations.
Morphological opening is useful for removing small objects and thin lines from an image while preserving the shape and size of larger objects in the image. 


## What is closing?
The closing operation dilates an image and then erodes the dilated image, using the same structuring element for both operations.
Morphological closing is useful for filling small holes in an image while preserving the shape and size of large holes and objects in the image.


