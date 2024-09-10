#This is project 1, Semester 2, 2023 - CITS1401
#Author: Quoc Son Dang - 24060686

def main(csvfile, country):
    # Open and read the csv file
    with open(csvfile, "r") as infile:
        lines = infile.readlines()

    # Function that find the max and min org
    def max_Min(country):
        new_list = []

        # Skip the header lines
        for line in lines[1:]:
            data = line.split(",")
            name = data[1]
            country_list = data[3]
            year = data[4]
            employee_num = data[6]
            if country == country_list and 1981 <= int(year) <= 2000:
                new_list.append((name, employee_num))
        if len(new_list) <= 1:
            return "No max min appear" #This is for the special case Japan

        max_name = new_list[0][0]
        min_name = new_list[0][0]
        max_num = new_list[0][1]
        min_num = new_list[0][1]
        for name, employee_num in new_list: # Initiate the loops until discover max value
            if employee_num > max_num:
                max_num = employee_num
                max_name = name.lower() # The answer is in lowercase
            if employee_num < min_num:
                min_num = employee_num
                min_name = name.lower() # The answer is in lowercase
        return [max_name, min_name]

    maxMin = max_Min(country)

    # Function that find the standard deviation
    def stdv(country):
        input_country_salary = []
        total = []

        # Skip the header lines
        for line in lines[1:]:
            data = line.split(",")
            country_list = data[3]
            median_salary = data[7]
            total.append(float(median_salary)) # Convert to float

            if country == country_list:
                input_country_salary.append(float(median_salary)) # Convert to float

        if len(input_country_salary) <= 1: #This is for special case Japan
            sd_input = 0
        # Calculate the standard deviation for the org of input country if there is sufficient data
        else: 
            # Calculate the average value
            sum_salary_country = sum(input_country_salary)
            avg_salary_country = sum_salary_country / len(input_country_salary)
            
            # Calculate the numerator
            sqrt_to_avg = [(i - avg_salary_country) ** 2 for i in input_country_salary]
            
            # Calculate the standard deviation for the org of input country
            sd_input = (sum(sqrt_to_avg) / (len(sqrt_to_avg) - 1)) ** 0.5

        #Now, i started calculating the sd for all org
        if len(total) <= 1:
            sd_total = 0
        else:
            # Calculate the average value
            sum_salary_total = sum(total)
            avg_salary_total = sum_salary_total / len(total)
            
            # Calculate the numerator
            sqrt_to_avg_total = [(i - avg_salary_total) ** 2 for i in total]
            
            # Calculate the standard deviation for all org
            sd_total = (sum(sqrt_to_avg_total) / (len(sqrt_to_avg_total) - 1)) ** 0.5
        # Finally, round number to 4dp
        sd_round = round(sd_input, 4)
        total_sd_round = round(sd_total, 4)

        return [sd_round, total_sd_round]

    stdv = stdv(country)

    # Function that calculate the ratio
    def ratio(country):
        profit_changes_from_2020_to_2021 = []

        # Skip the header lines
        for line in lines[1:]:
            data = line.split(",")
            country_list = data[3]
            profit_2020 = float(data[8]) # Convert to float
            profit_2021 = float(data[9]) # Convert to float
            if country == country_list:
                profit_change = (profit_2021 - profit_2020)
                profit_changes_from_2020_to_2021.append(profit_change)

        # Calculate the sum of positive changes and negative changes
        sum_of_positive_change = sum([profit for profit in profit_changes_from_2020_to_2021 if profit > 0])
        sum_of_negative_change = abs(sum([profit for profit in profit_changes_from_2020_to_2021 if profit < 0]))

        if sum_of_negative_change == 0:
            ratio = 0 # avoid 0 in denominator
        else:
            ratio = round(sum_of_positive_change / sum_of_negative_change, 4)

        return ratio

    ratio = ratio(country)

    # Function that calculate the correlation coefficient
    def corr(country):
        positive_profit = []
        Median_salary_list = []

        for line in lines[1:]:
            data = line.split(",")
            country_list = data[3]
            median_salary = float(data[7])
            profit_2020 = float(data[8])
            profit_2021 = float(data[9])
            
            # First, I set up requirements
            # The second requirement helps me filter data to include the organisations where profits from 2020 to 2021 is positive
            if country == country_list and (profit_2021 - profit_2020) > 0:
                positive_profit.append(profit_2021)
                Median_salary_list.append(median_salary)

        if len(positive_profit) <= 1:
            correlation_coefficient = 0 # Return 0 for special cases like Japan
        else:
            
            # Then, I calculate the mean of profit in 2021 and the mean of salary (which is x-bar and y-bar respectively)
            avg_profit = sum(positive_profit) / len(positive_profit)
            avg_salary = sum(Median_salary_list) / len(Median_salary_list)
            
            # Next, I calculate the summation
            diff_profit_and_avg_profit = [i - avg_profit for i in positive_profit]
            diff_medsalary_and_avg_medsalary = [i - avg_salary for i in Median_salary_list]
            
            # Then, calculate numerator and denominator separately
            numerator = sum([x * y for x, y in zip(diff_profit_and_avg_profit, diff_medsalary_and_avg_medsalary)])
            denominator = (sum([i ** 2 for i in diff_profit_and_avg_profit]) * sum([i ** 2 for i in diff_medsalary_and_avg_medsalary])) ** 0.5
            
            # Check if the denominator is zero before calculating the correlation coefficient
            if denominator == 0:
                correlation_coefficient = 0 
            else:
                correlation_coefficient = round(numerator / denominator, 4) # round to 4dp

        return correlation_coefficient

    corr = corr(country)

    return maxMin, stdv, ratio, corr
