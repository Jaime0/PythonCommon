out_file = open("test.csv", 'w')
out_file.write("test")
out_file.close()



  with open("test.csv", "w") as out_file:
      out_file.write("test")
  out_file.close()
