import tkinter as tk

class CenterPanel:
    def __init__(self, root):
        """Set up the simulation panel with a canvas for visualization."""
        self.simulation_frame = tk.Frame(root, bg="#f0f0f0", padx=10, pady=10)
        self.simulation_frame.grid(row=0, column=1, sticky="nsew")

        self.simulation_label = tk.Label(
            self.simulation_frame, text="Simulation", font=("Arial", 14, "bold"), bg="#f0f0f0"
        )
        self.simulation_label.pack(anchor="w", pady=(0, 5))

        # Create the simulation canvas
        self.simulation_canvas = tk.Canvas(
            self.simulation_frame,
            bg="#ffffff",
            width=800,
            height=700,
            highlightbackground="#000000",
            highlightcolor="#000000",
            highlightthickness=2
        )
        self.simulation_canvas.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)

        # Bind events for zoom and pan
        self.simulation_canvas.bind("<MouseWheel>", self._zoom_simulation)
        self.simulation_canvas.bind("<ButtonPress-1>", self._start_pan)
        self.simulation_canvas.bind("<B1-Motion>", self._pan_simulation)

        self.current_scale = 1.0
        self.min_scale = 0.5
        self.max_scale = 2.0
        self.canvas_start_x = 0
        self.canvas_start_y = 0

        # Reset canvas after layout is ready
        self.simulation_canvas.after(100, self.reset_canvas)

    def reset_canvas(self):
        """Reset the canvas to its initial state with centered content."""
        self.simulation_canvas.delete("all")
        canvas_width = self.simulation_canvas.winfo_width()
        canvas_height = self.simulation_canvas.winfo_height()
        center_x = canvas_width // 2
        center_y = canvas_height // 2
        radius = 50

        # Draw a blue circle at the center
        self.simulation_canvas.create_oval(
            center_x - radius, center_y - radius,
            center_x + radius, center_y + radius,
            fill="blue", tags="example"
        )

        # Update scroll region and center the view
        self.simulation_canvas.configure(scrollregion=self.simulation_canvas.bbox("all"))
        scrollregion = self.simulation_canvas.bbox("all")
        if scrollregion:
            left, top, right, bottom = scrollregion
            canvas_width = self.simulation_canvas.winfo_width()
            canvas_height = self.simulation_canvas.winfo_height()

            x_offset = (right - left - canvas_width) / 2
            y_offset = (bottom - top - canvas_height) / 2

            self.simulation_canvas.xview_moveto(x_offset / (right - left))
            self.simulation_canvas.yview_moveto(y_offset / (bottom - top))

        # Reset zoom scale
        self.current_scale = 1.0

    def _zoom_simulation(self, event):
        """Zoom in or out on the canvas content."""
        scale_factor = 1.1 if event.delta > 0 else 0.9
        new_scale = self.current_scale * scale_factor

        if not (self.min_scale <= new_scale <= self.max_scale):
            return

        self.current_scale = new_scale
        x = self.simulation_canvas.canvasx(event.x)
        y = self.simulation_canvas.canvasy(event.y)
        self.simulation_canvas.scale("all", x, y, scale_factor, scale_factor)
        self.simulation_canvas.configure(scrollregion=self.simulation_canvas.bbox("all"))

    def _start_pan(self, event):
        """Start panning by capturing the initial position."""
        self.canvas_start_x = self.simulation_canvas.canvasx(event.x)
        self.canvas_start_y = self.simulation_canvas.canvasy(event.y)

    def _pan_simulation(self, event):
        """Pan the canvas content based on mouse movement."""
        new_x = self.simulation_canvas.canvasx(event.x)
        new_y = self.simulation_canvas.canvasy(event.y)

        dx = new_x - self.canvas_start_x
        dy = new_y - self.canvas_start_y

        self.simulation_canvas.move("all", dx, dy)
        self.canvas_start_x = new_x
        self.canvas_start_y = new_y
        self.simulation_canvas.configure(scrollregion=self.simulation_canvas.bbox("all"))
