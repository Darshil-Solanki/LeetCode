class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        if not bank: return -1
        bank = set(bank)
        queue, seen = [(startGene, 0)], set()
        geneSet = ['A','C','G','T']
        while queue:
            curr_len = len(queue)
            for i in range(curr_len):
                cur_gene, moves = queue.pop(0)
                seen.add(cur_gene)
                for i in range(4):
                    for j in range(8):
                        if geneSet[i]==cur_gene[j]:
                            continue
                        newGene = cur_gene[:j]+geneSet[i]+cur_gene[j+1:]
                        if newGene not in seen and newGene in bank:
                            if newGene==endGene:
                                return moves+1
                            queue.append((newGene,moves+1))

        return -1
