import unittest

from maze import Maze

class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m1._cells),
            num_cols,
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_rows,
        )
    def test_maze_reset_cells_visited(self):
        m1=Maze(0,0, 10,10, 10,10)
        m1._reset_cells_visited()
        visited_count=0
        for c in m1._cells:
            for d in c:
                self.assertEqual(
                        d.visited,
                        False,
                        )

if __name__ == "__main__":
    unittest.main()


