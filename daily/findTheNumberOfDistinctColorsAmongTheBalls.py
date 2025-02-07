class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        balls = defaultdict(int)
        colors = defaultdict(int)
        result = []

        for ball, color in queries:
            if ball in balls:
                curr_color = balls[ball]
                if colors[curr_color]==1:
                    del colors[curr_color]
                else:
                    colors[curr_color]-=1
            balls[ball]=color
            colors[color]+=1
            result.append(len(colors))

        return result

        # color_of_ball = defaultdict(int)
        # balls_of_color = defaultdict(set)
        # result = []
        # for ball, color in queries:

        #     if ball in color_of_ball:
        #         curr_color = color_of_ball[ball]
        #         balls_of_color[curr_color].remove(ball)
        #         if not balls_of_color[curr_color]:
        #             del balls_of_color[curr_color]

        #     color_of_ball[ball]=color
        #     balls_of_color[color].add(ball)

        #     result.append(len(balls_of_color))
        # return result
