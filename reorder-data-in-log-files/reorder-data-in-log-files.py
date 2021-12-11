class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        digit_logs = list(filter(lambda a: a.split()[1].isdigit(), logs))
        letter_logs = list(filter(lambda a: a not in digit_logs, logs))
        letter_logs.sort(key = lambda a: (' '.join(a.split()[1:]), a.split()[0]))
        return [*letter_logs, *digit_logs]