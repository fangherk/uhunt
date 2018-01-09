from sys import stdin

def main():

	

	while(1):
		# read in the first time
		analog = stdin.readline()

		# read in the hour and minute 
		hour, minute = analog.strip().split(":")
		if(hour == "0" and minute == "00"):
			break
		# generate the minute from the minute
		minute = float(minute)
		# generate the hour val in terms of minutes
		hour = float(hour) * 5.0 % 60.0 +  (minute/60.0)*5.0 
		# print("hour: {}".format(hour))
		# print("minute: {}".format(minute))

		# take care of overflow error
		if hour > minute:
			difference = hour - minute
			if difference > 30:
				difference =  (minute+60.0) - hour 
		else:
			# minute > hour'
			difference = minute - hour
			if minute - hour > 30:
				difference =  (hour+60.0) - minute 

		# print("difference {}".format(difference))
		degrees = (difference / 30.0) * 180.0
		print("{:.3f}".format(round(degrees,3)))


if __name__ == "__main__":
	main()