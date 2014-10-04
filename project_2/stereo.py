"""Project 2: Stereo vision.

In this project, you'll extract dense 3D information from stereo image pairs.
"""

import cv2
import math
import numpy


def rectify_pair(image_left, image_right, viz=False):
    """Computes the pair's fundamental matrix and rectifying homographies.

    Arguments:
      image_left, image_right: 3-channel images making up a stereo pair.

    Returns:
      F: the fundamental matrix relating epipolar geometry between the pair.
      H_left, H_right: homographies that warp the left and right image so
        their epipolar lines are corresponding rows.
    """
    pass


def disparity_map(image_left, image_right):
    """Compute the disparity images for image_left and image_right.

    Arguments:
      image_left, image_right: rectified stereo image pair.

    Returns:
      an single-channel image containing disparities in pixels,
        with respect to image_left's input pixels.
    """
    pass


def point_cloud(disparity_image, image_left, focal_length):
    """Create a point cloud from a disparity image and a focal length.

    Arguments:
      disparity_image: disparities in pixels.
      image_left: BGR-format left stereo image, to color the points.
      focal_length: the focal length of the stereo camera, in pixels.

    Returns:
      A string containing a PLY point cloud of the 3D locations of the
        pixels, with colors sampled from left_image. You may filter low-
        disparity pixels or noise pixels if you choose.
    """
    pass

def find_fundamental_mat(image_a, image_b):
    sift = cv2.SIFT()
    # detect feature points in each image
    kp_a, des_a = sift.detectAndCompute(image_a, None)
    kp_b, des_b = sift.detectAndCompute(image_b, None)

    # Match feature points together
    FLANN_INDEX_KDTREE = 0
    index_params = dict(algorithm=FLANN_INDEX_KDTREE, trees=5)
    search_params = dict(checks=50)
    flann = cv2.FlannBasedMatcher(index_params, search_params)
    matches = flann.knnMatch(des_b, des_a, k=2)

    # Filter out outliers
    filter_fn = lambda (m, n): m.distance < 0.7 * n.distance
    matches = filter(filter_fn, matches)

    image_a_points = np.float32(
        [kp_a[m.trainIdx].pt for (m, _) in matches]).reshape(-1, 1, 2)
    image_b_points = np.float32(
        [kp_b[m.queryIdx].pt for (m, _) in matches]).reshape(-1, 1, 2)
    
    # find fundamental mat    
    retval, mask = cv2.findFundamentalMat(image_a_points, image_b_points)
    
    
