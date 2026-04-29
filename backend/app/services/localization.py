import cv2
import numpy as np


def apply_localization(image, heatmap):
    # Resize heatmap to match image
    heatmap = cv2.resize(heatmap, (image.shape[1], image.shape[0]))

    # Convert to uint8
    heatmap_uint8 = np.uint8(255 * heatmap)

    # Threshold (focus only strong regions)
    _, thresh = cv2.threshold(heatmap_uint8, 180, 255, cv2.THRESH_BINARY)

    # Find contours
    contours, _ = cv2.findContours(
        thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE
    )

    if contours:
        # Take largest region
        c = max(contours, key=cv2.contourArea)

        # Draw contour
        cv2.drawContours(image, [c], -1, (0, 0, 255), 2)

    return image