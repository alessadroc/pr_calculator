import numpy as np
from io import BytesIO
from matplotlib.figure import Figure
from events import Events
from pr_calculation_model import calculate_pr

class Graph:
    def __init__(self, event, placement, user):
        self.event = event
        self.placement = placement
        self.user = user
    
    def get_png_bytes(self):
        fig = self.plot_graph()
        buf = BytesIO()
        fig.savefig(buf, format='png', dpi=300, bbox_inches='tight')
        buf.seek(0)
        return buf.getvalue()

    def plot_graph(self):
        # Data organisin
        data = self.lobf(self.event)
        x, y = zip(*data)
        x = np.array(x)
        y = np.array(y)

        # Get line of best fit
        m, b = np.polyfit(x, y, 1)
        lobf_y = m * x + b

        # Matplotlib figure
        fig = Figure(figsize=(6, 4))
        ax = fig.add_subplot(111)
        ax.scatter(x, y, color='purple', label='Data Points')
        ax.plot(x, lobf_y, color='black', linestyle='--', label='Line of Best Fit')

        # User's actual placement (the red dot)
        user_x = int(self.placement)
        user_y = calculate_pr(self.event, self.placement) # logic for y coordinate of users place
        ax.plot(user_x, user_y, 'ro', markersize=8, label=f"{self.user}'s Placement: {self.placement}")

        # Other graph details
        ax.set_title(f"{self.event} PR Curve")
        ax.set_xlabel("Placement")
        ax.set_ylabel("Points")
        ax.legend()

        return fig

    def lobf(self, event):
        events = Events()
        try:
            event_method_name = event.lower().replace(" ", "_")
            func = getattr(events, event_method_name)
        except AttributeError:
            print(f"Event '{event}' not found in Events.")
            return []

        ranges_dict = func()
        xy = []
        for placement_range, points in ranges_dict.items():
            start, end = placement_range
            for placement in range(start, end + 1):
                xy.append((placement, points))

        return xy