from FileHandler import FileReader
from collections import Counter
import math
class KNN:
    def __init__(self, filename,InputtedTime):
        self.InputtedTime = InputtedTime
        self.filename = filename
        self.data = FileReader(self.filename)
        self.time = ""
        
    def knn(self,data, query, k, distance_fn, choice_fn):
        neighbor_distances_and_indices = []
        for index, example in enumerate(data):
            distance = distance_fn(example[:-1], query)
            neighbor_distances_and_indices.append((distance, index))
        sorted_neighbor_distances_and_indices = sorted(neighbor_distances_and_indices)
        k_nearest_distances_and_indices = sorted_neighbor_distances_and_indices[:k]
        k_nearest_labels = [data[i][1] for distance, i in k_nearest_distances_and_indices]
        return k_nearest_distances_and_indices , choice_fn(k_nearest_labels)

    def mean(self,labels):
        return sum(labels) / len(labels)

    def euclidean_distance(self,point1, point2):
        sum_squared_distance = 0
        for i in range(len(point1)):
            sum_squared_distance += math.pow(point1[i] - point2[i], 2)
        return math.sqrt(sum_squared_distance)

    def main(self):
        reg_data = self.data.getData()
        reg_query = [int(self.InputtedTime)]
        reg_k_nearest_neighbors, reg_prediction = self.knn(reg_data, reg_query, k=10, distance_fn=self.euclidean_distance, choice_fn=self.mean)
        res = [str(x) for x in str(reg_prediction)] 
        return(self.format(res))

    def format(self,time):
        for t in time:
            if t == ".":
                time.remove(t)
                del time[-1]
        formattime = []
        #if time is 5449 under a minute
        if len(time) == 5:
            time.insert(0,"0")
            time.insert(2, ":")
            time.insert(5,".")
        else: 
            time.insert(0,"0")
            time.insert(0, "0")
            time.insert(2,":")
            time.insert(5, ".")
        return time


if __name__ == "__main__":
    x = KNN("50FreestyleData", 4456)
    print(x.main())

    