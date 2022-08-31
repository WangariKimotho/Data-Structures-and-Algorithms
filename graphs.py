class Graph:
	def __init__(self,edges):
		self.edges = edges
		self.graph_dict = {}
		for start,end in self.edges:
			if start in self.graph_dict:
				self.graph_dict[start].append(end)
			else:
				self.graph_dict[start] = [end]	

		# print(self.graph_dict)	

	def get_paths(self,start,end,path=[]):
		path = path + [start]

		if start == end:
			return [path]

		if start not in self.graph_dict :
			return []	
		paths = []
		for node in self.graph_dict[start]:
			if node not in path:
				new_paths = self.get_paths(node,end,path)
				for p in new_paths:
					paths.append(p)
		return paths
		




if __name__=="__main__":
	routes = [
	("Nairobi","Thika"),
	("Nairobi","Kitui"),
	("Thika","Kitui"),
	("Thika","Nyeri"),
	("Kitui","Nyeri"),
	("Nyeri","Isiolo")
	]
	routes_graph = Graph(routes)
	start = "Nairobi"
	end = "Nyeri"

	print(f"Paths between {start} and {end}: ",routes_graph.get_paths(start,end))