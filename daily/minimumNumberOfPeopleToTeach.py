class Solution:
    def minimumTeachings(self, n: int, languages: List[List[int]], friendships: List[List[int]]) -> int:
        languages = [set(lang) for lang in languages]

        language_users = [0]*n
        user = set()
        for f1, f2 in friendships:
            if languages[f1-1].isdisjoint(languages[f2-1]):
                user.add(f1)
                user.add(f2)

        for u in user:
            for l in languages[u-1]:
                language_users[l-1] += 1
                
        return len(user)-max(language_users)
