# Ask the user for a search query
$query = Read-Host "Enter your search query"
$cursor = Read-Host "Enter the cursor (leave empty for default)"
# If the cursor is empty, set it to 0
if (-not $cursor) {
    $cursor = 0
}

# Define the file where search results will be saved
$today = Get-Date -Format "yyyy-MM-dd"
$resultsFile = "${today}_${query}_links.txt"

Write-Host "Searching for '$query'..."
# Launch search.py with the query and output file arguments
python .\search.py --q $query --o $resultsFile --c $cursor

# Check if search.py created the results file
if (Test-Path $resultsFile) {
    Write-Host "Search completed. Now starting download..."
    # Launch download_from_file.py passing the results file as argument
    python .\download_from_file.py --file_with_links $resultsFile
} else {
    Write-Error "Error: Expected results file '$resultsFile' not found."
}