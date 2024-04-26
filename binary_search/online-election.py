class TopVotedCandidate:

    def __init__(self, persons: List[int], times: List[int]):
        self.times = times
        self.persons = persons

    def q(self, t: int) -> int:
        index = bisect_left(self.times, t)  #3 -> 0 #5 ->1

        if index == len(self.times) or self.times[index] > t:
            index -= 1

        persons = self.persons[:index + 1]  # [0:1]
        freq = Counter(persons)
        sorted_freq = freq.most_common()  #(value, freq)
        max_vote = sorted_freq[0][1]
        leadings = []
        for k, v in sorted_freq:
            if v < max_vote:
                break
            else:
                leadings.append(k)
        # return 1
        reverse_persons = persons.copy()[::-1]
        print(reverse_persons)
        return 1
        # for reverse_index in reverse_persons:
        #     for l in leadings:
        #         if l == reverse_persons[reverse_index]:
        #             return  l

        # return

        # max_vote = 0
        # leading_person = 0

        # for p in persons:
        #     freq[p] += 1
        #     if freq[p] >= max_vote:
        #         leading_person = p
        #         max_vote = freq[p]

        # return sorted_freq[0][0]


# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)
