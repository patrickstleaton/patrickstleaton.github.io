#This program displays all different proposition combinations for three input variables.
table_count = 1
for a1 in range(0,2):
 for a2 in range(0,2):
  for a3 in range(0,2):
   for a4 in range(0,2):
    for a5 in range(0,2):
     for a6 in range(0,2):
      for a7 in range(0,2):
       for a8 in range(0,2):
		print "|-------------------|"
		print "|Truth Table: ", table_count 
		print "|-------------------|"
		print "|p q r | proposition"
		print "|-------------------|"
		print "|F F F | ", ('T' if a1 else 'F')
		print "|-------------------|"
		print "|F F T | ", ('T' if a2 else 'F')
		print "|-------------------|"
		print "|F T F | ", ('T' if a3 else 'F')
		print "|-------------------|"
		print "|F T T | ", ('T' if a4 else 'F')
		print "|-------------------|"
		print "|T F F | ", ('T' if a5 else 'F')
		print "|-------------------|"
		print "|T F T | ", ('T' if a6 else 'F')
		print "|-------------------|"
		print "|T T F | ", ('T' if a7 else 'F')
		print "|-------------------|"
		print "|T T T | ", ('T' if a8 else 'F')
		print "|-------------------|\n\n"
		table_count += 1


