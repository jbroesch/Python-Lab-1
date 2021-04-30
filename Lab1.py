
def convert_kg(value):
	print(value, "kg converted is",(value * 2.20462),"pounds "\
    + "and", (value * 35.274 ),"ounces.") 

def convert_pounds(value):
    print(value,"pounds converted is",(value * 0.453592),"kg and",\
    (value * 16),"ounces.")

def convert_ounces(value):
    print(value,"ounces converted is",(value * 0.0283),"kg and",\
    (value * 0.0625),"pounds.")

if __name__ == "__main__":
	# Test your code here
    convert_kg(10)
    convert_pounds(10)
    convert_ounces(10)