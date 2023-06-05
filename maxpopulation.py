class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        years = [0] * 101  # Initialize a list to store population counts for each year

        # Iterate through the logs and count the number of people alive for each year
        for log in logs:
            birth_year, death_year = log
            for year in range(birth_year, death_year):
                years[year - 1950] += 1

        max_population = max(years)  # Find the maximum population count
        max_population_year = years.index(max_population) + 1950  

        return max_population_year
