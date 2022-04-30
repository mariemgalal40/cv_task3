import cv2 
import timeit

from numpy import ndarray
from feature_matching import SSD, NCC, np

# def getMatchingTable(matrix: ndarray):
#     minvaluesIndices = np.argmin(matrix, axis=1) # row-wise
#     feature_indices = [i for i in range(matrix.shape[1])]
#     matching_table = list(zip(feature_indices, minvaluesIndices))
#     print(matching_table)
#     return matching_table

# def getMatchingTable_ncc(matrix: ndarray):
#     matrix = abs(matrix)
#     maxvaluesIndices = np.argmax(matrix, axis=1) # row-wise
#     feature_indices = [i for i in range(matrix.shape[1])]
#     matching_table = list(zip(feature_indices, maxvaluesIndices))
#     print(matching_table)
#     return matching_table
    

# ------------  Feature matching -------------
# feature vector 1
desc1 = [ [13,2,3,4,5,6,7,8,9,90],
          [14,2,32,4,5,21,70,8,9,0],
          [51,20,3,24,5,6,754,8,9,110],
          [1,2,32,42,50,6,7,86,9,60],
          [91,2,33,24,5,6,7,83,9,14],
          [10,25,43,40,5,6,7,8,9,104],
          [1,2,36,74,5,6,78,80,9,1] ]

# feature vector 2
desc2 = [ [1,2,3,4,5,6,7,8,9,10],
          [14,2,32,4,5,21,70,8,9,0],
          [51,20,3,24,5,6,754,8,9,110],
          [1,2,32,42,50,6,7,86,9,60],
          [91,2,33,24,5,6,7,83,9,14],
          [10,25,43,40,5,6,7,8,9,104],
          [1,2,36,74,5,6,78,80,9,1] ]

desc1 = np.array(desc1)
desc2 = np.array(desc2)

ssd = SSD(desc1, desc2)
ssd.match()
duration = timeit.Timer(ssd.match).timeit(number = 10)
print("Run time of ssd.match function is", duration/10)
matches_ssd = ssd.match()
# getMatchingTable(np.array(matches_ssd))
print("matches_ssd:", matches_ssd)

ncc = NCC(desc1, desc2)
matches_ncc = ncc.match()
duration = timeit.Timer(ncc.match).timeit(number = 10)
print("Run time of ncc.match function is", duration/10)
# getMatchingTable_ncc(np.array(matches_ncc))
print("matches_ncc:", matches_ncc)


print(matches_ssd[6])
print(matches_ncc[6])


# ------------  Template matching -------------
img1_path = "./images/white_cat2.jpg"

img = cv2.imread(img1_path, cv2.IMREAD_GRAYSCALE)
template = img[66:116,89:139]
cv2.imshow("img", img)
cv2.imshow("template", template)
cv2.waitKey(0)
cv2.imshow("ssd", ssd.match_image(img, template))
cv2.waitKey(0)
cv2.imshow("ssd_thresholded", ssd.ssd_thresholded)
cv2.waitKey(0)


cv2.imshow("ncc", ncc.match_image(img, template))
cv2.imshow("ncc_thresholded", ncc.ncc_thresholded)
cv2.waitKey(0)