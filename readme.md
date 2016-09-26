# Python arguments parsing module

Simple arguments parsing module without any dependencies with simple initialization and values getting.

## Installing

Just place _arguments.py_ near you python script and import arguments.Arguments.

## Usage

### Initialization

1. Create _Arguments_ instance. Custom callback can be passed for formatted error output
2. Add arguments to created instance with _addNewArg_ method. Params: 
	- *name*: name of argument. Used to find argument by it later
	- *key*: key of the argument to be used in command line
	- *help*: text with the argument description. Used to generate help page. Empty by default.
	- *isBool*: will be this argument used as boolean (was used or not during call). If False then next argument will be parsed as value for this one. False by default.
	- *defaultValue*: argument default value to be used if aurgument wasn't used during call. False for boolean arguments and None for others by default.

Example:

	import arguments.Arguments

	args = Arguments()
	args.addNewArg('debug', '-d', 'Enables debug mode', True, False)
	args.addNewArg('input', '-i', 'Input file')
	args.addNewArg('output', '-o', 'Ouput file. Default "out.txt"', defaultValue='out.txt')
	args.addNewArg('help', '-h', 'Prints this page', True)

### Parsing arguments

To parse arguments use _parseArgs_ method. Params:

- *args*: list of arguments to be parsed
- *stopOnError*: if True parsing will be stopped if some argument wasn't found in arguments list defined on initialization step. False by default.

Method returnes True if parsing was done without errors and False otherwise.

Example:

	res = args.parseArgs(sys.argv[1:], True)

Make attention that when parsing sys.argv, we should pass argument excluding the zero one because it's just script file path and not argument for parsing

### Getting value

To get value of the argument _getValue_ method is used. It takes _name_ of the argument as param. returns None if not found.

	def printValues(args):
		print 'debug:\t', args.getValue('debug')
		print 'input:\t', args.getValue('input')
		print 'output:\t', args.getValue('output')

### Print help

To print help use _printHelp_ method. Print callback can be passed if format output needed. Params for callback:

- *name*: name of the argument
- *key*: key of the argument
- *help*: help message of the argument

### Errors ouput

If default print not suitable for errors output callback can be used. It can be set on initalization stage as constructor parameter or with a _setErrorCallback_ method. Callback should get one parameter: message - as message that should be printed.

Example with lambda:
	
	# pass True to stop parsing on error
	res = args.parseArgs(sys.argv[1:], True)
	if (args.getValue('help') or not res):
		args.printHelp(lambda name, key, help: log.info("{0}: {1}\t- {2}".format(key, name, help)))

### Reseting

_resetValues_ method with no params can be used if need to reset all values to default.

### Test

See the test.py as example of module usage.