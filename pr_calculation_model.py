def calculate_pr(event, place):
    try:
        rank = int(place)
        event_pr_bonus = 0
        
        if event == "Solo Cash Cup Opens":
            pr_bracket = {
                (1, 1): 1000,
                (2, 2): 900,
                (3, 3): 850,
                (4, 4): 825,
                (5, 5): 800,
                (6, 6): 775,
                (7, 7): 750,
                (8, 8): 725,
                (9, 9): 700,
                (10, 10): 625,
                (11, 20): 550,
                (21, 30): 475,
                (31, 40): 400,
                (41, 50): 350,
                (51, 60): 325,
                (61, 70): 300,
                (71, 80): 275,
                (81, 90): 250,
                (91, 100): 225,
                (101, 150): 200,
                (151, 200): 175,
                (201, 250): 150,
                (251, 300): 125,
                (301, 400): 100,
                (401, 500): 50,
                (501, 1000): 20,
                (1001, 2500): 15,
                (2501, 5000): 10,
                (5001, 7500): 5,
                (7501, 10000): 0
            }
        
        elif event == "Solo Cash Cup Finals":
            event_pr_bonus = 200
        elif event == "FNCS Division 1":
            event_pr_bonus = 500
        elif event == "FNCS Division 2":
            event_pr_bonus = 400
        elif event == "FNCS Division 3":
            event_pr_bonus = 300
        elif event == "Performance Evaluation":
            event_pr_bonus = 150

        # logic for interpolation
        prev_low, prev_high = None, None
        prev_pr = None

        for (low, high), pr_value in pr_bracket.items():
            if low <= rank <= high:
                # if rank is on a boundary, return exact PR
                return pr_value + event_pr_bonus

            if prev_low is not None:
                if prev_high < rank < low:
                    # interpolate between (prev_high, low) using (prev_pr, pr_value)
                    PR1, PR2 = prev_pr, pr_value
                    P1, P2 = prev_high, low

                    interpolated_pr = PR1 + ((rank - P1) * (PR2 - PR1) / (P2 - P1))
                    return round(interpolated_pr) + event_pr_bonus

            # retain brackets
            prev_low, prev_high = low, high
            prev_pr = pr_value

        return "Placement out of range"

    except ValueError:
        return "Invalid input"
