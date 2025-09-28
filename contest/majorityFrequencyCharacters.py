class Solution:
    def majorityFrequencyGroup(self, s: str) -> str:
        cnt = Counter(s)
        frequency_group = defaultdict(set)
        ans_freq = max_len = 0
        for c, freq in cnt.most_common():
            frequency_group[freq].add(c)
            if len(frequency_group[freq])>max_len:
                ans_freq = freq
                max_len = len(frequency_group[freq])
        return "".join(frequency_group[ans_freq])
