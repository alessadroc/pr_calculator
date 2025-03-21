from events import Events

events = Events()

def calculate_pr(event, place):
    try:
        rank = int(place)
        event_pr_bonus = 0
        pr_bracket = {}
        
        if event == "Solo Cash Cup Opens":
            pr_bracket = events.solo_cash_cup_opens()
        
        elif event == "Solo Cash Cup Finals":
            pr_bracket = events.solo_cash_cup_finals()

        elif event == "FNCS Division 1":
            pr_bracket = events.fncs_division_1()

        elif event == "FNCS Division 2":
            pr_bracket = events.fncs_division_2()

        elif event == "FNCS Division 3":
            pr_bracket = events.fncs_division_3()
            
        elif event == "Performance Evaluation Opens":
            pr_bracket = events.performance_evaluation_opens()
        
        elif event == "Performance Evaluation Finals":
            pr_bracket = events.performance_evaluation_finals()


        # logic for interpolation
        prev_low, prev_high = None, None
        prev_pr = None

        for (low, high), pr_value in pr_bracket.items():
            if low <= rank <= high:
                # if rank is on a boundary, return exact PR
                return pr_value

            if prev_low is not None:
                if prev_high < rank < low:
                    # # y = y1 + ((x-x1)*(y2-y1)/(x2-x1))
                    PR1, PR2 = prev_pr, pr_value
                    P1, P2 = prev_high, low
                    interpolated_pr = PR1 + ((rank - P1) * (PR2 - PR1) / (P2 - P1))
                    return round(interpolated_pr, 2) + event_pr_bonus

            # retain brackets
            prev_low, prev_high = low, high
            prev_pr = pr_value

        return "Placement out of range"

    except ValueError:
        return "Invalid input"
