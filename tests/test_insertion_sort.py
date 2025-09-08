"""
Pytest test for insertion-sort.R script.

This test runs the R script and checks if the output contains
a sorted sequence of numbers in ascending order.
"""

import subprocess
import pytest

def test_insertion_sort_output():
    # Run the R script using Rscript command
    result = subprocess.run(
        ["Rscript", "src/insertion-sort.R"],  # Adjust path if needed
        capture_output=True,
        text=True
    )
    
    # Ensure the script executed successfully
    assert result.returncode == 0, "R script did not run successfully"
    
    # Check if the final sorted output contains the expected sequence
    assert "1 2 3 4 5 6" in result.stdout, "Sorted output not found in script output"
