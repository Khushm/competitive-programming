class Solution:
	def floodFill(self, image, sr, sc, newColor):
	    if image[sr][sc] == newColor:
            return image
            
	    m = len(image)
	    n = len(image[0])
	    
	   # visited = [[False for j in range(n)] for i in range(m)]
	    oldColor = image[sr][sc]
	    
	    def is_safe(row, col):
	        return min(row, col) >= 0 and row < m and col < n
	   
	    def is_same_color(row, col):
	        return image[row][col] == oldColor
	   
	   # def is_not_visited(row, col):
	   #     return not visited[row][col]
	   
	    def dfs(row, col):
	       # visited[row][col] = True
	        image[row][col] = newColor
	        
	        nei = [(row, col+1), (row, col-1), (row+1, col), (row-1, col)]
	        for row1, col1 in nei:
	            if is_safe(row1, col1) and is_same_color(row1, col1): 
	               # and is_not_visited(row1, col1):
	                dfs(row1, col1)
	   
	    dfs(sr, sc)
	    return image
