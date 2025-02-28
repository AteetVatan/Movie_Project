"""The DataHelpers Module."""


class DataHelpers:
    """The DataHelpers Class."""

    @staticmethod
    def find_median(values: list) -> float:
        """Method to find rating data median."""
        length = len(values)
        if length % 2 == 0:  # Even
            index = int(length / 2)
            return (values[index - 1] + values[index]) / 2
        index = length // 2
        return values[index]

    @staticmethod
    def fuzzy_string_matching(movie_rating_list: list, search_text: str) -> list:
        """Method to find fuzzy strings matches."""
        distance_dict = {}
        for item in movie_rating_list:
            distance = DataHelpers.levenshtein_distance(search_text, item[0])
            distance_dict[item] = distance

        sorted_distance_key_list = sorted(distance_dict.items(), key=lambda x: x[1])
        sorted_movie_list = [x[0] for x in sorted_distance_key_list]
        if len(movie_rating_list) > 5:
            return sorted_movie_list[:6]
        return sorted_movie_list[:1]

    @staticmethod
    def levenshtein_distance(a, b):
        """Method implementing levenshtein_distance Algorithm."""
        n, m = len(a), len(b)
        # Create an array of size NxM
        dp = [[0 for i in range(m + 1)] for j in range(n + 1)]

        # Base Case: When N = 0
        for j in range(m + 1):
            dp[0][j] = j
        # Base Case: When M = 0
        for i in range(n + 1):
            dp[i][0] = i
        # Transitions
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if a[i - 1] == b[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = 1 + min(
                        dp[i - 1][j],  # Insertion
                        dp[i][j - 1],  # Deletion
                        dp[i - 1][j - 1]  # Replacement
                    )

        return dp[n][m]
    # endregion Private static Methods
