
# This program helps me calculate a homework problem.
# It helps me calculate the equation and print out the answers
# without me doing any manual calculations.
# I can just copy and paste the result into my homework.

lambda_param = (1.0/8.0)
mu_param = 1.0
phi_param = 4.0
count = 1
timeOut_low_bound = 4.0
last_printed = False

def calculate(estimatedRTT, deviation, sampleRTT, timeOut, count, last_printed):
	if (not last_printed):
		difference = sampleRTT - estimatedRTT
		estimatedRTT = estimatedRTT + (lambda_param * difference)
		deviation = deviation + (lambda_param * (abs(difference) - deviation))
		timeOut = (mu_param * estimatedRTT) + (phi_param * deviation)

		print("Iteration " + str(int(count)) +
		"\tDifference: %.2f" % round(difference, 2),
		"\tEstimatedRTT: %.2f" % round(estimatedRTT, 2),
		"\tDeviation: %.2f" % round(deviation, 2),
		"\tTimeOut %.2f" % round(timeOut, 2))

		count = count + 1
		if (timeOut < timeOut_low_bound):
			last_printed = True
		calculate(estimatedRTT, deviation, sampleRTT, timeOut, count, last_printed)

estimatedRTT = input("input estimatedRTT: ")
deviation = input("input deviation: ")
sampleRTT = input("input sampleRTT: ")
timeOut_low_bound = input("input TimeOut lower bound: ")

estimatedRTT = float(estimatedRTT)
deviation = float(deviation)
sampleRTT = float(sampleRTT)
timeOut_low_bound = float(timeOut_low_bound)

calculate(estimatedRTT, deviation, sampleRTT, timeOut_low_bound + 1, count, last_printed)