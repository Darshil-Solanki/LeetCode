class FoodRatings:

    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.cuisines = defaultdict(list)
        self.food_rating = defaultdict(int)
        self.food_to_cuisine = defaultdict(str)
        for food, cuisine, rating in zip(foods, cuisines, ratings):
            self.cuisines[cuisine].append((-rating, food))
            self.food_to_cuisine[food] = cuisine
            self.food_rating[food] = -rating

        for cuisine in self.cuisines:
            heapify(self.cuisines[cuisine])
        
    def changeRating(self, food: str, newRating: int) -> None:
        self.food_rating[food] = -newRating
        heappush(self.cuisines[self.food_to_cuisine[food]], (-newRating, food))

    def highestRated(self, cuisine: str) -> str:
        while self.cuisines[cuisine] and self.cuisines[cuisine][0][0]!= self.food_rating[self.cuisines[cuisine][0][1]]:
            heappop(self.cuisines[cuisine])
        max_rat, ans = heappop(self.cuisines[cuisine])
        max_list = [(max_rat, ans)]
        while self.cuisines[cuisine] and self.cuisines[cuisine][0][0]==max_rat:
            max_list.append(heappop(self.cuisines[cuisine]))

        for r, f in max_list:
            heappush(self.cuisines[cuisine], (r, f))
            ans = min(ans, f)

        return ans


# Your FoodRatings object will be instantiated and called as such:
# obj = FoodRatings(foods, cuisines, ratings)
# obj.changeRating(food,newRating)
# param_2 = obj.highestRated(cuisine)
