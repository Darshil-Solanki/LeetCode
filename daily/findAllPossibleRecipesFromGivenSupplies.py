class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        graph = {}
        supplies_set = set(supplies)
        
        for recipe, ingredient in zip(recipes, ingredients):
            graph[recipe] = ingredient
        
        ans = []
        prev_len = -1
        queue = deque(recipes)
        while queue:
            prev_len = len(ans)
            for i in range(len(queue)):
                recipe = queue.popleft()
                all_ingre = True
                for ingredient in graph[recipe]:
                    if ingredient not in supplies_set:        
                        all_ingre = False
                        break
                if all_ingre:
                    supplies_set.add(recipe)
                    ans.append(recipe)
                else:
                    queue.append(recipe)
            if len(ans)==prev_len:
                break
        return ans


        # slightly improved not need to have a graph using index for mapping
        # supplies_set = set(supplies)
        
        # ans = []
        # queue = deque(range(len(recipes)))
        # while queue:
        #     prev_len = len(ans)
        #     for i in range(len(queue)):
        #         recipe_idx = queue.popleft()
        #         all_ingre = True
        #         for ingredient in ingredients[recipe_idx]:
        #             if ingredient not in supplies_set:        
        #                 all_ingre = False
        #                 break
        #         if all_ingre:
        #             supplies_set.add(recipes[recipe_idx])
        #             ans.append(recipes[recipe_idx])
        #         else:
        #             queue.append(recipe_idx)
        #     if len(ans)==prev_len:
        #         break
        # return ans
