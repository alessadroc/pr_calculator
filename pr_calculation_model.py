from events import Events

events = Events()

def calculate_pr(event, place):
    try:
        rank = int(place)
        pr_bracket = {}
        
        if event == "solo cash cup opens":
            if rank > 10000:
                return "0"
            
            pr_bracket = events.solo_cash_cup_opens()
        
        elif event == "solo cash cup finals":
            if rank > 600:
               return "Rank is too low."
            
            pr_bracket = events.solo_cash_cup_finals()

        elif event == "fncs division 1":
            if rank > 10000:
                return "0"
            
            pr_bracket = events.fncs_division_1()

        elif event == "fncs division 2":
            if rank > 10000:
                return "0"
            
            pr_bracket = events.fncs_division_2()

        elif event == "fncs division 3":
            if rank > 10000:
                return "0"
            
            pr_bracket = events.fncs_division_3()
            
        elif event == "performance evaluation opens":
            if rank > 10000:
                return "0"
            
            pr_bracket = events.performance_evaluation_opens()
        
        elif event == "performance evaluation finals":
            if rank > 33:
                return "Rank is too low."
            
            pr_bracket = events.performance_evaluation_finals()
        
        elif event == "fncs showdown":
            if rank > 10000:
                return "Rank is too low."
            
            pr_bracket = events.fncs_showdown()

        # Interpolation logic
        sorted_brackets = sorted(pr_bracket.items(), key=lambda x: x[0][0])

        for (low, high), pr_value in sorted_brackets:
            if low == rank or high == rank:
                return pr_value

        lower_bound = None
        upper_bound = None

        for i in range(len(sorted_brackets) - 1):
            (low1, high1), pr1 = sorted_brackets[i]
            (low2, high2), pr2 = sorted_brackets[i + 1]

            if low1 <= rank <= high1:
                interpolated_pr = pr1 + ((rank - low1) * (pr2 - pr1) / (high1 - low1))
                return round(interpolated_pr, 2)

            if high1 < rank < low2:
                lower_bound = (high1, pr1)
                upper_bound = (low2, pr2)
            
        # If placement falls between two defined ranges
        if lower_bound and upper_bound:
            (P1, PR1) = lower_bound
            (P2, PR2) = upper_bound
            interpolated_pr = PR1 + ((rank - P1) * (PR2 - PR1) / (P2 - P1))
            return round(interpolated_pr, 1)
                   
        return "Placement out of range"

    except ValueError:
        return "Invalid input"
