import numpy as np



class NCC():     
    
    def __init__(self, desc1: np.ndarray, desc2: np.ndarray) -> None:
        self.__desc1 = desc1
        self.__desc2 = desc2

        # 2d list of all similarities between discriptors
        self.matchingMatrix = []

        # list of tuples contains the closest matched descriptors
        self.matching_table = []

        if self.__validate_descriptors() == False:
            raise TypeError("Inconvenient shape")
        

    def __validate_descriptors(self):
        # number of cols in each array must be equal
        return self.__desc1.shape[1] == self.__desc2.shape[1]
    
    def __getMatchingTable_ncc(self):
        """ Get a list of all index-pair matched features
        
            return: list of tuples of matched features
            ex:
            [(0,1), (1,5), (2,4),..]
            1st element in each tuple represents index of descriptor in descriptors1
            2nd element in each tuple represents index of the closest descriptor in descriptors2
        """
        matrix = np.array(self.matchingMatrix)
        matrix = abs(matrix)

        maxvaluesIndices = np.argmax(matrix, axis=1) # row-wise
        feature_indices = [i for i in range(matrix.shape[1])]
        self.matching_table = list(zip(feature_indices, maxvaluesIndices))
        return self.matching_table


    def match(self):

        
        for i in range(self.__desc1.shape[0]):
            desc1i_mean = np.mean(self.__desc1[i])
            desc2_means = np.mean(self.__desc2, axis=1)

            zero_mean_desc1i = self.__desc1[i]- desc1i_mean
            zero_mean_sesc2 = (self.__desc2.T - desc2_means).T

            cross_correlations = np.sum(zero_mean_sesc2 * zero_mean_desc1i, axis=1) # y-axis (rows)

            variance1 = np.sum(zero_mean_desc1i**2)
            variance2 = np.sum(zero_mean_sesc2**2, axis=1) # y-axis (rows)

            ncc = cross_correlations/( (variance1 * variance2)**0.5 )

            self.matchingMatrix.append(ncc)

        return self.__getMatchingTable_ncc()

    def match_image(self, img, temp, threshold=0.5): # temp is the mask
    
        # get dimensions of mask
        mask_rows = temp.shape[0]
        mask_cols = temp.shape[1]

        ncc_image_rows = img.shape[0]
        ncc_image_cols = img.shape[1]

        ncc = np.ones((ncc_image_rows,ncc_image_cols))
        
        print("performing ncc computations...")
        
        temp_mean = np.mean(temp)

        for i in range(ncc_image_rows):     # height
            for j in range(ncc_image_cols): # width
                img_masked = img[i:i+mask_rows, j:j+mask_cols]
                img_masked_mean = np.mean(img_masked)
                if img_masked.shape != temp.shape:
                    break

                zero_mean_img = (img_masked-img_masked_mean)
                zero_mean_temp = (temp-temp_mean)
                cross_correlation = sum(sum(zero_mean_img * zero_mean_temp))

                ncc[i][j] = cross_correlation/( sum(sum(zero_mean_img**2)) * sum(sum(zero_mean_temp**2)) )**0.5
        self.ncc_thresholded = (ncc > threshold) * 1.0
        return ncc


class SSD():   
    def __init__(self, desc1: np.ndarray, desc2: np.ndarray) -> None:
        self.__desc1 = desc1
        self.__desc2 = desc2
        # 2d list of all distances between discriptors 
        self.matchingMatrix = []

        # list of tuples contains the closest matched descriptors
        self.matching_table = []

        if self.__validate_descriptors() == False:
            raise TypeError("Inconvenient shape")


    def __validate_descriptors(self):
        # number of cols in each array must be equal
        return self.__desc1.shape[1] == self.__desc2.shape[1]

    def __getMatchingTable(self):
        """ Get a list of all index-pair matched features
        
            return: list of tuples of matched features
            ex:
            [(0,1), (1,5), (2,4),..]
            1st element in each tuple represents index of descriptor in descriptors1
            2nd element in each tuple represents index of the closest descriptor in descriptors2
        """

        # 2d list of all distances between discriptors
        matchingMatrix = np.array(self.matchingMatrix) 

        minValuesIndices = np.argmin(matchingMatrix, axis=1) # row-wise

        feature_indices = [i for i in range(matchingMatrix.shape[1])]

        self.matching_table = list(zip(feature_indices, minValuesIndices))
        return self.matching_table

    def match(self):
        
        for i in range(self.__desc1.shape[0]):
            diff = self.__desc2 - self.__desc1[i]
            sumOfSquaredDiff = np.sum( (diff*diff),axis=1).tolist()
            self.matchingMatrix.append(sumOfSquaredDiff)

        return self.__getMatchingTable()

    def match_image(self, img, temp, threshold=0.7): 
        
        # get dimensions of mask
        mask_rows = temp.shape[0]
        mask_cols = temp.shape[1]

        ssd_image_rows = img.shape[0]
        ssd_image_cols = img.shape[1]

        ssd = np.ones((ssd_image_rows,ssd_image_cols))

    
        print("performing ssd computations...")
        
        for i in range(ssd_image_rows):     # height
            for j in range(ssd_image_cols): # width
                img_masked = img[i:i+mask_rows, j:j+mask_cols]

                if img_masked.shape != temp.shape:
                    break
                diff = img_masked - temp
                
                ssd[i][j] = sum((sum(diff * diff)))
                
        self.ssd_normalized = ssd/np.amax(ssd) # normalize it
        self.ssd_negative = 1-ssd**0.5
        self.ssd_thresholded = (ssd < threshold) * 1.0
        
        return ssd