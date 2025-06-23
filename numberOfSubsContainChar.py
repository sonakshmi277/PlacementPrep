def numberOfSubstrings(self, s: str) -> int:
        last_seen = {'a': -1, 'b': -1, 'c': -1}
        count = 0

        for i in range(len(s)):
            if s[i] in last_seen:
                last_seen[s[i]] = i

        # If all three seen, we can count substrings ending at i
            if -1 not in last_seen.values():
                min_index = min(last_seen.values())
                count += min_index + 1  # substrings starting from 0 to min_index

        return count
