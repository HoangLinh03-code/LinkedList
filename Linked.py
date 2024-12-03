import tkinter as tk
from tkinter import messagebox
from LinkedList import Solu

class LinkedListVisualizer:
    def __init__(self, root):
        self.root = root
        self.root.title("Linked List Visualizer")

        self.list = Solu()

        # Input and buttons
        self.input_value = tk.Entry(root, width=20)
        self.input_value.grid(row=0, column=0, padx=10, pady=10)
        tk.Button(root, text="Add Node", command=self.add_node).grid(row=0, column=1, padx=10,pady=5)
        tk.Button(root, text="Delete Middle", command=self.delete_middle).grid(row=1, column=0, padx=10,pady=5)
        tk.Button(root, text="Odd-Even", command=self.odd_even).grid(row=1, column=1, padx=10,pady=5)
        tk.Button(root, text="Reverse", command=self.reverse_list).grid(row=2, column=0, padx=10,pady=5)
        tk.Button(root, text="Count Nodes", command=self.count_nodes).grid(row=2, column=1, padx=10,pady=5)
        tk.Button(root, text="Pair Sum", command=self.pair_sum).grid(row=3, column=0,columnspan=2, padx=10,pady=5)
        tk.Button(root, text="Clear List", command=self.clear_list).grid(row=3, column=1,columnspan=2, padx=10,pady=5)
        

        # Canvas for visualization
        self.canvas = tk.Canvas(root, width=600, height=200, bg="white")
        self.canvas.grid(row=4, column=0, columnspan=2, pady=20)

    def draw_list(self):
        """Draw the linked list on the canvas."""
        self.canvas.delete("all")  # Clear the canvas
        nodes = self.list.print()
        x, y = 50, 100  # Starting position

        for i, value in enumerate(nodes):
            # Draw node as a rectangle with text
            self.canvas.create_rectangle(x, y - 20, x + 40, y + 20, fill="lightblue")
            self.canvas.create_text(x + 20, y, text=str(value))

            # Draw arrow to the next node
            if i < len(nodes) - 1:
                self.canvas.create_line(x + 40, y, x + 80, y, arrow=tk.LAST)
            x += 80  # Move to the next node position

    def add_node(self):
        """Add a node to the linked list."""
        value = self.input_value.get()
        if value.isdigit():
            self.list.addToList(int(value))
            self.draw_list()
            self.input_value.delete(0, tk.END)
        else:
            messagebox.showerror("Invalid Input", "Please enter a valid integer.")

    def delete_middle(self):
        """Delete the middle node of the linked list."""
        self.list.delMid()
        self.draw_list()

    def odd_even(self):
        """Rearrange the list in odd-even order."""
        self.list.OddEvenList()
        self.draw_list()

    def reverse_list(self):
        """Reverse the linked list."""
        self.list.reList()
        self.draw_list()

    def count_nodes(self):
        """Count the nodes in the linked list."""
        count = self.list.count()
        messagebox.showinfo("Node Count", f"The linked list has {count} nodes.")
    def pair_sum(self):
        """Maximum Twin Sum of a Linked List"""
        ans = self.list.pairSum()
        messagebox.showinfo("Node Pair Sums", f"The linked list pair sum is {ans}")
    def clear_list(self):
        """Clear the entire linked list."""
        self.list.clear()  # Clear the linked list
        self.draw_list() 


# Main application
if __name__ == "__main__":
    root = tk.Tk()
    app = LinkedListVisualizer(root)
    root.mainloop()