def calculate_pr(event, place):
    try:
        rank = int(place) 
        event_pr_bonus = 0  
        
        if event == "Solo Cash Cup Opens":
            event_pr_bonus = 100
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
        
        result = rank + event_pr_bonus
        return result 
    
    except ValueError:
        return "Invalid input"  # non numeric input handler
