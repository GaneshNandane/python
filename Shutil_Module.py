import shutil
#copy a file
shutil.copy("src_txt","dst_txt")
#copyting a directorty
shutil.copytree("src_dir","dst_dir")
#Moving a file
shutil.move("demo/sam_txt","sam_txt")
#deleting a dirctory
shutil.rmtree("demo") 