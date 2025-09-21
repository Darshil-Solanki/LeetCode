class MovieRentingSystem:
    def __init__(self, n: int, entries: List[List[int]]):
        self.shop_to_movie = {i:defaultdict(int) for i in range(n)} 
        self.movie_to_shop = defaultdict(list)
        self.prices = defaultdict(int)
        self.rented_heap = []
        movies = set()
        for shop, movie, price in entries:
            self.shop_to_movie[shop][movie] = price
            self.movie_to_shop[movie].append((price, shop))
            self.prices[(shop, movie)] = price
            movies.add(movie)
        
        for movie in movies:
           heapify(self.movie_to_shop[movie])


    def search(self, movie: int) -> List[int]:
        cheap_shop = []
        heap = []
        for i in range(5):
            if not self.movie_to_shop[movie]:
                for _ in heap:
                    heappush(self.movie_to_shop[movie], _)
                return cheap_shop
            _, top_shop = self.movie_to_shop[movie][0]
            while not self.shop_to_movie[top_shop][movie]:
                heappop(self.movie_to_shop[movie])
                heap.append((_, top_shop))
                if not self.movie_to_shop[movie]:
                    for _ in heap:
                        heappush(self.movie_to_shop[movie], _)
                    return cheap_shop
                _, top_shop = self.movie_to_shop[movie][0]

            heappop(self.movie_to_shop[movie])
            heap.append((_, top_shop))
            cheap_shop.append(top_shop)

        for _ in heap:
            heappush(self.movie_to_shop[movie], _)
        return cheap_shop

    def rent(self, shop: int, movie: int) -> None:
        price = self.shop_to_movie[shop][movie]
        self.shop_to_movie[shop][movie] = 0
        heappush(self.rented_heap, (price, shop, movie))

    def drop(self, shop: int, movie: int) -> None:
        self.shop_to_movie[shop][movie] = self.prices[(shop, movie)]     

    def report(self) -> List[List[int]]:
        cheap_movie = []
        heap = []
        for i in range(5):
            if not self.rented_heap:
                for _ in heap:
                    heappush(self.rented_heap, _)
                return cheap_movie
            t_p, t_s, t_m = self.rented_heap[0]

            while self.shop_to_movie[t_s][t_m] or (t_p, t_s, t_m) in heap:
                heappop(self.rented_heap)
                if not self.rented_heap:
                    for _ in heap:
                        heappush(self.rented_heap, _)
                    return cheap_movie
                t_p, t_s, t_m = self.rented_heap[0]

            heappop(self.rented_heap)
            heap.append((t_p, t_s, t_m))
            cheap_movie.append((t_s, t_m))
            
        for _ in heap:
            heappush(self.rented_heap, _)
        return cheap_movie


# Your MovieRentingSystem object will be instantiated and called as such:
# obj = MovieRentingSystem(n, entries)
# param_1 = obj.search(movie)
# obj.rent(shop,movie)
# obj.drop(shop,movie)
# param_4 = obj.report()

# from submissions
# using sortedlist is working better than heap
# from sortedcontainers import SortedList

# class MovieRentingSystem:

#     def __init__(self, n: int, entries: List[List[int]]):
        
#         self.store = defaultdict(int)
#         self.films = defaultdict(SortedList)
#         self.rental = set()

#         for shop, movie, price in entries:
#             self.store[(shop, movie)] = price
#             self.films[movie].add((price, shop))
            

#     def search(self, movie: int) -> List[int]:
#         a = self.films[movie][:5]
#         return [x[1] for x in a]


#     def rent(self, shop: int, movie: int) -> None:

#         price = self.store[(shop, movie)]
#         self.films[movie].discard((price, shop))
#         self.rental.add((price, shop, movie))
        

#     def drop(self, shop: int, movie: int) -> None:
 
#         price = self.store[(shop, movie)]
#         self.films[movie].add((price, shop))
#         self.rental.discard((price, shop, movie))
    

#     def report(self) -> List[List[int]]:

#         report_stores = sorted(self.rental)[:5]
#         return [[s, m] for p, s, m in report_stores]
