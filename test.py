from arguments import Arguments
import logging as log
import sys

def initArguments():
	# init module and set custom callback
	args = Arguments(argumentsErrorCallback)

	# add some testing arguments
	args.addNewArg('debug', '-d', 'Enables debug mode', True, False)	# Don't need any additional value
	args.addNewArg('input', '-i', 'Input file')							# Will use next argument as value and None by default
	args.addNewArg('output', '-o', 'Ouput file. Default "out.txt"', defaultValue='out.txt')	# Will be "out.txt" if not switched in arguments list
	args.addNewArg('help', '-h', 'Prints this page', True)				# User asked to print help. No additional value needed and False by default as boolean value
	args.addNewArg('custom', '-c', 'Use custom help ouput', True)
	return args

def printValues(args):
	# Try to find values by names
	print 'debug:\t', args.getValue('debug')
	print 'input:\t', args.getValue('input')
	print 'output:\t', args.getValue('output')

def argumentsErrorCallback(message):
	log.error('\t' + message)

def main():
	log.basicConfig(level=log.INFO)
	args = initArguments()
	res = args.parseArgs(sys.argv[1:], True)

	if (args.getValue('help') or not res):
		if (args.getValue('custom')):
			# print help with custom callback
			args.printHelp(lambda name, key, help: log.info("{0}: {1}\t- {2}".format(key, name, help)))
		else:
			# print help without customization
			args.printHelp()
	else:
		print "\nWas read"
		printValues(args)
		args.resetValues()
		print "\nAfter reset"
		printValues(args)

		# Trying to find invalid value
		print '\n\nrandom', args.getValue('random')

if __name__ == '__main__':
	main()