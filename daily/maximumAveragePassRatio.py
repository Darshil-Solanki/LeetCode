class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        def calculate_gain(pass_std, tot_std):
            return (pass_std+1)/(tot_std+1) - pass_std/tot_std

        heap = []
        for pass_std, tot_std in classes:
            gain = calculate_gain(pass_std, tot_std)
            heap.append((-gain, pass_std, tot_std))

        heapify(heap)

        for _ in range(extraStudents):
            gain, pass_std, tot_std = heappop(heap)
            heappush(heap, (-calculate_gain(pass_std+1, tot_std+1), pass_std+1, tot_std+1))

        tot_pass_ratio = sum(pass_std/tot_std for _, pass_std, tot_std in heap)
        return tot_pass_ratio/len(classes)
